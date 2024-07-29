#!/usr/bin/python3
"""
Module 2-export_to_JSON.py
Returns information about employee ID TODO list progress in a json file
"""

import json
import requests
import sys

if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{employee_id}")
    todos_response = requests.get(f"{url}todos", params={"userId": employee_id})
    user = user_response.json()
    todos = todos_response.json()
    username = user.get("username")
    tasks_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        tasks_list.append(task_dict)

    with open(f"{employee_id}.json", mode="w", newline="") as file:
        json.dump({str(employee_id): tasks_list}, file)
