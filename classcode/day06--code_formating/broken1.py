#!/usr/bin/env python
var1=0
#var1 = total
input_list=[]
input_number=None
while input_number!="":
    input_number=raw_input()
    if input_number.isdigit():
        input_list.append(float(input_number))
        
for var in input_list:
    var1+=var
    
print var1/len(input_list)
