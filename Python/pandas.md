## 1. 使用pandas将excel文件所有包含子字符串关键字的记录筛选出来

    import pandas as pd

    # 定义Excel文件路径和关键字列表
    filename = './example.xlsx'
    keywords = ['银行', '金融']

    # 读取Excel文件
    data = pd.read_excel(filename)

    # 筛选包含任意一个关键字的记录

    series_ret = data['文件名称'].str.lower().str.contains('|'.join(keywords))
    print('series_ret\n', series_ret)

    filtered_data = data[series_ret]

    # 输出筛选后的数据
    print('ret\n', filtered_data)
    with pd.ExcelWriter('output.xlsx',engine='xlsxwriter',options={'strings_to_urls': False}) as writer:
            filtered_data.to_excel(writer, index=False)


## 2. 对pandas数据的基本操作(增册改查)
    import pandas as pd

    # 创建一个DataFrame
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})

    # 查询数据
    # 查询所有数据
    print(df)
    # 根据列名查询数据
    print(df['Name'])
    # 根据行号查询数据
    print(df.loc[0])

    # 增加数据
    # 增加一行数据
    df.loc[3] = ['Dave', 40]
    # 增加一列数据
    df['Gender'] = ['Female', 'Male', 'Male', 'Male']

    # 修改数据
    # 修改一行数据
    df.loc[1] = ['Bobby', 31, 'Male']
    # 修改一列数据
    df['Gender'] = ['Female', 'Male', 'Male', 'Female']
    # 修改某行某列
    df[0, 'Name'] = 'is you Bob?'

    # 删除数据
    # 删除一行数据
    df = df.drop(2)
    # 删除一列数据
    df = df.drop('Gender', axis=1)


