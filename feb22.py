#!/usr/bin/env python

def ftoc(temp):
    cent = temp - 32
    cent*=5
    cent/=9
    return cent

pingas = int(raw_input("Fahrenheit: "))
print "In Celsius it is ", ftoc(pingas)