#Start Program
"""
""
Program: input_while.py
Author: Paul Thairu
Last date modified: 06/08/2020

Write a small script, input_while.py that prompts the user for numeric input between 1 and 100.
Prompt the user until the input is in the correct range.
Once a the input is correct, store the input in a list.
"""

list = []
sentinel_value = True

while (sentinel_value):
    numbers = int(input("Please enter numbers between 1 and 99 and -99 to exit: "))
    if numbers < 0 or numbers > 99:
        sentinel_value = False
    for numbers in list:
        list.append(numbers)
        print(list)




