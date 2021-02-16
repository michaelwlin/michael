# CIS 41A Lab - 2 Factoring of Integers
# Description: Asks user for an integer then prints out all of its factors
# By Michael Lin

# While loop to ensure the user inputs a valid number
while True:
    try:
        # Take user input then convert it to integer 
        # It will have a ValueError error if not a valid number & the except will catch that
        user_in = input("Please enter an integer to be shown all of its factors: ")
        temp = int(user_in)

        # Begin our initial output
        print("All factors for %d:" %(temp))
        # Followed by our loop that will output any factor of the given parameter
        for i in range(2,temp,1): # Essentially the modulus will divide by the increment from 2 to the parameter
            if temp%i == 0: # If there is no remainder then that means it is a factor
                print(i)
        break

    # This will catch the ValueError if the user does not input the specified type  
    except ValueError:
        print("Please enter a valid integer!")


"""
The following is the record of program execution and outputs:

All factors for 77:
7
11

All factors for 78:
2
3
6
13
26
39

All factors for 79:

All factors for 12345:
3
5
15
823
2469
4115

All factors for 123456:
2
3
4
6
8
12
16
24
32
48
64
96
192
643
1286
1929
2572
3858
5144
7716
10288
15432
20576
30864
41152
61728

All factors for 111111111:
3
9
37
111
333
333667
1001001
3003003
12345679
37037037
""" 