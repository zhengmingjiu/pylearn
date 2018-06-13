﻿# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):

    argus=(a,b,c)
    for i in argus:
         if not isinstance(i, (int, float)):
            raise TypeError('bad operand type')
    d=b**2-4*a*c
    if a==0:
        return -c/b
    else:
        if d> 0:
            x1 = ((-b) + math.sqrt(d)) / (2*a)
            x2 = ((-b) - math.sqrt(d)) / (2*a)
            return x1, x2
        elif d == 0:
            x = (-b)/(2*a)
            return x
        else:
            return "No solution"
        
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
	
input