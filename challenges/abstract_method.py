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
        lboard = [4500, 4299, 4001, 3990]
        lboard.append(score)
        lboard.sort(reverse=True)
        print(lboard)
        user_place = "Second"
        print("You placed in {} on the Tetris leaderboard".format(user_place))


player = TetrisScore()
player.playerScore(4400)
player.insertScore(4400)
        
        
