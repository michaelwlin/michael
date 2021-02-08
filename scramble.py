"""
***************************************************************************
Filename:      scramble.py
Author:        Michael Lin
Date:          2021.02.02
Modifications: Michael Lin - 2021.02.02
Description:   This module demonstrates a specific type of word scrambling:
            1) Constructs a scrambled version of a given word.  
            2) Randomly flipping two characters other than the first and last one.
***************************************************************************
"""
import random
def scramble(phrase):
    """
    ***************************************************************************
    Function: scramble(string)
    Parameters: string - string to be scrambled
    Outputs: None
    Returns: scrambled string
    Author: Michael Lin
    Date: 2021.02.02
    Modifications: 2021.02.02
    Description:
    This function takes a string argument and scrambles it.
    It's algorithm involves only the inner characters to be scrambled (the first & last character doesn't change).
    The return value is the scrambled string.
    ***************************************************************************
    """
    # Split the given phrase into individual words
    temp = phrase.split()
    # Create the variable we are going to be adding to & returning at the end
    new_phrase = ""
    
    # Start the loop for all of the words ('i' will be each word)
    for i in temp:
        # Create a temporary variable that we are going to scramble
        temp_word = ""
        # Add the first character because we are not changing that
        temp_word += i[0]
        # Check to see if the word is only one character
        if len(i) <= 1:
            # If it is then we add it
            new_phrase += temp_word
        else:
            # Find the inner characters 
            inner = i[1:-1]
            # Add the inner characters in a random fashion
            temp_word += ''.join(random.sample(inner,len(inner)))
            # Add the last character at the end because we aren't changing that
            temp_word += i[len(i)-1]
            new_phrase += temp_word
        new_phrase += " "
    return new_phrase

# User Input (Outside of the function)
user_in = input("Please enter the word or phrase you would like to be scrambled: ")
print("Scrambled! \n")
print(scramble(user_in))
print("\n")


"""
***************************************************************************
Test Cases:
*********
CASE 1:
Please enter the word or phrase you would like to be scrambled: You can't have the cake and eat it too.
Scrambled! 

You c'nat hvae the ckae and eat it too. 

*********
CASE 2:
Please enter the word or phrase you would like to be scrambled: A gentle answer turns away wrath, but a harsh word stirs up anger.
Scrambled! 

A gtlnee awsenr tunrs aawy wtarh, but a hrash word srits up aegnr. 

*********
CASE 3:
Please enter the word or phrase you would like to be scrambled: The love of god does not find, but creates, that which is pleasing to it. The love of man comes into being through that which is pleasing to it. (Martin Luther)
Scrambled! 

The lvoe of god deos not fdin, but cterase, that whcih is plainseg to it. The lvoe of man coems into bnieg torguhh that whcih is pieasnlg to it. (Miartn Lrtueh) 
***************************************************************************
"""