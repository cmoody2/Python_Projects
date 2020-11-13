#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.7.8
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Creating a mock state sales tax calculator
#                   to demonstrate the use of protected and private
#                   attributes and methods.
#
#   Tested OS:      Written and tested with Windows 10.


from abc import ABC, abstractmethod

class Leaderboard(ABC):
    def playerScore(self, score):
        print("Your score is: ",score)

    @abstractmethod
    def insertScore(self, score):
        pass



class TetrisScore(Leaderboard):
    def insertScore(self, score):
        user = "SAM"
        lboard = {"DEX": 4500, "WIL": 4299, "FRD": 4001, "GBL": 3990, "ADM": 4490}
        lboard.update({user: score})
        newlboard = sorted(lboard.items(), key = lambda kv:(kv[1], kv[0]))
        print("\nCurrent leader board:")
        for k, v in reversed(newlboard):
            print(k, v)


player = TetrisScore()
player.playerScore(4333)
player.insertScore(4333)
        
        
