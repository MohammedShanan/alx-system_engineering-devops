#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "u/trigun"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        hot_posts = results.get("children")[:10]
        for post in hot_posts:
            print(post.get("data").get("title"))
    else:
        print("None")


top_ten("programming")
