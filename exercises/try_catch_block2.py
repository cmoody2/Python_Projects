

def getName():
    fName = input("\nPlease enter Your first name: ")
    lName = input("\nPlease enter Your last name: ")
    return fName,lName

def welcome_msg():
    go = True
    while go:
        fName,lName = getName()
        try:
            if fName.isalpha():
                go = False
            else:
                continue
        except:
            print("\n\nYou did not enter a valid input")
        finally:
            print("\n\nComputing...")
    print("Hello, {} {}. Welcome to IDLE!".format(fName,lName))


if __name__ == "__main__":
    welcome_msg()
