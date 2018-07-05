#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "例子4-1:使用了嵌套循环输出2~100之间的素数："
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            print i, "还能被", j, '整除'
        j = j + 1
    if j > i / j:
        print
    i = i + 1

print "Good bye!"
