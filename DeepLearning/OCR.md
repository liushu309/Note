## 1. ctpn
1. 使用常用的卷积层;  
2. 使用一个卷积层代替Ｎ*Ｃ*Ｈ*Ｗ -> N*9*C*H*W;  
3. 使用双向循环神经网络以Ｃ为数据,Ｗ为一个sequence(相当于一个句子),对特征图层进行升维;  
4. 使用RPN网络进行单个box回归;  
5. 使用迭代算法,
