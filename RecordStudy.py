#!/usr/bin/python
# -*- coding: UTF-8 -*-


#    分支：即是if-else和if-elif-else语句
#
# 　　循环：即是while 和 for循环
#
# 　　另外还有while-else和for-else结构
#

# if-else和if-elif-else语句
# 1.if语句 elif语句和else语句没有括号，且后面要有“：”冒号
# 2.以代码的缩进来表示层次关系（而不像C使用大括号哦）
# 例子1：3个数从大到小输出

print "例子1：3个数从大到小输出:"
n1 = 3
n2 = 5
n3 = 4
if n1 > n2:
    if n2 > n3:
        print "n1>n2>n3"
    elif n3 > n1:
        print "n3>n1>n2"
    else:
        print "n1>n3>n2"
elif n1 < n2:
    if n2 < n3:
        print "n3>n2>n1"
    elif n3 < n1:
        print "n2>n1>n3"
    else:
        print "n2>n3>n1"
# 注意：如果代码是在.py文件中运行，可能需要指定编码格式utf-8,
# 在文件开头写上#incoding=utf-8或#incoding:utf-8即可。

# while循环
# 1.格式如c语言，但while条件没有括号，同样需要冒号
# 2.循环体同样以代码缩进表示
# 例子2：累加0-2
print "例子2：累加0-2："
i = 0
s = 0
# n = raw_input("number:")无法使用？why？
# print n
while i < 3:
    s = s + i
    i = i + 1
print s

# for循环
# 1.类似于其它语言中的foreach语句
# 2.同样需要冒号“：”
# 例子3：循环输出单词‘today’中的每一个字母
print "例子3：循环输出单词‘today’中的每一个字母:"
for a in 'today':
    print "current char:" + a
# for-else和while-else结构
# 1.在循环正常执行完成后执行else语句。
# 2.什么是不正常执行完呢？比如使用break语句
# 例子4：for-else结构
print "例子4：for-else结构:"
fruits = ['banana', 'apple', 'mengo']
for fruit in fruits:
    print "current fruit:" + fruit
    if fruit == 'apple':
        break  # 有了break,就不会执行else
else:
    print "OK!"
# Python 循环嵌套
# Python 语言允许在一个循环体里面嵌入另一个循环。
#
# Python for 循环嵌套语法：
#
# for iterating_var in sequence:
#    for iterating_var in sequence:
#       statements(s)
#    statements(s)
# Python while 循环嵌套语法：
#
# while expression:
#    while expression:
#       statement(s)
#    statement(s)
# 你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环。
#
# 实例4-1：以下实例使用了嵌套循环输出2~100之间的素数：
print "例子4-1:使用了嵌套循环输出2~100之间的素数："
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print i, " 是素数"
    i = i + 1

print "Good bye!"

# python中的list列表是一种序列型数据类型，一有序数据集合用逗号间隔用方括号括起来，和字符串一样可以通过索引index和切片来访问某个元素或子列表。
#
# 　　元组相当于一个只读的列表，它的元素不可修改。
#
# 　　字典是一种键值对。
#
# list列表
# 可以类比于其它语言（如，C语言）的数组，其起始下标为也为0。
# 1.列表的索引访问
# 　　1）通过list_name[index]来访问，每个列表的起始下标为0。
# 例子5：
print "例子5："
my1 = [1, 2, 3, 4]  # 列表的定义
print type(my1)  # 打印类型
print my1[0]  # 输出第一个元素
print my1[1]  # 输出第二个元素

# 2）可以通过del list_name[index]来删除列表的下标是index的数据。
# 例子6：
print "例子6："

my2 = [1, 2, 3, 4]  # 列表的定义
del my2[2]  # 删除第三个元素
print my2  # 输出整个列表

# 2.列表的切片访问
# 　　1）想访问列表里一段连续的元素（或规则间隔的元素）可以指定列表的起止位置和终止位置、间隔的步长(可省，默认为1)。语法格式list_name(start:end[:step])表示访问下标为start至end-1的元素，step可省略，可以简记为前闭后开。
# 例子7：
print "例子7："
demolist = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 列表的定义
print demolist[0:5]  # 访问第1-5的元素
print demolist[0:8:2]  # 访问第1-8的元素，步长为2
#
# 　　2）同样也可以使用del list_name(start:end[:step])来删除对应的元素。
# 例子8：
print "例子8："
demolist = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 列表的定义
del demolist[0:8:2]  # 删除下标为0到7的元素
print demolist  # 输出整个列表

