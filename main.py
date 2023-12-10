#!/usr/bin/python3
"""main module contains user's to-do operations"""
from tasks.functions import Task



print("Welcome to To-Do✅")

still_creating = True

while still_creating:
    print("What would you like to do? (choose an option #):")
    start = int(input("1. Create new task\n2. Update existing task\n3. Remove task\n4. Display Tasks\n5. Exit\n-> "))

    if not isinstance(start, int):
        raise TypeError("Input a number")
    
    if start == 1:
        new_task = Task.create()
    elif start == 2:
        Task.update()
    elif start == 3:
        Task.remove()
    elif start == 4:
        Task.display()
    elif start == 5:
        print("Exiting...")
        still_creating = False

    else:
        cont = input("Choose an option from 1 - 5, continue? 'y' or 'n': ").lower()
        if cont == "n":
            still_creating = False

