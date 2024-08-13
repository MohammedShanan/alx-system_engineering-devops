#!/usr/bin/python3
"""Recursively retrieves titles of all hot articles for given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieves titles of all hot articles for given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "u/trigun"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        hot_posts = results.get("children")
        for post in hot_posts:
            hot_list.append(post.get("data").get("title"))
    else:
        return None
    after = response.json().get("data").get("after")
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