# 3.列表的基本运算
# 　　1）列表的加法：列表可以同字符串一样相加。
# 例子9：
print "例子9："
demolist = [1, 2, 3, 4]  # 列表的定义
print demolist + [5, 6, 7, 8, 9]

# 　　2）列表的乘法：相当于字符串的乘法，一个列表乘（*）以N次，表示这个列表相加了N次。
# 例子10：
print "例子10："
demolist = ["y", "y", "c"]  # 列表的定义
print  demolist * 3  # 列表可以做乘法

# 　　3）列表的in和not in运算：用于判断某个元素是否在（不在）列表中。在返回True,不在返回False。
# 例子11：
print "例子11："
demolist = [1, 2, 3, 4]  # 列表的定义
print 2 in demolist  # 判断元素是否在列表中
print 21 in demolist

# 　　4）列表的遍历：可以通过像字符串那样使用for循环来遍历列表。
# 例子12：
print "例子12："
demolist = [1, 2, 3, 4]  # 列表的定义
i = 0
for value in demolist:
    print 'demolist[%d]: ' % i, value
i += 1

# 　　5）列表的解析：可以方便的对列表中的元素进行运算，语法格式：[val_expr for val in
# list_name]，val_expr是一个关于val的运算表达式，val用于存储for每次从列表中取出的元素，然后通过val_expr的运算形成一个新的列表项，for循环结束则生成一个新的列表。
# 例子13：计算1-9每个数本身的次方，如2**2 = 4
print "例子13：计算1-9每个数本身的次方，如2**2 = 4："
demolist = range(1, 10)  # 列表的定义:生成一个[1,10)的列表
print demolist
new_list = [x ** x for x in demolist]
print new_list

# 4.列表相关函数
# TIPS--->列表的函数很多，这里有个小技巧：遇到这种很多函数又记不住，可以通过help 函数查看该类型拥有的所有方法，例如：
print "例子14:"
demolist = [1, 2, 3, 4]  # 列表的定义


def help(demolist):
    pass


print help(demolist)  # 通过help函数查看该类型所有的函数方法

#  通过help查看的list相关函数
# 如果只记得方法名不知道参数怎么传了，可以用help(变量名.方法名)，例如15：
print "例子15:"

demolist = [1, 2, 3, 4]  # 列表的定义
demolist.pop()  # 1出桟，删除最后一个元素
print demolist

demolist.pop(1)  # 2出桟，删除下标为1的元素
print demolist

demolist.append(20)  # 3追加一个数
print demolist

demolist.append('hello')  # 4还可以追加一个字符串、实型等任何类型
print demolist

demolist.append(['a', 'b', "c", 20])  # 5甚至还可以追加一个列表，（注：python中字符用单引号双引号都一样）
print demolist

print len(demolist)  # 6列表长度

demolist.insert(2, [8, 9, 10])  # 7在列表的指定位置插入元素（可以时任意对象，如这里就是插入的一个列表）
print demolist

print demolist.count(20)  # 8统计某个值在列表中出现的次数

demolist.extend([20, 100, 200, 300])  # 9将指定的列表以个体的方式追加到列表的末尾
print demolist
demolist.remove(20)  # 10删除列表中第一次出现的指定元素
print demolist

# 5.多维列表
# 　　　　其实前面已经体会到了，列表里可以嵌套一个列表，这就形成了多维列表。
#
# 　　　例子16：
print "例子16:"
demolist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 定义二维列表相当于一个3*3的二维数组
print demolist
print demolist[0]  # 输出第一行
del demolist[0]  # 删除第一行
print demolist

# 元组
# 1）元组的结构和访问、使用方法和列表基本一致，区别主要有两点：1.使用圆括号将各个数据项包括起来  ；2.元组里的值不可修改。
# 例子17：
print "例子17:"

# 元组相当于一个只读的列表，它的元素不能修改
demotuple = (1, 3, 5, 6, 8, 9)  # 定义元组，用圆括号
print demotuple  # 只能读不能写
print demotuple[2:5]  # 输出下标为2到5的字元组

