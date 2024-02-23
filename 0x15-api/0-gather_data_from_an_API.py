#!/usr/bin/python3
"""fetch to-do list information for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = requests.get(baseUrl + f"users/{sys.argv[1]}").json()
    todos = requests.get(
        baseUrl + "todos", params={"userId": sys.argv[1]}).json()

    completedTasks = []
    for task in todos:
        if task.get("completed") is True:
            completedTasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completedTasks), len(todos)))
    for task in completedTasks:
        print(f"\t {task}")
