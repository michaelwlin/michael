"""
***************************************************************************
Filename:      exception_handling.py
Author:        Michael Lin
Date:          2021.02.21
Modifications: Michael Lin - 2021.02.21
Description:   This module asks the user to input a set of floating-point values:
            1) When the value is not a number, it gives the user a second chance to enter the value.
            2) After two chances, it will quit reading input
            3) Adds all correctly specified values 
***************************************************************************
"""
tries = 2
counter = 0

print("This program will only take floating-point values and add them up! You have 2 tries.\n")
while True:
    if tries == 0:
        print("You are out of tries!")
        break
    try:
        user_input = input("Please enter a floating-point value: ")
        counter += float(user_input)
    except ValueError:
        tries -= 1
        print("Number of tries left: " + str(tries))
print("The total amount you entered is: " + str(counter))

"""
TEST CASE #1
This program will only take floating-point values and add them up! You have 2 tries.

Please enter a floating-point value: asdf
Number of tries left: 1
Please enter a floating-point value: 5.5
Please enter a floating-point value: 1002
Please enter a floating-point value: 7.295
Please enter a floating-point value: haha
Number of tries left: 0
You are out of tries!
The total amount you entered is: 1014.795

TEST CASE #2
This program will only take floating-point values and add them up! You have 2 tries.

Please enter a floating-point value: asdf
Number of tries left: 1
Please enter a floating-point value: asdf
Number of tries left: 0
You are out of tries!
The total amount you entered is: 0

TEST CASE #3
This program will only take floating-point values and add them up! You have 2 tries.

Please enter a floating-point value: 5
Please enter a floating-point value: 9.2
Please enter a floating-point value: 1104515.3
Please enter a floating-point value: im
Number of tries left: 1
Please enter a floating-point value: done
Number of tries left: 0
You are out of tries!
The total amount you entered is: 1104529.5

"""
