#!/usr/bin/python3
"""Getting the NO of Subscribers"""
import requests


def number_of_subscribers(subreddit):
    """func that get the NO of Subscribers"""

    subInfo = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    # In case of redirectio or server and client erorr
    if subInfo.status_code >= 300:
        return 0

    return subInfo.json().get("data").get("subscribers")
