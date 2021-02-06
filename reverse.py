"""
***************************************************************************
Filename:      reverse.py
Author:        Michael Lin
Date:          2021.02.02
Modifications: Michael Lin - 2021.02.02
Description:   This module computes the reverse of a string recursively:
            1) The recursive call passes in a spliced portion of the word starting from the second character 
            2) Until the base case is reached (empty string is passed)
            3) Then it starts to call the return stack and adds the last character passed in (LIFO)
***************************************************************************
"""

def reverse(word):
    """
    ***************************************************************************
    Function: reverse(string)
    Parameters: string - string to be reversed
    Outputs: None
    Returns: reversed string
    Author: Michael Lin
    Date: 2021.02.02
    Modifications: 2021.02.02
    Description:
    This function takes a string argument and reverse it.
    It's algorithm involves recursive calls of the function itself.
    The return value is the reversed string.
    ***************************************************************************
    """
    # Our base case is when there is when we reach the end of the word (no more to be reversed)
    # This will be reached since every time we are recursively calling the method we are passing in a spliced section of the word
    if word == "":
        return word
    else:
        # Keeps calling the function until the base case is reached, then we start to add the given 0th characters of each call
        # ie: "f l o w" will be given in every recursive call (word[0]), but it be added as "w o l f" in the return stack
        return reverse(word[1:]) + word[0]  
# User Input (Outside of the function)
user_in = input("Please enter the word or phrase you would like to be reversed: ")
print("Reversed! \n")
print(reverse(user_in))
print("\n")

"""
***************************************************************************
Test Cases:
*********
Case 1:
Please enter the word or phrase you would like to be reversed: pineapple
Reversed! 

elppaenip

*********
Case 2:
Please enter the word or phrase you would like to be reversed: cherimoya
Reversed! 

ayomirehc

*********
Case 3:
Please enter the word or phrase you would like to be reversed: america
Reversed! 

acirema

*********
Case 4:
Please enter the word or phrase you would like to be reversed: level
Reversed! 

level
***************************************************************************
"""

