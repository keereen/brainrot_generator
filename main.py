import praw
import os
import subprocess
from reddit_keys import keys
from reddit_scraper import Reddit_scraper
from tiktokvoice import tts
from control_video import Video_controller

reddit_scraper = Reddit_scraper(keys)
posts = reddit_scraper.top_posts_from_subreddit("day", 1, "AITAH")

for post in posts:
    print(post.title)
    print(post.selftext)

    video_controller = Video_controller(post.title + " " + post.selftext)
    video_controller.make_video()

'''testposts = reddit_scraper.top_posts_from_subreddit("day", 1, "AITAH")
for testpost in testposts:
    tts(testpost.selftext, "en_us_006", "test.mp3")'''

    
