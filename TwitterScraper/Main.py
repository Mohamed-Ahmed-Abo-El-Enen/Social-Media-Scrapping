import TwitterScraper as twScraper

if __name__ == "__main__":
    tScraper = twScraper.TwitterScraper()
    tScraper.captionEditText = ""

    if tScraper.check_twitter_login():

        tScraper.twitter_login()
        #tScraper.like_reply_re_tweet_on_tweet(100)
        #tScraper.like_first_tweets()
        #tScraper.like_num_tweets(5)
        #tScraper.re_tweet_num_tweets(5)
        #tScraper.follow("TheRock")
        #tScraper.un_follow("TheRock")
        #tScraper.search_keyword()
        tScraper.tweets_all_files_in_source_folder()

        print("DONE")


