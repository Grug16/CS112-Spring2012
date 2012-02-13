#!/usr/bin/env python
from random import randint
s=1
input_length=int(raw_input())
rr=[]
for _ in range(input_length):
    rr.append(randint(0,20))
    #Generates "input_lenght" random numbers into list RR
print rr

rr.sort()
#while s:
#    s=0
#    for i in range(1,input_length):
#        if rr[i-1]>rr[i]:
#            #if the current element is greater than the previous, switch them
#            
#            
#            t1=rr[i-1]
#            t2=rr[i]
#            rr[i-1]=t2
#            rr[i]=t1
#            s=1
#            #s=1 means that if something gets switched, it will start from the beginning.
print rr
