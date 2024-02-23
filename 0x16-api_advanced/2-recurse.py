#!/usr/bin/python3
"""Task 2 Mosule"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """func that get Hot posts"""

    subInfo = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        params={"count": count, "after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if subInfo.status_code >= 300:
        return None

    hot = hot_list + [
        info.get("data").get("title")
        for info in subInfo.json()
            .get("data")
            .get("children")]

    info = subInfo.json()
    if not info.get("data").get("after"):
        return hot

    return recurse(
        subreddit,
        hot,
        info.get("data").get("count"),
        info.get("data").get("after"))
