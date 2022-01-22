from redvid import Downloader
import praw
import requests
import requests.auth
import os

reddit_r = praw.Reddit(
    client_id="QMvKrQrYrkBXEJGRpxi1nQ",
    client_secret="gcCtf4u7OZd7hzCiPZjvjjD5wzBmKA",
    user_agent="clipdownload",
)

def download_vid(url, name):
    reddit = Downloader(max_q=True)
    reddit.path = 'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\videos'
    reddit.url = url
    reddit.download()
    print(name)
    while not(name[-1:].isalnum()):
        name = name[:-1]
        print(name)
    os.rename(reddit.file_name, 'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\videos\\' + name +'.mp4')

for submission in reddit_r.subreddit("leagueoflegends").top("week"):
    if (submission.score > 10000):
        if "v.redd" in submission.url:
            download_vid(submission.url, submission.title)
            







