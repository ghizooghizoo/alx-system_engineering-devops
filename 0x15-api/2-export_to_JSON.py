#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to json format"""
import json
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

    with open(f"{userId}.json", "w") as f:
        json.dump({userId: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": userName
            } for task in todos]}, f)
