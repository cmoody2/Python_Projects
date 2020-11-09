

#-------------------------------------
# Parent class
#-------------------------------------
class Game_console:
    def __init__(self, name, manufacturer, resolution, number_of_controllers):
        self.name = name
        self.manufacturer = manufacturer
        self.resolution = resolution
        self.number_of_controllers = number_of_controllers

    #defining a method for the parent class(i.e. class behavior)
    def power(self):
        sys_power = True
        power_button = input("Enter 'ON' to turn system on or 'OFF' to turn it off: ").upper()
        while sys_power:
            if power_button == 'ON':
                print("\n\nSystem powering on!")
                sys_power = False
            elif power_button == 'OFF':
                print("\n\nSystem powering off")
                sys_power = False
            else:
                print("Please enter 'ON' or 'OFF'")
                Game_console.power(self)


#-------------------------------------
# Child class 1
#-------------------------------------
class Nintendo_switch(Game_console):
    def __init__(self, name, manufacturer, resolution, number_of_controllers, console_mode, handheld_resolution):
        # Using super() method we can have the child class inherit the parents attributes
        super().__init__(name, manufacturer, resolution, number_of_controllers)
        # Adding two additional attributes specific to this child class
        self.console_mode = console_mode
        self.handheld_resolution = handheld_resolution

    #Using polymorphism we create a method similar to parent method but we print the childs name attribute
    #when powering on and off instead of generic 'system' for parent method
    def power(self):
        sys_power = True
        power_button = input("Enter 'ON' to turn system on or 'OFF' to turn it off: ").upper()
        while sys_power:
            if power_button == 'ON':
                print("\n\n{} powering on!".format(self.name))
                sys_power = False
            elif power_button == 'OFF':
                print("\n\n{} powering off!".format(self.name))
                sys_power = False
            else:
                print("Please enter 'ON' or 'OFF'")
                Nintendo_switch.power(self)


#-------------------------------------          
# Child class 2
#-------------------------------------
class Playstation_5(Game_console):
    def __init__(self, name, manufacturer, resolution, number_of_controllers, video_connection, online_subscription):
        # Using super() method we can have the child class inherit the parents attributes
        super().__init__(name, manufacturer, resolution, number_of_controllers)
        # Adding two additional attributes specific to this child class
        self.video_connection = video_connection
        self.online_subscription = online_subscription

    #Using polymorphism we create a method similar to parent method but we print the childs name attribute
    #when powering on and off instead of generic 'system' for parent method
    def power(self):
        sys_power = True
        power_button = input("\nEnter 'ON' to turn system on or 'OFF' to turn it off: ").upper()
        while sys_power:
            if power_button == 'ON':
                print("\n\n{} powering on!".format(self.name))
                sys_power = False
            elif power_button == 'OFF':
                print("\n\n{} powering off!".format(self.name))
                sys_power = False
            else:
                print("Please enter 'ON' or 'OFF'")
                Playstation_5.power(self)
                



if __name__ == "__main__":
    f1 = Playstation_5("Playstation 5 Pro", "Sony", "4K", "1", "HDMI 2.1", "No Subscription Provided")
    print("\n{}".format(f1.name))
    f1.power()
