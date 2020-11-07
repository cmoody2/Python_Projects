

myString = "I should wear my"

shoe_list = ["Jordan 5s", "Adidas Ozweegos", "Nike LDV Waffles", "Nike Airmax 95s"]

todayString = "today."

for i in shoe_list:
    print(i)

print(shoe_list.sort())

def shoe_function():
    user_choice = input("which shoes should I weare today? ")
    for a in shoe_list:
        msg = "{} {} {}".format(myString,a,todayString)
        if user_choice == a:
            return msg
        else:
            print(" ")
        
print(shoe_function())

print(shoe_list.sort())
