import os
import json
import random

import pandas as pd


def concat_file_to_path(path, file_name):
    return os.path.join(path, file_name)


def get_relative_path():
    return os.path.dirname(os.path.abspath(__file__))


def read_account_info(file_path):
    with open(concat_file_to_path(file_path, r"Assets\settings.json"), 'r') as info_file:
        data = info_file.read()
    if data is None:
        return None
    return json.loads(data)


def is_followed_accounts_file_exist(file_name):
    return os.path.exists(get_relative_path()+"\\"+file_name)


def save_followed_accounts(followed_accounts, file_name):
    followed_accounts.to_csv(get_relative_path() + "\\" + file_name)


def read_followed_accounts_file(file_name):
    return pd.read_csv(get_relative_path()+"\\"+file_name, index_col=0)


def get_random_choice_list(search_list):
    return random.choice(search_list)


def get_random_choice_range(min_num, max_num):
    return random.randint(min_num, max_num)




