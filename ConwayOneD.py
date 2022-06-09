#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#importing ------------
import random
from turtle import update

#class defining-------------------------------------
max_pix = 20

class pixel():
    def __init__(self, index, status):
        self.status = status
        self.nextStatus = None
        self.index = index
        self.neighbors = 0

    def CalculateStatus(self):
        statusToLeft = initial_array[(self.index) - 1].status
        statusToRight = initial_array[((self.index) + 1) % max_pix].status

        if self.index == 0:
            self.CalculateNeigbors(statusToRight)
        elif self.index == max_pix:
            self.CalculateNeigbors(statusToLeft)
        else:
            self.CalculateNeigbors(statusToLeft + statusToRight)
        
        return self
    
    def CalculateNeigbors(self, neighbors):
        if self.status == 0:
            if (neighbors in ruleset['born']):
                self.nextStatus = 1
            else:
                self.nextStatus = 0
        elif self.status == 1:
            if (neighbors in ruleset['survive']):
                self.nextStatus = 1
            else:
                self.nextStatus = 0
    
    def updateStatus(self):
        self.status = self.nextStatus
        return self

def updateRuleset(password): # password is of form R*B**S** where the ** are any number of neighbors. * is the radius to check in. 
    print(ruleset)
    split_array = list(password)
    r = split_array.index('R')
    b = split_array.index('B')
    s = split_array.index('S')

    ruleset['radius'] = int(split_array[r + 1])
    ruleset['born'] = [int(x) for x in split_array[b + 1: s]]
    ruleset['survive'] = [int(x) for x in split_array [s + 1:]]
    print(ruleset)



#main-------------------------------------------
tracker = {"resolved": False, "ticker": 0}
ruleset = {"radius": 1, "born": [1], "survive": [0, 1]}
alternating_array = [pixel(x, x % 2) for x in range(0, max_pix + 1)]

initial_array = [pixel(x, random.randint(0,1)) for x in range(0, max_pix + 1)]
#initial_array = alternating_array
display_array = [p.status for p in initial_array]

print("initial state: {} \n".format(display_array))
#updateRuleset(str(input("Would you like to change the ruleset? use R*B**S**: ")))


while tracker['resolved'] == False:
    tracker['ticker'] = tracker['ticker'] + 1

    initial_array = [p.CalculateStatus() for p in initial_array]

    if [p.nextStatus for p in initial_array] == [p.status for p in initial_array]:
        print("\n" + "your final iteration: {}".format([p.nextStatus for p in initial_array]))
        print('1 step equality took {} iterations!'.format(tracker['ticker'] - 1))
        break

    initial_array = [p.updateStatus() for p in initial_array]
    display_array = [p.status for p in initial_array]
    print("{}: {}".format(tracker['ticker'], display_array))

    if tracker['ticker'] == 20:
        print('This initial condition didn\'t reach 1 step equality in {} loops!'.format(tracker['ticker']))
        tracker['resolved'] = True