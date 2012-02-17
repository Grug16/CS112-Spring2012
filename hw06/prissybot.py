#!/usr/bin/env python

print "I am Nasty Bot.  What's your name, Maggot?"

name = raw_input() 

print "You mean, \"%s\" SIR!" % (name)

#asking again
name = raw_input("I'll ask you again.  What is your name!? \n")

print "%s?  That's a terrible name.  Your parents must have hated you.  I'm not surprised." % (name)
print "How tall are you, %s?" % (name)

# Height in centimeters.
height = raw_input("Insert Height in CM, and by god if you put something other than a number I will break your terminal.\n")
height = float(height)

# A Long story.
print "%f cm?  I didn't know they stacked shit that high." % (height)
print "Let me tell you a story. Once I met a man that was twice your height. \nThat's right, he was %f cm tall!" % (height*2)
print "And you know what else?  When the Russians cut his feet off he was %f cm tall." % (height*2-10)

# Percentage of difference between original height and modified height
print "Footless Joe, we used to call him.  And I'd say even without his feet, he was still %f%% as reliable as you." % (((height*2-10)/height)*100)
print "Do you have anything to say for yourself, you pickle-tickling doorhinge?"

words = raw_input()

print "I DIDN'T THINK SO.  GET OUT OF MY SIGHT!"