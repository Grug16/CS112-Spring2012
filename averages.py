#!/usr/bin/env python

a = 0.0
b = 0.0
c = 0.0
scores = []
possible = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
for a in possible:
    for b in possible:
        for c in possible:
            scores.append((a+b+c)/3.0)

if scores:
    scores.sort()
    last = scores[-1]
    for i in range(len(scores)-2, -1, -1):
        if last == scores[i]:
            del scores[i]
        else:
            last = scores[i]
            
print scores
print len(scores)