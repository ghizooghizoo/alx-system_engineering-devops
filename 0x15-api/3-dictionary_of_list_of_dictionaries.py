#!/usr/bin/python3
"""Exports to-do list information of Allll employees to JSON format"""
import json
import requests

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/"
    users = requests.get(baseUrl + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(
                baseUrl + "todos", params={"userId": user.get("id")}).json()]
            for user in users}, f)
