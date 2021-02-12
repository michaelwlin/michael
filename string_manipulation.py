"""
***************************************************************************
Filename:      string_manipulation.py
Author:        Michael Lin
Date:          2021.02.11
Modifications: Michael Lin - 2021.02.11
Description:   This module asks a user to type in two strings and that prints:
            1) the characters that occur in both strings
            2) the characters that occur in one string but not the other
            3) the letters that don’t occur in either string
***************************************************************************
"""
# Establish alphabet
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Start io
print("Welcome to the String Manipulator!")
print("This application takes two strings and identifies:")
print("1. Characters that occur in both strings")
print("2. Characters that occur in one string but not the other")
print("3. Letters that do not occur in either string")

# Begin checking
str1 = input("Please enter the first string: ")
str2 = input("Please enter the second string: ")

both = ""
first_unique = ""
second_unique = ""
none = ""

# Check
# For all cases we don't want to include 
for char in str1:
    # Check if each char in str1 is in the str2
    # Also if we haven't already added it to the final result
    if char in str2 and char not in both:
        both += ("'" + char + "', ")
    
    # Check if each char in str1 is not in str2
    if char not in str2 and char not in first_unique:
        first_unique += ("'" + char + "', ")

# Check if each char in str2 is not in str1
for char in str2:
    if char not in str1 and char not in second_unique:
        second_unique += ("'" + char + "', ")

# Check if any characters are not used from the alphabet
for char in letters:
    if char not in str1 and char not in str2:
        none += ("'" + char + "', ")

print("\nCharacters in both strings:",  both)
print("\nCharacters only in the FIRST string & not in the SECOND string:",  first_unique)
print("\nCharacters only in the SECOND string & not in the FIRST string:", second_unique)
print("\nCharacters from the Alphabet that are NOT used in any of the two strings:", none)

"""
******************************************************
TEST CASE #1:
1. You can't have the cake and eat it too.
2. A gentle answer turns away wrath, but a harsh word stirs up anger.
******************************************************

Welcome to the String Manipulator!
This application takes two strings and identifies:
1. Characters that occur in both strings
2. Characters that occur in one string but not the other
3. Letters that do not occur in either string
Please enter the first string: You can't have the cake and eat it too.
Please enter the second string: A gentle answer turns away wrath, but a harsh word stirs up anger.

Characters in both strings: 'o', 'u', 'a', 'n', 't', 'h', 'e', 'd', 'i', '.', 

Characters only in the FIRST string & not in the SECOND string: 'Y', 'c', 'v', 'k', 

Characters only in the SECOND string & not in the FIRST string: 'A', 'g', 'l', 's', 'w', 'r', 'y', 'b', 'p', 

Characters from the Alphabet that are NOT used in any of the two strings: 'f', 'j', 'm', 'q', 'x', 'z', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z', 

******************************************************
TEST CASE #2:
1. The love of god does not find, but creates, that which is pleasing to it. The love of man comes into being through that which is pleasing to it. (Martin Luther)
2. You can't have the cake and eat it too.
******************************************************

Welcome to the String Manipulator!
This application takes two strings and identifies:
1. Characters that occur in both strings
2. Characters that occur in one string but not the other
3. Letters that do not occur in either string
Please enter the first string: The love of god does not find, but creates, that which is pleasing to it. The love of man comes into being through that which is pleasing to it. (Martin Luther)
Please enter the second string: You can't have the cake and eat it too.

Characters in both strings: 'h', 'e', 'o', 'v', 'd', 'n', 't', 'i', 'u', 'c', 'a', '.', 

Characters only in the FIRST string & not in the SECOND string: 'T', 'l', 'f', 'g', 's', 'b', 'r', 'w', 'p', 'm', '(', 'M', 'L', ')', 

Characters only in the SECOND string & not in the FIRST string: 'Y', 'k', 

Characters from the Alphabet that are NOT used in any of the two strings: 'j', 'q', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Z', 

"""