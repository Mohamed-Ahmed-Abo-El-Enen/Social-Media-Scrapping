import InstagramScraper as instScraper
import TimeSteps
import Utilites as Utl

if __name__ == "__main__":
    search_word_list = ["therock"]

    inScraper = instScraper.InstagramScraper()
    if inScraper.check_instagram_login():
        inScraper.instagram_login()
        num_iter = Utl.get_random_choice_range(2, 6)
        inScraper.reset_followed_last_round()
        itr = 0
        while itr < num_iter:
            search_word = Utl.get_random_choice_list(search_word_list)
            inScraper.search_for(search_word)
            TimeSteps.time_between_click()
            inScraper.get_account_followers(search_word, Utl.get_random_choice_range(10, 20))
            TimeSteps.time_between_un_follow(900, 1200)
            inScraper.un_follow_account_file()
            itr += 1
            print("DONE: "+str(itr))
            TimeSteps.time_between_follow(900, 1200)

        inScraper.__exit__()
        print("ALL IS DONE SUCCESSFULLY")
