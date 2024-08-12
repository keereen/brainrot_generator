import praw
from reddit_keys import keys
from reddit_scraper import Reddit_scraper

reddit_scraper = Reddit_scraper(keys)
posts = reddit_scraper.top_posts_from_subreddit("day", 10, "AITAH")

for post in posts:
    print(post.title)
    print(post.selftext)