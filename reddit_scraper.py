import praw

class Reddit_scraper:
    def __init__(self, keys):
        self.reddit = praw.Reddit(
            client_id = keys["client_id"],
            client_secret = keys["client_secret"],
            user_agent = keys["user_agent"],
            username = keys["username"],
            password = keys["password"]
        )
        print(self.reddit)

    def top_posts_from_subreddit(self, time_filter_value, post_limit, subreddit_name):
        # time_filter specifies 'top' 'new' 'hot' etc
        # post_limit specifies how many posts to scrape
        # subreddit_name is the subreddit to scrape

        subreddit = self.reddit.subreddit(subreddit_name)
        subreddit_top = subreddit.top(time_filter = time_filter_value, limit = post_limit)
        
        # remove stickied posts as an optional toggle

        print(subreddit_top)

        return subreddit_top
        '''for post in subreddit_top:
            print(post.selftext)'''
        

