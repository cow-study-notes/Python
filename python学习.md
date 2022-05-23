#  python安装pip环境
## 1、想要在 Ubuntu 20.04 上为 Python 3 安装 pip，以 root 或者其他 sudo 用户身份在终端运行下面的命令：
- 1、sudo apt update
- 2、sudo apt install python3-pip

## 2、当安装结束，验证安装过程，检查 pip 版本：
- pip3 --version


小马视频官网：http://komavideo.com
课程文件：https://gitee.com/komavideo/learnpython3
https://www.youtube.com/watch?v=82dVQa6xBCA&list=PLliocbKHJNwsQ7fbMNwy20qR-SURFmhir&index=14
# Windows 安装python3.7
## python数据类型
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
    int（整型）
    float（浮点型）
## 命令行模式 
    ctrl+z 退出
    pyton -v 查看版本
    round() 四舍五入
    11//3 取整
    2**3 二的三次方
    title（）首字母大写
    upper（）大写
    lower（）小写
    r 使路径中的\无效
    print([1:5]) 取1-5字符
## 变量与字符串
    rstrip（） 去掉右边空白
    lstrip（） 去掉左边空白
    strip（） 去掉所有空白
## 数字运算
    numpy 数字运算基础库
    str() 字符串转函数
    示例：
        result = (2+3)*5
        print(result)
## 数组（列表list）
    列表按特定顺序排列的元素组成
    append（）增加元素
    del 删除元素
    pop 弹出元素删除
    remove 指名删除
    示例：
        mylist = ["baby","tony","callous"]
        print(mylist)
        print(mylist[0])
        print(mylist[0].title)
## 排序算法
    len（）计算列表长度
    sort（）升序排序
    reverse（）降序排序
    sorted（）全局升序排序
    示例：
        mylist = ["baby","tony","callous"]
        print(len（mylist）)
        mylist.sort()
        print(mylist）
        mylist.reverse()
        print(mylist）
## 数组循环
    enumerate() 循环索引（元组）
    示例：
        mylist = ["baby","tony","callous"]
        print（"start."）
        for name in mylist:
            print(name)
        print("End.")
## range（）的使用
    range（）函数生成数列
    min（）奇数
    max（）偶数
    sum（）求和
    示例：
        for val in range(6):
            print(val)
## 数组切片
    示例：
        mylist = ["baby","tony","callous"]
        print（mylist[0:1]）
## 元组的使用
    元组是特殊数组（列表），值不可变
    示例：
        mylist = (1,2,3,4,5,6,22)
        print(mylist)
        # 循环元组
        for val in mylist:
            print(val)        
## if条件
    if == 等于
    if != 不等于
    示例：
    mylist = ["baby","tony","callous"]
    for player in mylist:
        if player == "tony":
        print(player)
半夜2点了今天先学到这里，明天复习后接着学习python。现在接着学习英语



















