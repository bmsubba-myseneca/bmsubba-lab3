#!/usr/bin/env python3

# Author ID: bmsubba

# List to be used by the functions
my_list = [100, 200, 300, 'six hundred']

# Function to return the whole list
def give_list():
    return my_list

# Function to return the first item in the list as a string
def give_first_item():
    return str(my_list[0])

# Function to return a list containing the first and last items
def give_first_and_last_item():
    return [my_list[0], my_list[-1]]

# Function to return a list containing the second and third items
def give_second_and_third_item():
    return [my_list[1], my_list[2]]

# Main Program (Optional, based on how you want to run the script)
if __name__ == '__main__':
    print("Whole List:", give_list())
    print("First Item:", give_first_item())
    print("First and Last Items:", give_first_and_last_item())
    print("Second and Third Items:", give_second_and_third_item())
