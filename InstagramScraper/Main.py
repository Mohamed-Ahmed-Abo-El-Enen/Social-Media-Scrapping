import InstagramScraper as instScraper

if __name__ == "__main__":
    inScraper = instScraper.InstagramScraper()
    inScraper.captionEditText = ""
    if inScraper.check_instagram_login():
        #inScraper.instagram_login()
        #inScraper.post_all_files_in_source_folder()
        #followed_account = inScraper.like_follow_in_search_explore(2)
        #inScraper.un_follow_in_list(followed_account)
        #inScraper.like_reply_on_following_post(100)
        #inScraper.get_last_added_to_url(end_url)
        print("DONE")