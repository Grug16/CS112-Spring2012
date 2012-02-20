#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums() #you forgot a _

print "Before sort:"
print nums

Length =len(nums) #value N is now Length.  No need to subtract 1.
for x in range(Length):
    p=x #saves the original value at that address. P changes
   
    for i in range(x+1, Length): #i is the new value, p is saved value.
        if nums[i]<nums[p]:
            p=i
            
    nums[p],nums[x]=nums[x],nums[p] #this needs to stay inside the first For loop.

print "After sort:"
print nums
