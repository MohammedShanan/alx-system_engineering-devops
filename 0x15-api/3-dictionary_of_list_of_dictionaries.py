#!/usr/bin/python3
"""
Module 3-dictionary_of_list_of_dictionaries.py
Returns information about employee ID TODO list progress in a json file
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users")
    todos_response = requests.get(f"{url}todos")
    users = user_response.json()
    todos = todos_response.json()

    def create_task_list(id, user_name):
        tasks_list = []
        for task in todos:
            if id == task.get("userId"):
                task_dict = {
                    "username": user_name,
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
                tasks_list.append(task_dict)
        return tasks_list

    todo_all_employees = {}
    for user in users:
        id = user.get("id")
        user_name = user.get("username")
        todo_all_employees[id] = create_task_list(id, user_name)
    with open(f"todo_all_employees.json", mode="w", newline="") as file:
        json.dump(todo_all_employees, file)
