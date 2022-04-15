#!/usr/bin/env python3
#
# Created by: Hertz Antonella
# Created on: Apr 14 2022
# This program ask the user to enter a leap year

def main():
    # Ask the user to enter a year
    user_numb = input("please enter year:")
    try:
        user_int = int(user_numb)

        user_int_4 = user_int % 4
        user_int_100 = user_int % 100
        user_int_400 = user_int % 4400

        if user_int_4 == 0:
            if user_int_100 == 0:
                if user_int_400 == 0:
                    print("{}is a leap year .".format(user_int))
                else:
                    print("{} is not a leap year.".format(user_int))
            else:
                print("{} is a leap year.".format(user_int))
        else:
            print("{} is not a leap year.".format(user_int))

    except Exception:
        print("please enter valid input")


if __name__ == "__main__":
    main()
