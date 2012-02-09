#!/usr/bin/env python

print ("Please Enter positive integers less than 256")
num1 = int(raw_input("First: "))
num2 = int(raw_input("Second: "))
num3 = int(raw_input("Third: "))
num4 = int(raw_input("Fourth: "))
num5 = int(raw_input("Fifth: "))

print ("Integer |  Binary  | Hexidecimal")
# print ("%i%s|%s|%s") % (num1, " "*(if  (num1>100): 1 elif (num1>10): 2 else: 3)), bin(num1), hex(num1)0
print ("%i%s|%s%s|%s") % (num1, int((8-len(str(num1))))*" ", bin(num1), int((10-len(str(bin(num1)))))*" ", hex(num1))
print ("%i%s|%s%s|%s") % (num2, int((8-len(str(num2))))*" ", bin(num2), int((10-len(str(bin(num2)))))*" ", hex(num2))
print ("%i%s|%s%s|%s") % (num3, int((8-len(str(num3))))*" ", bin(num3), int((10-len(str(bin(num3)))))*" ", hex(num3))
print ("%i%s|%s%s|%s") % (num4, int((8-len(str(num4))))*" ", bin(num4), int((10-len(str(bin(num4)))))*" ", hex(num4))
print ("%i%s|%s%s|%s") % (num5, int((8-len(str(num5))))*" ", bin(num5), int((10-len(str(bin(num5)))))*" ", hex(num5))