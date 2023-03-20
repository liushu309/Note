## 1. 使用pandas将excel文件所有包含子字符串关键字的记录筛选出来

    import pandas as pd

    # 定义Excel文件路径和关键字列表
    filename = './example.xlsx'
    keywords = ['印发', '通知', '《']

    # 读取Excel文件
    data = pd.read_excel(filename)

    # 筛选包含任意一个关键字的记录

    series_ret = data['文件名称'].str.lower().str.contains('|'.join(keywords))
    print('series_ret\n', series_ret)

    filtered_data = data[series_ret]

    # 输出筛选后的数据
    print('ret\n', filtered_data)
    filtered_data.to_excel('output.xlsx', index=False)
