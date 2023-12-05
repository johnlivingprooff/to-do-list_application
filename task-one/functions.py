#!/usr/bin/python3
"""Contains all the functions for to-do list"""


class Task:
    """Defines a task for the user"""

    task_no = 0
    tasks = {}

    def __init__(self):
        pass

    @classmethod
    def create(cls):
        """Creates a new task"""

        cls.task_no += 1
        task_title = input("Give your task a title:\n").title()
        task_desc = input("Describe your task:\n").lower()

        cls.tasks[Task.task_no] = [task_title, task_desc]

    
    @classmethod
    def update(cls):
        print("Here's all your tasks:")
        for key, value in cls.tasks.items():
            print(f"{key}: {value[0]}")

        task_to_update = int(input("What task would you like to update?\n-> "))
        change = input("Change Title / Description? (type 'title' or 'desc') ").lower()

        if change == "title":
            title = input("What's the new title?\n").title()
            task_items = cls.tasks[task_to_update]
            task_items[0] = title

        if change == "desc":
            desc = input("What's the new description?\n").lower()
            task_items = cls.tasks[task_to_update]
            task_items[1] = desc

    @classmethod
    def remove(cls):
        pass


    @classmethod
    def display(cls):
        """Displays all tasks"""

        for key, value in cls.tasks.items():
            print(f"Task {key}: {value[0]}")
            print(value[1])
            print()
