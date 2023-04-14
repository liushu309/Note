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


## 2. 对pandas数据的基本操作
    ```python
    import pandas as pd

    # 假设数据是一个包含字典的列表，每个字典表示一条记录，键表示字段
    data = [{'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30},
            {'name': 'Charlie', 'age': 35}]

    # 将数据转换为pandas DataFrame
    df = pd.DataFrame(data)

    # 查找年龄大于30的记录
    result = df[df['age'] > 30]

    # 输出结果
    print(result.to_dict('records'))
    # Output: [{'name': 'Charlie', 'age': 35}]

    # 修改名字为Bob的记录的年龄为40
    df.loc[df['name'] == 'Bob', 'age'] = 40

    # 输出修改后的结果
    print(df.to_dict('records'))
    # Output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 40}, {'name': 'Charlie', 'age': 35}]
