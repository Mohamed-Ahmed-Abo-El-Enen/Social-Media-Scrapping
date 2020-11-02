import MultiSocialMediaEngine as MSME
import Utilites as Utl

if __name__ == "__main__":
    pages_url = ["https://www.instagram.com", "https://www.pinterest.com",
                 "https://www.twitter.com"]
    mulScraper = MSME.MultiSocialMediaEngine(pages_url, Utl.DriverType.chrome)

    if mulScraper.check_login_multi_tabs():
        mulScraper.login_multi_tabs()
        mulScraper.post_all_files_in_source_folder()
    print("DONE")