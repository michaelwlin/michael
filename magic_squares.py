"""
***************************************************************************
Filename:      magic_squares.py
Author:        Michael Lin
Date:          2021.02.02
Modifications: Michael Lin - 2021.02.02
Description:   This module takes 16 values from the keyboard and tests whether they form a magic square:
            1) Checks to see if 1-16 is in the user input
            2) Checks if the numbers are put into a square
            3) If the 4 in rows, columns and diagonals are equal to each other 
***************************************************************************
"""
# Establish some variables
numbers_needed = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
user_numbers = [[],[],[],[]]
row = 0
column = 0

# Start the checking process
print("Welcome to the Magic Square Program!")
while True:
    try:
        # If we reach the end then we stop and check the result
        if row == 4:
            break
        # Take user input
        user_in = input("Please enter a value from 1 to 16 to form a Magic Square: ")
        # Convert to int (the exception will catch this if not int)
        temp = int(user_in)
        # Check if valid number 1-16
        if temp in numbers_needed:
            # Check if not already inputed
            if any(temp in sublist for sublist in user_numbers):
                print("You have already added this value!")
            else:
                # Append the number to each row
                # When column hits 3 then we switch rows
                user_numbers[row].append(temp)
                for i in range(len(user_numbers)):
                    print(user_numbers[i])
                column+=1
                if column == 4:
                    row+=1
                    column = 0      
        # If the value is not between 1 to 16
        else:
            print("\n************************************")
            print("Please enter a value from 1 to 16!")
            print("************************************\n")
    # Exception to catch non-integers
    except ValueError:
        print("Please enter a valid integer!")

# Now we can check the result 
# Check the rows & columns first
magic_square = True
temp2 = sum(user_numbers[0])
for i in range(len(user_numbers)):
    temp3 = 0
    temp4 = 0
    for j in range(len(user_numbers[i])):
        # Check rows
        temp3 += user_numbers[i][j]
        # Check columns
        temp4 += user_numbers[j][i]
    if temp3 != temp2 or temp4 != temp2:
        magic_square = False
# Check the diagonals
temp5 = 0
for i in range(len(user_numbers)):
    temp5 += user_numbers[i][i]
if temp5 != temp2:
    magic_square = False
temp6 = 0
loop_temp = len(user_numbers)-1
for i in range(len(user_numbers)):
    temp6 += user_numbers[i][loop_temp]
    loop_temp -= 1
if temp6 != temp2:
    magic_square = False

# Print Result (if True will print successful)
if magic_square:
    print("You have entered a Magic Square! Here it is:")
    print("\n************************************")
    for i in range(len(user_numbers)):
                print(user_numbers[i])
    print("\nA Magic Square!")
    print("************************************")
else:
    print("You have NOT entered a Magic Square.")
    print("Make sure your rows, columns and diagonals equal each other!")
    print("\n************************************")
    for i in range(len(user_numbers)):
                print(user_numbers[i])
    print("\nNot a Magic Square.")
    print("************************************")