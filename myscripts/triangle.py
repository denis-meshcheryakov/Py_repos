#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "triangle.py"
#  
n = int(input())
for i in range(0,n):
    for j in range(0,n):
        if(j<n-i-1):
            print(" ",end=" ")
        else:
            print(i+1,end=" ")
    print()
