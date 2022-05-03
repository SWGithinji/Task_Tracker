# Code compiled by Sam_Githinji

from prettytable import PrettyTable
from datetime import date
import time

extension = '.txt'
current_date = date.today()
current_date_str = str(current_date)
file_name = current_date_str + extension

print('-----------------------------------------------------')
print('      SG Task List Tracker v1.1')
print('-----------------------------------------------------')

user_name = input('Enter Your Name: ')

try:
    file = open(file_name, "r")
except FileNotFoundError:
    file = open(file_name, "x")

print(user_name + "'s Tasks for today")

instructions = '\ni.Add:a to add new Task.' \
               '\nii.List_Check:l to check your Task List.' \
               '\niii.Exit:e to exit the program.'

print(instructions)

my_Task_list = []

x = PrettyTable()


def my_list():
    x.field_names = ["Item Names"]
    for i in my_Task_list:
        x.add_row([i])
    print(x.get_string(title='TO DO LIST'))
    x.clear_rows()


running = True
while running:
    user_input = input('\nWhat do you want to do? (A, L, E): ').lower()

    if user_input == 'a':
        duration = input(str('\nEnter start and end time: '))
        new_Task = input('\nPlease enter your new Task: ').lower()
        newTaskDetails = input('\nInput the Task details: ').lower()
        print(f'\nYour current Task is {new_Task}.')
        my_Task_list.append(new_Task)
        file = open(file_name, "a")
        file.write(f"\n{user_name},\n{duration}, \n{new_Task}, \n{newTaskDetails}")
        file.close()

    elif user_input == 'l':
        my_list()
        file = open(file_name, "r")
        print(file.read())
        file.close()

    elif user_input == 'e':
        ask_user = input(user_name + ', are you sure you want to exit? (Y/N): ').lower()
        if ask_user == 'y':
            running = False

    elif user_input == '' or user_input == ' ':
        print('Please enter something.')

    else:
        print('Enter valid letters!')

print('-----------------------------------------------------')
print('      Sam G Task List Tracker v1.1, 2022')
print('-----------------------------------------------------')


print('You are now exiting the program, Goodbye ' + user_name + '!')

time.sleep(3)