## 1. 图像视频采集
### 1. 保存图像
按键1就按计数命名保存图像

    #include <opencv2/opencv.hpp>
    #include <stdio.h>
    #include <iostream>

    int main(){
        cv::VideoCapture capture(0);
        char file_name[64];
        int count = 0;
        bool camera_flag = true;

        cv::Mat frame;

        while(camera_flag){
            capture >> frame;
            cv::imshow("test", frame);
            int key = cv::waitKey(1);
            if(key == 49){
                sprintf(file_name, "./Image/%04d.jpg", count);
                count += 1;
                cv::imwrite(file_name, frame);
                // TODO 保存图像
            }else if(key == 27){
                camera_flag = false;
            }
        }
        return 0;
    }

### 2. 保存视频
按Esc键结束

    #include <opencv2/opencv.hpp>
    #include <stdio.h>
    #include <iostream>

    int main(){
      cv::VideoCapture cap(0);

      if (!cap.isOpened())
      {
        printf("open video failed!\n");
        return 1;
      }

      cv::Mat Frame;

      //设置保存的视频帧数目
      int frameNum = 100;
      //保存视频的路径
      std::string outputVideoPath = "./Image/liushu.avi";
      //获取当前摄像头的视频信息
      cv::Size sWH = cv::Size((int)cap.get(CV_CAP_PROP_FRAME_WIDTH),
        (int)cap.get(CV_CAP_PROP_FRAME_HEIGHT));
      cv::VideoWriter outputVideo;
      outputVideo.open(outputVideoPath, CV_FOURCC('M', 'P', '4', '2'), 25.0, sWH);

        bool stop_flag = false;

      while (cap.isOpened() && !stop_flag)
      {
        cap >> Frame;
        if (Frame.empty()) break;
        outputVideo << Frame;
        frameNum--;

        imshow("img", Frame);
        int key = cv::waitKey(1);

            if (key == 27){
                stop_flag =  true;
            }
      }

      outputVideo.release();
    }
