#!/usr/bin/python3
"""
Script that queries subscribers for a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        return int(response.json().get("data").get("subscribers"))
    else:
        return 0
