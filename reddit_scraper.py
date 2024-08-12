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

def top_posts_from_subreddit(reddit, time_filter_value, post_limit, subreddit_name):
    # time_filter specifies 'top' 'new' 'hot' etc
    # post_limit specifies how many posts to scrape
    # subreddit_name is the subreddit to scrape

    subreddit = reddit.subreddit(subreddit_name)
    subreddit_top = subreddit.top(time_filter = time_filter_value, limit = post_limit)
    print(subreddit_top)
    for post in subreddit_top:
        print(post.selftext)
    # remove stickied posts as an optional toggle

top_posts_from_subreddit(reddit, "day", 10, "AITAH")