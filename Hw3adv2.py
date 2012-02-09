#!/usr/bin/env python

num = raw_input("Numerator Please: ")
den = raw_input("Denominator Please: ")
num = int(num)
den = int(den)
print ("Reduced, that fraction is %i and %i/%i") % ((num / den), (num%den), den)