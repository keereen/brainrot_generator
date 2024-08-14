import praw
import os
import subprocess
from reddit_keys import keys
from reddit_scraper import Reddit_scraper
from tiktok_keys import sessionid
from tiktokvoice import tts

reddit_scraper = Reddit_scraper(keys)
posts = reddit_scraper.top_posts_from_subreddit("day", 10, "AITAH")

'''for post in posts:
    print(post.title)
    print(post.selftext)'''

testposts = reddit_scraper.top_posts_from_subreddit("day", 1, "AITAH")
for testpost in testposts:
    tts(testpost.selftext, "en_us_006", "test.mp3")