# 2）多维元组：和多维列表相似，同时具备元组的相关特性
#
# 例子18：
print "例子18:"
# 同样也可以类似于二维数组
tuple1 = ((1, 2), (3, 4), (5, 6))  # 定义多维元组
print tuple1  # 打印整个二维元组
print tuple1[0]  # 打印第一行
print tuple1[0][1]  # 打印第一行第二个元素

# 字典
# 字典的元素是由一对对键值对组成，每一对之间用逗号隔开，将所有的键值对用花括号括起来就构成了字典。它是无序的，键和值之间用冒号隔开。
# 语法格式：dic_name={key:value,key:value,key:value}
# 简单来说：
# 　　1.类似于json,也就是key-value键值对
# 　　2.不允许同一个键值出现两次，所以一般对字典的操作都是对键进行操作。
# 　　3.键必须不可变，所以可以用数字，字符串，元组充当，而不能用列表
# 例如19：
print "例子19:"
dic = {"key1": "value1", "key2": "value2", "key3": "value3"}  # 定义字典
# 1.字典的基础操作
# 　　
# 　　1）可以增加、删除、修改、访问字典中的元素。同样也可以求字典的长度。
# 例子：
dic = {"key1": "value1", "key2": "value2", "key3": "value3"}  # 定义字典
print dic  # 打印整个字典
print dic["key2"]  # 根据key找value

del dic['key1']  # 根据key删除元素(通过键删除一个键值对)
print dic

dic['key4'] = "value4"  # 可以直接添加一个原字典里没有的元素(key不存在就行)
print dic

dic["key2"] = 45678  # 修改字典中的某值
print dic  # 打印整个字典

print len(dic)  # 字典的长度

# 2）也可以通过字典的in运算对字典进行遍历（其实是用的for循环），也可以用来判断某个键是否在字典中。
#
# 例子20：
print "例子20:"

dic = {"key1": "value1", "key2": "value2", "key3": "value3"}  # 定义字典
for key in dic:
    print key, dic[key]  # 遍历字典并输出

print 'key1' in dic  # 判断键值为key1是否存在于字典中
print 'key5' in dic

#  2.字典的相关函数
#
# 　　1）字典复制copy函数：字典的copy方法可以新建一字典与拷贝对象里的数据项一样。
# 例子21：
print "例子21:"

dic = {"key1": "value1", "key2": "value2", "key3": "value3"}  # 定义字典
dic1 = dic.copy()  # 字典复制
print dic
print dic1
del dic1['key3']  # dic1是dic的一个副本，对dic1进行操作不影响dic
print dic
print dic1

# 2）字典的get函数和update函数：dic_name.get(key_name)函数等价于dic_name[key_name]用来获取某键对应的值。update(key_value)函数用来更新字典里对应Key的值，如果要更新的key在字典里不存在，则update就向字典里增加数据。
# 例子22：
print "例子22:"

dic = {"key1": "value1", "key2": "value2", "key3": "value3"}  # 定义字典
print dic
print dic.get('key1')  # 相当于dic['key1']
dic.update({'key1': 'value8'})  # 更新key1的值
print dic
dic.update({'key5': 'value9'})  # 增加key5
print dic

# 3）字典里的keys()、values()、items()函数：他们返回的都是一个列表。keys()获取字典的所有Key,values()获取字典的所有value，items()获取字典的key,value值。
# 例子23：
print "例子23:"

dic = {"key1": "value1", "key2": "value2", "key3": "value3"}  # 定义字典
print dic
print dic.keys()  # 获取所有的Key
print dic.values()  # 获取所有的value
print dic.items()  # 获取所有的key,value

# 4）字典dict()函数：创建字典的函数
# 例子24：
print "例子24:"

d0 = dict()  # 创建空字典
print d0

d1 = dict(a='123', b=456)  # 通过赋值创建字典 ,key不能加引号,value如果是字符串就要加引号，是数字可以不加
print d1

key = range(1, 3)
value = ['john', 'Tom', 'Jack']
d2 = dict(zip(key, value))  # 通过一对列表创建字典
print d2

# 4）字典的pop()、popitem()和clear()函数：pop()函数用于通过key来获取其value值并从字典里删除该数据项。popitem()函数随机移除一个数据项并返回移除的数据项(元组形式返回)。clear()函数用于清除字典数据项。
# 例子25：
print "例子25:"

dic = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5"}  # 定义字典
print dic

