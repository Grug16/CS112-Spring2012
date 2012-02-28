#!/usr/bin/env python









s = "Monty Python"
print s[3:8]  #strings can be accessed like lists


people = {"Jonah" :"stupid",
          "Alec" : "smelly",
          "Jack" : "ugly",
          "Paul" : "awesome"}


name = raw_input("Your Name: ")
if name in people:
    print name,"is",people[name] #Address as a string instead of a number
else:
    print "I don't know you."

eng2sp = {}
color = (255, 10, 30, 255)
# Red, Green, Blue, Alpha
color = (0, 0, 0)
matrix=["hello",2.0,5,[10,20]]
eng2sp["one"]= "uno"
eng2sp["two"]= "dos"
for k,v in eng2sp.items():
    print k,v

print matrix

print matrix[0]
print matrix[1]
print matrix[2]
print matrix[3]
print matrix[3][0]
print matrix[3][1]