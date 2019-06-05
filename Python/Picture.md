## 设置画布大小

    import matplotlib.pyplot as plt
    # 单位百
    fig, ax = plt.subplot(1, 2, figsize=(16, 4))
    
## 添加图例
    import matplotlib.pyplot as plt
    
    # label为设置图像名称，但没有显示
    ax[i].plot(accuracies, label = 'accuracies')
    ax[i].plot(top_5_accuracies, label = 'top_5_accuracies')
    # 注意，legend没有的话，不显示
    ax[i].legend(loc="best")
  
## 设置标题
    ax[i].set_title(title)
    
## 保存图像
    fig, ax = plt.subplots(1, num_log, figsize=(16, 4))
    # 注意，尽量在show之前存在，不然可能出现空白的图
    fig.savefig('data/res.jpg')
    plt.show()