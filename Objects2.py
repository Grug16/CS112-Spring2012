#!/usr/bin/env python

class Student(object):
    def __init__(self, name):
        self.name = name
        
    def say(self, message):
        print self.name +": "+message
    
    def say_to(self,other,message):
        self.say(message+", "+other.name)
    def printf(self):
        print self.name

bob = Student("Bob")
fred = Student("Fred")
fred.say("No way")
juliet = Student("Juliet")
bob.say_to(fred, "I love you")
bob.say("Hi Fred.")
fred.say("Go away, Bob.")

class Course(object):
    def __init__(self, name):
        self.name = name
        self.enrolled=[]
    def enroll(self, student):
        self.enrolled.append(student)
    def printf(self):
        for student in self.enrolled:
            student.printf()
        
bob = Student("Bob")
fred = Student("Fred")
cs112 = Course("CS112")
cs112.enrolled.append(bob) #this is bad.  Better to use as a function than direct access
cs112.enroll(fred)
cs112.printf()

bob2 = bob
print bob2 is bob