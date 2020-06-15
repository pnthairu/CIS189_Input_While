# Start Program
"""
""
Program: input_while.py
Author: Paul Thairu
Last date modified: 06/08/2020

Write a small script, input_while.py that prompts the user for numeric input between 1 and 100.
Prompt the user until the input is in the correct range.
Once a the input is correct, store the input in a list.
"""

List = []
sentinel_value = True

while sentinel_value:
    # get user input
    numbers = int(input("Please enter numbers between 1 and 99 and -99 to exit: "))
    # if user input is bad
    if numbers < 0 or numbers > 99:
        # if its bad
        print("The number you entered is not between 1 and 99")
        break
    # if user input is -99
    elif numbers == -99:
        sentinel_value = False
    else:
        # adding numbers to the list
        List.append(numbers)
for numbers in List:
    # print the list of numbers
    print(List)
    break
# End program
