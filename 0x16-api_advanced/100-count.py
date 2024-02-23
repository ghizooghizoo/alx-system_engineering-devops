#!/usr/bin/python3
"""Task 3 Module"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    returns the count of words in word_list in the titles of all the hot posts
    of the subreddit
    """
    subInfo = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        params={"after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if subInfo.status_code != 200:
        return None

    info = subInfo.json()

    hot = [
        child.get("data").get("title")
        for child in info.get("data").get("children")]
    if not hot:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot:
        words = title.split(' ')
        for word in word_list:
            for sword in words:
                if sword.lower() == word.lower():
                    word_count[word] += 1

    if not info.get("data").get("after"):
        sorted_counts = sorted(
            word_count.items(),
            key=lambda kv: kv[0])
        sorted_counts = sorted(
            word_count.items(),
            key=lambda kv: kv[1], reverse=True)
        [print(f'{i}: {j}') for i, j in sorted_counts if j != 0]
    else:
        return count_words(
            subreddit, word_list, word_count,
            info.get("data").get("after"))
