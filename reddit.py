from redvid import Downloader
import praw
import os
from utils import *

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

def reddit_vid_download(subreddit, timePeriod, upvoteThreshhold):
    for submission in reddit_r.subreddit(subreddit).top(timePeriod):
        if (submission.score > upvoteThreshhold):
            if "v.redd" in submission.url:
                download_vid(submission.url, submission.title)
            if 'clips.t' in submission.url:
                os.system("twitch-dl download -q source " + submission.url)
                move_files()






