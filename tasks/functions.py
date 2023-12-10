#!/usr/bin/python3
"""Contains all the functions for to-do list"""
import json


class Task:
    """Defines a task for the user"""

    task_no = 0
    __tasks = {}
    __file_path = "todo.json"

    def __init__(self):
        pass

    @classmethod
    def create(cls):
        """Creates a new task"""

        cls.task_no += 1
        task_title = input("Give your task a title:\n").title()
        task_desc = input("Describe your task:\n").lower()

        cls.__tasks[Task.task_no] = [task_title, task_desc]

        cls.save()
    
    @classmethod
    def update(cls):

        cls.reload()
        print("Here's all your tasks:")
        for key, value in cls.__tasks.items():
            print(f"{key}: {value[0]}")

        task_to_update = int(input("What task would you like to update?\n-> "))
        change = input("Change Title / Description? (type 'title' or 'desc') ").lower()

        if change == "title":
            title = input("What's the new title?\n").title()
            cls.__tasks[task_to_update][0] = title

        if change == "desc":
            desc = input("What's the new description?\n").lower()
            cls.__tasks[task_to_update][1] = desc

        cls.save()

    @classmethod
    def remove(cls):
        cls.reload()
        print("Here's all your tasks:")
        for key, value in cls.__tasks.items():
            print(f"{key}: {value[0]}")

        task_to_remove = str(input("What task would you like to remove?\n-> "))
        confirm = input(f"Are you sure you want to delete Task {task_to_remove}? [y/N]\n").lower()

        if confirm == "y":
            del cls.__tasks[task_to_remove]
            print(f"Task {task_to_remove} deleted successfully.")
        else:
            print("Removal cancelled")

        cls.save()


    @classmethod
    def display(cls):
        """Displays all tasks"""
        cls.reload()
        for key, value in cls.__tasks.items():
            print(f"Task {key}: {value[0]}")
            print(value[1])
            print()
    
    @classmethod
    def to_dict(cls):
        """returns a dict repr of todo list"""
        todo_dict = cls.__tasks.copy()
        return todo_dict

    @classmethod
    def save(cls):
        """serialisation of data"""
        temp_dict = {}
        for k, v in cls.__tasks.items():
            temp_dict[k] = v
        with open(cls.__file_path, 'w', encoding='utf-8') as todo:
            json.dump(temp_dict, todo)

    @classmethod
    def reload(cls):
        """Deserialisation"""
        try:
            with open(cls.__file_path, 'r', encoding='utf-8') as todo:
                todo_obj = json.load(todo)
                for k, v in todo_obj.items():
                    cls.__tasks[k] = v        
        except FileNotFoundError:
            pass