# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:48:24 2026

@author: AT
"""

a = float(input("first number:"))
op = input("operation  (+ - * /):" )
b = float(input("second number"))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op =="/":
    if op != 0:
        print(a / b)
    else:
        print("Error : Division by zero")
else:
    print("invalid operation")    
    