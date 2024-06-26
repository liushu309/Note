## 1. python re正则表达式模块
### 1.1 单字符匹配规则
    字符    功能
    .       匹配任意1个字符(除了\n)
    []      匹配[]中列举的字符
    \d      匹配数字,也就是0-9
    \D      匹配非数字,也就是匹配不是数字的字符
    \s      匹配空白符,也就是 空格\tab
    \S      匹配非空白符,\s取反
    \w      陪陪单词字符, a-z, A-Z, 0-9, _
    \W      匹配非单词字符, \w取反
    
### 1.2 表示数量的规则
    字符    功能
    *       匹配前一个字符出现0次多次或者无限次,可有可无,可多可少
    +       匹配前一个字符出现1次多次或则无限次,直到出现一次
    ?       匹配前一个字符出现1次或者0次,要么有1次,要么没有
    {m}     匹配前一个字符出现m次
    {m,}    匹配前一个字符至少出现m次
    {m,n}   匹配前一个字符出现m到n次
示例

    #首先清楚手机号的规则
    #1.都是数字 2.长度为11 3.第一位是1 4.第二位是35678中的一位
    pattern = "1[35678]\d{9}"
    phoneStr = "18230092223"
    result = re.match(pattern, phoneStr)
    result.group()
    # out
    '18230092223'

注意：当我们使用r原始字符串时,就不必考虑字符串的转移问题,更易集中解决字符匹配问题.

## 1.3 表示边界
    字符    功能
    ^       匹配字符串开头
    $       匹配字符串结尾
    \b      匹配一个单词的边界
    \B      匹配非单词边界

示例

    import re
    #定义规则匹配str="ho ve r"
    #1. 以字母开始
    #2. 中间有空字符
    #3. ve两边分别限定匹配单词边界
    pattern = r"^\w+\s\bve\b\sr"
    str = "ho ve r"
    result = re.match(pattern, str)
    result.group()

## 1.4 匹配分组
可以给表示数量的匹配符号使用，使分组整个用于数量

    字符        功能
    |           匹配左右任意一个表达式
    (ab)        将括号中字符作为一个分组
    \num        引用分组num匹配到的字符串
    (?P<name>)  分组起别名
    (?P=name)   引用别名为name分组匹配到的字符串
    
示例：匹配出0-100之间的数字  

    import re
    #匹配出0-100之间的数字
    #首先:正则是从左往又开始匹配
    #经过分析: 可以将0-100分为三部分
    #1. 0        "0$"
    #2. 100      "100$"
    #3. 1-99     "[1-9]\d{0,1}$"
    #所以整合如下
    pattern = r"0$|100$|[1-9]\d{0,1}$"
    #测试数据为0,3,27,100,123
    result = re.match(pattern, "27")
    result.group()

    #将0考虑到1-99上,上述pattern还可以简写为:pattern=r"100$|[1-9]?\d{0,1}$"
    # out:
    # 27
    
## 1. python beatifulsoup模块
### 1.1 示例
    from bs4 import BeautifulSoup
    import requests
    import re
    url = 'https://www.hhk278.com/meinv/list-V女郎.html'
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    demo = r.text  # 服务器返回响应
    soup = BeautifulSoup(demo, "html.parser")
    """
    demo 表示被解析的html格式的内容
    html.parser表示解析用的解析器
    """
    
    with open('ret.html', 'w', encoding='utf-8') as f:
        f.write(soup.text)
        f.write(soup.prettify())
    # 查找标签<a>的href属性中，含有4个数字以上的字段
    # ret = soup.find_all('a', attrs={'href' :re.compile('\d{4,}')})
    # 查找含有title属性的标签
    ret = soup.find_all(lambda tag:tag.has_attr('title'))
    # 标签名为<a>，子标签数量大于1，好像文本也算是一个子标签
    ret = soup.find_all(lambda tag:tag.name == 'a' and len(tag.contents) > 1 and tag.has_attr('title'))