print dic.pop('key2')  # 删除key2并返回Key2对应的value值
print dic
print dic.popitem()  # 随机删除一对数据项，并以元组形式返回该数据项
print dic

dic.clear()  # 清空字典的条目
print dic

# 字符串定义和访问　
# 1.字符串基础
# 　　a.字符串可以用单引号、双引号、三引号(单、双)定义，其中，单引号和双引号定义的字符串没啥区别，三引号有点区别。下面通过例子来看。
# 例子26：
print "例子26:"
str1 = 'hello'
str2 = "hello"
str3 = 'hello3 hello'
print str1, str2, str3
# 以上三种没有区别

print type(str1), type(str2), type(str3)
str4 = 'hello "dear"'
print str4
str5 = "hello \"dear\" "
print str5
str6 = 'hello \'dear\''
print str6
# 　从代码中可以看出，一对单引号，一对双引号没有区别，都是str类型。但是不能有双引号或单引号出现两对进行嵌套，如例子中的str5,
# str6这几个字符串，如果要这样使用就要加一个斜杠当做转义字符，因为Python它会从左到右找成对的引号，如果写成str5="hello "dear""这样子的话，就会找不到合适的匹配方法，报错。
# 　　b.下面这种情况也比较特殊：使用三对单引号
# 例子27：
print "例子27:"
str7 = '''"hello 'dear'"'''  # 三对单引号
# str7 = '''"hello \'dear\'"'''  # 这里加上转义字符也可以
print str7
str8 = '''hello 'hey' "Tom"'''
print str8
#
# 可以发现，一个字符串的最外层是三个单引号，则它不会关心引号里面的单引号和双引号，直接输出里面的内容。
# 所以如果需要输出的字符串里有引号建议使用这种方式。
# 综上，可以总结为：在不使用转义字符的情况下，单引号里可以有双引号，双引号里可以有单引号，三引号里既可以有单引号也可以有双引号。
# 常见的转义字符有：
#
# \n   回车换行
# \t    制表符
# \"    双引号
# \'    单引号
# \\    输出斜杠
#
# c.原字符串：比如下面这个例子，我希望"\"后面的字母不被python看作是转义字符，在字符串前面加上一个字母‘r’即可。
# 例子28：
print "例子28:"
print "c:\temp\node\wwm.py"
print r"c:\temp\node\wwm.py"
# d.字符串的更新：以下例子说明python中，字符串的更新不是在原地址上更新，而是重新开辟了一块新的地址空间。
# 例子29：
print "例子29:"

t = 'abc'
print id(t)  # id() 函数用于获取对象的内存地址。
t = 'asad'
print id(t)
c = 'abc'
print id(t)
#
# 2.字符串的访问
# 　　a.索引访问：字符串是python的一种序列型的数据类型，字符串里的每一个字符都有一个标号可以标识其在字符串中的位置，
# 从左至右依次是0，1，2...n-1，从右至左依次是-1，-2，-3....-n（其中n是字符串的长度），所有我们就可以通过索引来访问字符串中的某个字符。
# 例子30：
print "例子30:"

s = 'hello world!!'
print s[0]
print s[-3]

# b.切片访问：访问字符串中某个范围的子串。
# 语法格式：str_name[start:end:step]，start是访问字符串的起点，end为终点，step为步长，得到的子串由start到end-1这些字符组成(前闭后开)。
# 例子31：
print "例子31:"
s = '123456789123456789'
print s[0:6]
print s[1:20:2]

# 甚至还可以这样：
# 例子32：
print "例子32:"
s = '123456789abcdefghi123456789'
# 正切片
print s[:20]  # 不指定start
print s[2:]  # 不指定end
print s[9:-9]  # 指定end为负数
print s[:]  # 不指定start和end相当于print s
print s[::3]  # 只指定步长
# 反切片
print s[::-1]
print s[17:-19:-1]
print s[-10:-19:-1]
#
# 字符串的运算
# 1.字符串的加法和乘法
# 　　python中不但支持字符串相加，还支持字符串的乘法，使用起来相当方便。加法就是将两个字符串连接在一起，而乘法就是字符串的多次相加。
# 例子33：
print "例子33："

str8 = 'hello '
str9 = 'world!'
# 字符串连接
print str8 + str9
# 实现10个段横线的输出
print "-" * 10
# 输出3个hello
print str8 * 3

