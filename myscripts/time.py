#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "time.py"
#  
sec = int(input('Введите кол-во секунд: '))
h = sec // 3600
m = (sec-h*3600) // 60
s = sec % 60

if h % 10 == 1 and h % 100 != 11:
    hn = 'час'
elif h % 10 == 2 and h % 100 != 12 or h % 10 == 3 and h % 100 != 13 or h % 10 == 4 and h % 100 != 14:
    hn = 'часа'
else:
    hn = 'часов'
    
if m % 10 == 1 and m % 100 != 11:
    mn = 'минута'
elif m % 10 == 2 and m % 100 != 12 or m % 10 == 3 and m % 100 != 13 or m % 10 == 4 and m % 100 != 14:
    mn = 'минуты'
else: 
    mn = 'минут'
    
if s % 10 == 1 and s % 100 != 11:
    sn = 'секунда'
elif s % 10 == 2 and s % 100 != 12 or s % 10 == 3 and s % 100 != 13 or s % 10 == 4 and s % 100 != 14:
    sn = 'секунды'
else:
    sn = 'секунд'
if sec != 0:    
    print(h, hn, m, mn, s, sn)
