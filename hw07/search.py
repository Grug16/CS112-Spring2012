#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums=input_nums()
nums = sorted(nums) #the Sorted function doesn't change the original value.  It needs to be set.
print "I have sorted your numbers"
print nums
x=int(raw_input("Which number should I find? : ")) # you forgot to convert the input to an integer.  Otherwise it would remain a string, which you can't use in math.
min=0 # I renamed m to min and M to max, so they're easier to tell apart.
max=(len(nums))-1 # must be -1 to avoid overflow
while  max>=min: # If they're the same, you've found it.
    mid=int((max+min)/2) # order of operations is imporant, Billy
    # Here are some print functions that might help you keep track of what is what.
    
    print "min is ",min
    print "max is", max
    print "mid is" , mid
    print "x is", x
    
    if nums[mid]==x:
        break
    elif x>nums[mid]:
       min=(mid+1)
       print "Too Low.  Increasing min"
    else:
        max=(mid-1)
        print "Too High.  Decreasing Max"
    
        
if nums[mid]==x:
    print "Found", x, "at", mid
else:
    print "Could not find", x