# 2.字符串的成员运算符
# 　　1）in和not in 运算：in 运算用于判断某个字符或子串是否在字符串中，
# not  in运算符与in 运算相反用于判断某个字符或子串是否不在字符串中。
# 例子34：
print "例子34:"
# 如果字符串中包含给定的字符串,返回True
str8 = 'hello'
print 'he' in str8
# 如果字符串中不包含给定的字符串，返回True
print 'hc' not in str8

# 例子34-1
print "例子34-1"
a = 10
b = 20
list1 = [1, 2, 3, 4, 5]
if a in list1:
    print "1-变量 a 在给定的列表中list1 中"
else:
    print "1-变量 a 不在给定的列表中list1 中"
if b not in list1:
    print "2-变量 b 不在给定的列表中list1 中"
else:
    print "2-变量 b 在给定的列表中list1 中"
# 修改变量a的值
a = 2
if a in list1:
    print "3-变量 a 在给定的列表中list1 中"
else:
    print "3-变量 a 不在给定的列表中list1 中"

# 2）字符串的格式化（支持占位符）
# 例子35：
# 字符串的格式化（支持占位符）
print "例子35:"
dic = ('wwm', 45)
print 'my name is %s,weight is %d kg.' % dic

# 字符串函数
# 字符串拥有很多函数，下面的例子中是最常用的，以例子来说明。
# 例子36：
print "例子36:"
mystr = 'hello world start leaning and hello and world!'
print mystr.find('and')  # 查找字符串中第一个'and'出现的位置
print mystr.find('and', 27)  # 从第27的位置开始找
print mystr.find('and', 0, len(mystr))  # 从第一个字符到字符串结尾找第一个'and'出现的位置，可以缺省start ,end即起止参数
# -----mystr.rfind() 从右开始查找
print mystr.index('and')  # 和find差不多，但是index中的参数在mystr中不存在则会抛出异常
print mystr.count("and")  # 统计'and'出现的次数，同样和find一样可以有3个参数
mystr1 = mystr.encode(encoding="utf-8")  # 按指定编码方式编码
print type(mystr1)
mystr2 = mystr1.decode(encoding="utf-8", errors="strict")  # 按指定编码方式解码，
# errors参数为strict，如果编码错误会抛出ValueError异常，除非errors指定的是ignore或replace
print mystr2
print type(mystr2)
print mystr.replace('and', 'or')  # 字符串替换函数，返回替换后的字符串，但是mystr本身并没有改变,除非mystr=mystr.replace('and','or')
print mystr
print mystr.replace('and', 'or', 1)  # 只替换一次
print mystr.split(' ')  # 按照空格进行分割，放到一个列表里
print mystr.split(' ', 3)  # 按照空格分割成4个子串
# ****************另外字符串还有很多判断函数（查文档吧，太多了）**********************

# 变量
# 在前面的系列中也许就可以发现，python中的变量和C中的变量有些许不同。比如在C中：
# include <stdio.h>

# int main(void)
# {
#     /* code */
#     int a,b,c;
#     int *p,*q,*t;
#
#     a = 5,b=8,c=5;
#     p = &a;
#     q = &b;
#     t = &c;
#     printf("%d\n",p);
#     printf("%d\n",q);
#     printf("%d\n",t);
#     return 0;
# }
# 输出：
#
# 6487604
# 6487600
# 6487596

# 　从输出结果可以看出，虽然a和c的值是一样的，但是a和c的地址是不同的。也就是说a开始赋值为5开辟了一块空间，当c赋值为5时又会给它分配一块空间。
# 　　但是在python 中就不同，如下的例子。
# 例子37：
print "例子37:"
# ----------变量--------
a = 5
b = 8
c = 5
print id(a)  # id(变量名) 用于取变量的地址
print id(b)
print id(c)

# 从上面两个例子中我们可以看出区别：
# 　1）c语言中定义变量需要定义变量类型，具体这个变量是int、long还是char等等，
# 而python中不关心变量的类型，直接定义变量，它会自己寻找最合适的类型进行存储，可通过type(变量名)来查看变量的类型，
# 在前面的系列中也可以看出python的变量没有类型，比如定义一个字符串str则可以直接：str = "hello"。
# 　　2）c语言中定义变量时不管内存空间中有没有这个值都会重新开辟一块新的空间，
# 而python中如果在内存空间中存在一个相同的值，就不会开辟新空间，直接将变量指向这块空间。
