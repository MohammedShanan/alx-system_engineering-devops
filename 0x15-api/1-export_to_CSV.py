#!/usr/bin/python3
"""
Module 1-export_to_CSV.py
Returns information about employee ID TODO list progress in a csv file
"""
import csv
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
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    employee_id,
                    user.get("name"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )
