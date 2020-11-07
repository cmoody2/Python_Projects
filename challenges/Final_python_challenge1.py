import time                                                                      #importing time and math modules
import math

print("Welcome to the Keyboard Preorder list!")                                  
time.sleep(1)
Keyboard_dictionary = {'U80-A' : ('RAMA' , 'TKL' , '480.00'),                    #create dictionary of keyboards with tuple list
                       'Jules' : ('RAMA' , '65%' , '390.00'),
                       'M50-A' : ('RAMA' , 'Ortholinear' , '280.00'),
                       'M60-A' : ('RAMA' , '60%' , '360.00'),
                       'No.1/60' : ('Keycult' , '60%' , '585.00'),
                       'No.1/65' : ('Keycult' , '65%' , '585.00'),
                       'No.2' : ('Keycult' , 'TKL' , '885.00')}
User_name = input("Please type user name:").lower()                              #create user_name variable with provided user input
print('Hello, ' + User_name.capitalize())
time.sleep(1)                                                                    #assign user_name a budget to shop with 
User_budget = float(5000)
User_budget_float = "{:.2f}".format(User_budget)                                 #convert budget into float with two places after decimal, so number can be in dollar.cents format..
print('Alright, your available store credit is: $' + User_budget_float)          #..using string funtion .format          
time.sleep(1)
print("Here is the currently available stock: ")
time.sleep(.5)
print("")
for key in Keyboard_dictionary:                                                  #create loop iterating through keyboard dictionary to list each key and its values
    board_data = Keyboard_dictionary[key]
    print('Name: ' + key);
    print('Manufacturer: ' + board_data[0] + ', Type: ' + board_data[1] + ', Price: $' + board_data[2])
    time.sleep(.5)
    print("")

print("")
def Buy_start():                                                                 #create function that asks if user would like to buy a keyboard with different branches for given answer..                                                                                      
    Buying_decision = input("Would you like to buy a keyboard Yes or NO? ")      #..with start point for "buying" section of code
    if Buying_decision == 'Yes':
        start()
    elif Buying_decision == 'No':
        print("Thanks for visiting!")
        time.sleep(1)
        quit()
    else:
        print("Please enter Yes or No")
        Buy_start()

def start():                                                                    #create function for users choice in which keyboard they would like
    Buying_choice = input("Alright which board would you like? ")
    print(" You choose: " + Buying_choice)
    try:                                                                        #searches keyboard dictionary for key that matches users choice
        choice = Keyboard_dictionary[Buying_choice]
        print('Name: ' + Buying_choice)
        print(Buying_choice + ' is, $' + choice[2])
    except:
        print("Couldn't find keyboard in available stock")
        start()

    sub = User_budget - float(choice[2])                                        #test for -,+,*,/,and % arithmetic functions with given budget and user keyboard choice converted.. 
    sub_conv = "{:.2f}".format(sub)                                             #..into dollar.cents using string funtion .format
    print("You  would be left with: $" + str(sub_conv))
    time.sleep(3)
    add = sub + 10
    add_conv = "{:.2f}".format(add)
    print("Plus a store credit of $10: $" + str(add_conv))
    time.sleep(3)
    multiply = float(choice[2]) * 2
    multiply_conv = "{:.2f}".format(multiply)
    print("You could by 2 " + Buying_choice + " for $" + str(multiply_conv))
    time.sleep(3)
    divide = User_budget / float(choice[2])
    divide_conv = math.floor(divide)                                            #uses prebuilt math function math.floor to return usable cash left if user bought as many boards..
    remainder = User_budget % float(choice[2])                                  #..as possible.             
    remainder_conv = "{:.2f}".format(remainder)
    print('Or if you want gifts for friends you could buy ' + str(divide_conv) + ' ' + Buying_choice + '. With $' + str(remainder_conv) + ' remaining.')
    time.sleep(5)
        
Buy_start()                                                                     #end point for "buying" section of code

x = 0                                                                           #creates variable to work with in while loop for system error message to display 9 times
while x < 10:
    print("System ERROR, too much Keeb...")
    x = x + 1
    time.sleep(.8)

reboot = 9                                                                      #creates variable for system reboot
if not reboot == 10:
    print("")
    print("system reboot...")
    Buy_start()

if x or reboot > 1:                                                             #creates variable for sorry message telling user they are too late
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print("Sorry request timed out, all boards have been purchased, maybe next time :p")
    time.sleep(3)

successful_purchaser_list = ['Jake from State Farm', 'Phillip J. Fry', 'Vin Diesel']             #list of people who bought all the keyboards
for x in successful_purchaser_list:
    print(x + ": Succesful buyer");

    



    
    





        
    



