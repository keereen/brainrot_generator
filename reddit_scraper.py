import praw
from reddit_keys import keys

reddit = praw.Reddit(
    client_id = keys["client_id"],
    client_secret = keys["client_secret"],
    user_agent = keys["user_agent"],
    username = keys["username"],
    password = keys["password"]
)

print(reddit)

def top_posts_of_day():
    ''