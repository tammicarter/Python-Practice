'''
Build the engine for a car
using while loops/ if / else and elif 
Mosh reference
'''
print(' Please Type "help" to get the keys to run the engine of this car: ')
# set an empty var
command = " " 
# add Booloeans to see if the car is strated or stopped already
started = False
# setting condition
while True:
# user input gets stored using "> " in the command var - call the lower method on the input function here to eliminate dry coding 
# to assure case translates to all lower case   
    command = input("> ").lower()
    if command == "start":
        if started:
            print ("The car is already started!")
        else:
            started = True    
            print ("Car Started...")
    elif command == 'stop':
# using the not operator
        if not started:
            print("The car is already stopped!")
        else:
            started = False    
            print("Car Stopped. ")   
    elif command  == "help":
       print(""" 
Enter
start - to start the car
stop - to stop the car
quit - to exit
        """) 
# the below elif command allows you to jump out the program using break         
    elif command == "quit":
        break  
    else:
        print("Sorry, I dont understand that")  


