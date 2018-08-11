#!/usr/bin/python
# -*- coding: UTF-8 -*- 
print 'hell'
if True:
    print 'YES'
else:
    print 'NO'

var1 = 10
print var1
del var1

var2 = "hello"

print var2*8

for letter in 'python':
    if letter == 't':
        pass
        print "这是pass块"
    else:
        print "字母是:",letter

def printname(age, name):
    "传入任意字符"
    print age
    print name
    return


printname(age=10,name="你好");



