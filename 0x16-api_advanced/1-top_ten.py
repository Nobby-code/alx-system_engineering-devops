#!/usr/bin/python3
"""Reddit API queries"""

import requests


def top_ten(subreddit):
    """returns top 10 posts"""
    header = {"User-Agent": "Google Chrome"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        for i in r.json().get("data", None).get("children", None):
            print(i.get("data", None).get("title", None))
    else:
        print(None)

if __name__ == "__main__":
    pass
