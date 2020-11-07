date = ("9/11/2020")
print("Today " + date + " we will be observing two of my favorite keyboard designs and finding out if I can afford them!")
RAMA = ("RAMA U80-A")               #Here we define variables needed
RAMA_Price = 480
TGR = ("TGR Jane V2 CE")
TGR_Price = 550
My_Wallet = 880
print("")
print("Our first board is the " + RAMA + " at $" + str(RAMA_Price) + ".")       #listing both boards and prices converting the int..
print("Our second board is the " + TGR + " at $" + str(TGR_Price) + ".")        #... Price to str for concatenation.
print("And our budget is $880 available to spend.")
if TGR_Price + RAMA_Price <= My_Wallet:                                         #expression to find if both boards can be purchased
    print("I can buy both boards so I shall!")
if TGR_Price + RAMA_Price > My_Wallet:
    print("I can't afford both boards!")
print("")
if TGR_Price + RAMA_Price > My_Wallet and TGR_Price < My_Wallet:                #expression to find if either can be purchased standalone
    print("I can afford to buy the " + TGR + " by itself.")
if TGR_Price + RAMA_Price > My_Wallet and RAMA_Price < My_Wallet:
    print("I can afford to buy the " + RAMA + " by itself.")
if TGR_Price + RAMA_Price > My_Wallet and TGR_Price < My_Wallet and RAMA_Price < My_Wallet:
    print("Decisions, Decisions...")
if TGR_Price + RAMA_Price > My_Wallet and TGR_Price < My_Wallet:                #decision to purchase provided it fits in given budget
    print("" + TGR + " will be the one I'll go with!")
