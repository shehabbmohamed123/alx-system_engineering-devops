#!/usr/bin/python3

import praw

def top_ten(subreddit):
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')

    try:
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.hot(limit=10):
            print(submission.title)
    except praw.exceptions.InvalidSubreddit:
        print("None")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
