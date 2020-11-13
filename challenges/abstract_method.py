#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.7.8
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Create a leaderboard. Use the python ABC
#                   module to create an abstract parent method
#                   and define implementation of that method in a child class.
#
#   Tested OS:      Written and tested with Windows 10.


from abc import ABC, abstractmethod

class Leaderboard(ABC):
    def playerScore(self, score):
        print("Your score is: ",score)

    # Creates an abstract method that a child class can define and use
    @abstractmethod
    def insertScore(self, score):
        pass



class TetrisScore(Leaderboard):
    def insertScore(self, score):
        user = "SAM"
        lboard = {"DEX": 4500, "WIL": 4299, "FRD": 4001, "GBL": 3990, "ADM": 4490}
        # Adds new entry into dictionary
        lboard.update({user: score})
        # Sorts dictionary by value in ascending order
        newlboard = sorted(lboard.items(), key = lambda kv:(kv[1], kv[0]))
        print("\nCurrent leader board:")
        # For loop to print values in descending order
        for k, v in reversed(newlboard):
            print(k, v)


player = TetrisScore()
player.playerScore(4333)
player.insertScore(4333)
        
        
