#!/usr/bin/python3
"""Script to export data in the JSON format for a given employee"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": job.get("title"),
                "completed": job.get("completed"),
                "username": u.get("username")
            } for job in requests.get(url + "todos",
                                      params={"userId": u.get("id")}).json()]
        for u in users}, jsonfile)
