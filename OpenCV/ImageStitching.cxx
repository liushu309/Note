#include <stdio.h>
#include <iostream>
#include <vector>
#include "opencv2/opencv.hpp"
#include "opencv2/core/core.hpp"
#include "opencv2/xfeatures2d.hpp"
#include "opencv2/highgui/highgui.hpp"
using namespace cv;
using namespace std;

######################################################################
# 运行： ./test img1.jpg img2.jpg 2
# 2: 对图像进行缩放
######################################################################

int main(int argc, char **argv)
{
	std::string src_img_1 = "sub/000001.jpg";
	std::string src_img_2 = "sub/000030.jpg";
	if(argc > 1){
		src_img_1 = argv[1];
		src_img_2 = argv[2];
	}
	Mat src1 = imread(src_img_1);
	Mat src2 = imread(src_img_2);
	int scale_size = 2.0;
	if(argc > 3){
		float temp = 0.0;
		temp = atof(argv[3]);
		scale_size = temp;
		std::cout << "the scale is: " << scale_size << std::endl;
	}
    cv::resize(src1, src1, cv::Size(src1.cols / scale_size, src1.rows / scale_size));
    cv::resize(src2, src2, cv::Size(src2.cols / scale_size, src2.rows / scale_size));

	if (src1.data == NULL || src2.data == NULL)
	{
		cout << "No exist" << endl;
		return -1;
	}

	Ptr<Feature2D> surf = xfeatures2d::SURF::create();
	vector<KeyPoint> pic1key, pic2key;
	Mat des1, des2;
	surf->detectAndCompute(src1, Mat(), pic1key, des1);
	surf->detectAndCompute(src2, Mat(), pic2key, des2);
	//drawKeypoints(src1,pic1key,src1);

	FlannBasedMatcher matcher; //不使用暴力匹配，改成Fast Library for Approximate Nearest Neighbors匹配（近似算法，比暴力匹配更快）
	vector<DMatch> matches;
	matcher.match(des1, des2, matches);

	vector<Point2f> pic1, pic2; //滤掉误匹配点
	for (int i = 0; i < matches.size(); i++)
	{
		pic1.push_back(pic1key[matches[i].queryIdx].pt);
		pic2.push_back(pic2key[matches[i].trainIdx].pt);
	}
	vector<unsigned char> mark(pic1.size());
	Mat transM = findHomography(pic1, pic2, CV_RANSAC, 5, mark, 500);
	cout << "变换矩阵为：" << endl;
	cout << transM;
	vector<DMatch> optimizeMatch;
	for (int i = 0; i < matches.size(); i++)
	{
		if (mark[i])
			optimizeMatch.push_back(matches[i]);
	}
	//开始拼接
	Mat tempP;
	warpPerspective(src1, tempP, transM, Size(src1.cols * 2, src1.rows));
	Mat matchP(src1.cols * 2, src1.rows, CV_8UC3);
	tempP.copyTo(matchP);
	src2.copyTo(matchP(Rect(0, 0, src2.cols, src2.rows)));
	imshow("compare", tempP);
	imshow("compare1", matchP);

	//优化拼接线
	double lefttop[3] = {0, 0, 1};
	double leftbottom[3] = {0, src1.rows, 1};
	double transLT[3];
	double transLB[3];
	Mat _lefttop = Mat(3, 1, CV_64FC1, lefttop);
	Mat _leftbottom = Mat(3, 1, CV_64FC1, leftbottom);
	Mat _transLT = Mat(3, 1, CV_64FC1, transLT);
	Mat _transLB = Mat(3, 1, CV_64FC1, transLB);
	_transLT = transM * _lefttop;
	_transLB = transM * _leftbottom;
	double weight = 1;
	int leftline = MIN(transLT[0], transLB[0]);
	double width = src2.cols - leftline;
	for (int i = 0; i < src2.rows; i++)
	{
		uchar *src = src2.ptr<uchar>(i);
		uchar *trans = tempP.ptr<uchar>(i);
		uchar *match = matchP.ptr<uchar>(i);
		for (int j = leftline; j < src2.cols; j++)
		{
			if (trans[j * 3] == 0 && trans[j * 3 + 1] == 0 && trans[j * 3 + 2] == 0)
			{
				weight = 1;
			}
			else
			{
				weight = (double)(width - (j - leftline)) / width;
			}
			match[j * 3] = src[j * 3] * weight + trans[j * 3] * (1 - weight);
			match[j * 3 + 1] = src[j * 3 + 1] * weight + trans[j * 3 + 1] * (1 - weight);
			match[j * 3 + 2] = src[j * 3 + 2] * weight + trans[j * 3 + 2] * (1 - weight);
		}
	}

	imshow("output", matchP);
	waitKey(0);
	return 0;
}
