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



class StateTax:
    def __init__(self):
        self.__saleTax = 7.25

    def getSaleTax(self):
        return self.__saleTax

    def setSaleTax(self, saleTax):
        self.__saleTax = saleTax
        
    def _taxEquation(self):
        go = True
        while go:
            netPrice = input('\nPlease enter price of purchase: ')
            try:
                netPrice = float(netPrice)
                break
            except ValueError:
                print("\nVALUE ERROR: Please enter a number value (ex. 45 or 45.00)")
        tax_amount = netPrice * (self.__saleTax / 100)
        total_amount = netPrice + tax_amount
        return ("\n\nYour total including sales tax is: ${:0.2f}.".format(total_amount))
        


if __name__ == "__main__":
    transact = StateTax()
    print("This is the current CA sales tax: {}%".format(transact.getSaleTax()))
    purchase = transact._taxEquation()
    print(purchase)
    
