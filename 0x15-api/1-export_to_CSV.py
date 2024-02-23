#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        baseUrl + "users/{}".format(userId)).json()
    userName = user.get("username")
    todos = requests.get(
        baseUrl + "todos", params={"userId": userId}).json()

    with open(f"{userId}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [userId, userName, task.get("completed"), task.get("title")])
