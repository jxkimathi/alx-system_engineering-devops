#!/usr/bin/python3
"""Script to export data in the CSV format for a given employee"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = requests.get("username")
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as cvsfile:
        wrtr = csv.writer(cvsfile, quoting=csv.QUOTE_ALL)
        for job in todo:
            wrtr.writerow(
                user_id, username, job.get("completed"), job.get("title"))
