#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit"""
import requests


def count_words(subreddit, word_list, after=None, count={}):
    """Function to count words in all hot posts of a given Reddit subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "u/trigun"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        hot_posts = results.get("children")
        for post in hot_posts:
            title = post.get("data").get("title").lower()
            for word in word_list:
                word = word.lower()
                count[word] = count.get(word, 0) + title.count(word)
    else:
        return None
    after = response.json().get("data").get("after")
    if not after:
        sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word.lower(), count))
    else:
        return count_words(subreddit, word_list, after, count)
