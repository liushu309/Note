## 1. Faster-rcnn
### 1.1训练
第一步使用随机梯度下降（Stochastic Gradient Descent，简称SGD）训练RPN网络，通过ImageNet中预训练模型进行初始化后进行端到端的微调;  
第二步利用第一步训练好的 RPN网络生成的包围盒单独训练 Fast R-CNN 网络，此时两个网络的卷积层是独立的;  
第三步利用 Fast R-CNN 的卷积层初始化 RPN 网络，然后固定共享的卷积层，只微调 RPN 网络中独有的层，实现了网络中卷积层的共享;  
第四步保持共享的卷积层固定，微调 Fast R-CNN 中用于分类的全连接层。经过这四步训练，RPN 网络与 Fast R-CNN 网络实现了卷积层的共享，构成统一的系统.  

## 2. SSD


## 3. YOLO_v3
