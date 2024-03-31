#!/usr/bin/python3
"""Script that shows completed tasks of an Employee"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    for job in todo:
        if job.get("completed") is True:
            completed = job.get("title")
            print("Employee {} is done with tasks({}/{}):".format(
                user.get("name"), len(completed), len(todo)))

            for task in completed:
                print("\t {}".format(task))
