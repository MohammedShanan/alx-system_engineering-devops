#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API.py
Returns information about employee ID _TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{employee_id}")
    todos_response = requests.get(
        f"{url}todos", params={"userId": employee_id}
        )
    user = user_response.json()
    todos = todos_response.json()
    completed_tasks = list(filter(lambda x: x.get("completed"), todos))
    print(
        f"Employee {user.get('name')} is done with tasks"
        f"({len(completed_tasks)}/{len(todos)}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
