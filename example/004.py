#!/usr/bin/python
# -*- coding:UTF-8 -*-
print int("8")
dateStr = raw_input("请输入时间")
print dateStr
dateArr = dateStr.split("-")
year =(int)(dateArr[0])
print int("8")
month = (int)(dateArr[1])

day = (int)(dateArr[2])

months = (0,31,59,90,120,151,181,212,243,273,304,334)
sumday = 0
if month>=1 and month<= 12:
    sumday = months[month-1]
else:
    print "date error"
sumday += day
leap = 0
if (year % 400==0) or ( year %4==0 and year %100 != 0):
    leap = 1
if   leap ==1 and month>2:
    sumday += 1
print "这是第%d天" %sumday  



