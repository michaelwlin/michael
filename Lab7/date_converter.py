"""
***************************************************************************
Filename:      date_converter.py
Author:        Michael Lin
Date:          2021.03.23
Modifications: Michael Lin - 2021.03.23
Description:   This module prompts the user for a data input and specifies the required input format to be: mm/dd/yyyy:
            1) Use a regular expression to validate the user input date format.
            2) If the format is incorrect raise a SystemExit. 
***************************************************************************
"""
# List for all the months according to index
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',' November', 'December']

# This function validates the user's date input
def validate_date(user_date):
    try:
        # Split the user input
        date_list = user_date.split("/")
        # Check if the format is 2 digits for month, day, and 4 digits for year
        if len(date_list[0])==2 and len(date_list[1])==2 and len(date_list[2])==4:
            # Put them into variables with validation
            # Check month
            if int(date_list[0]) <= 12 and int(date_list[0]) >= 1:
                month = months_list[int(date_list[0]) - 1]
            else:
                print("Date input error or out of range.")
                raise SystemExit
            # Check day
            if int(date_list[1]) <= 31 and int(date_list[1]) >= 1:
                day = date_list[1]
            else:
                print("Date input error or out of range.")
                raise SystemExit    
            # Check year
            if int(date_list[2]) <= 2999 and int(date_list[2]) >= 1000:
                year = date_list[2]
            else:
                print("Date input error or out of range.")
                raise SystemExit

            # Edge case with February
            if int(date_list[0]) == 2:
                if not(int(year) % 400) or (not(int(year) % 4)) and (int(year) % 100):
                    # Leap Year
                    if int(date_list[1]) > 29:
                        print("Although your input was a Leap Year, the last day of February in a Leap Year is the 29th.")
                        raise SystemExit
                else:
                    if int(date_list[1]) > 28:
                        print("February only has 28 days, unless it is a Leap Year (29 days). " + year + " is not a Leap Year.")
                        raise SystemExit
        else:
            print("Date input error or out of range.")
            raise SystemExit

        final = month + " " + day + ", " + year
        return final


    except ValueError:
        print("Date input error or out of range.")
        raise SystemExit

# Main Function with loop of 5 inputs 
def main():
    counter = 5
    while counter > 0:
        user_date = input("Please enter a date (mm/dd/yyyy): ")
        print("The converted date is: " + validate_date(user_date))
        counter = counter - 1

if __name__ ==  "__main__":
    main()

"""
OUTPUT #1
Please enter a date (mm/dd/yyyy): 01/26/1998
The converted date is: January 26, 1998
Please enter a date (mm/dd/yyyy): 02/29/2020
The converted date is: February 29, 2020
Please enter a date (mm/dd/yyyy): 05/12/2025
The converted date is: May 12, 2025
Please enter a date (mm/dd/yyyy): 12/19/1994
The converted date is: December 19, 1994
Please enter a date (mm/dd/yyyy): 02/30/2020
Although your input was a Leap Year, the last day of February in a Leap Year is the 29th.


OUTPUT #2
Please enter a date (mm/dd/yyyy): 05/24/1922
The converted date is: May 24, 1922
Please enter a date (mm/dd/yyyy): 09/29/2074
The converted date is: September 29, 2074
Please enter a date (mm/dd/yyyy): 10/31/2000
The converted date is: October 31, 2000
Please enter a date (mm/dd/yyyy): 05/25/1874
The converted date is: May 25, 1874
Please enter a date (mm/dd/yyyy): 15/50/3050
Date input error or out of range.

OUTPUT #3
Please enter a date (mm/dd/yyyy): 12/25/2021
The converted date is: December 25, 2021
Please enter a date (mm/dd/yyyy): 07/04/1962
The converted date is: July 04, 1962
Please enter a date (mm/dd/yyyy): 01/22/2092
The converted date is: January 22, 2092
Please enter a date (mm/dd/yyyy): 06/23/1993
The converted date is: June 23, 1993
Please enter a date (mm/dd/yyyy): 02/30/2021
February only has 28 days, unless it is a Leap Year (29 days). 2021 is not a Leap Year.
"""
