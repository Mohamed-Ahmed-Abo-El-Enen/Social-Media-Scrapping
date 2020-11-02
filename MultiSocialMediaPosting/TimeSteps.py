import time
from random import randint


def time_between_click():
    return time.sleep(randint(5, 10))


def time_between_instruction():
    return time.sleep(randint(4, 8))


def reload_login_section():
    return time.sleep(randint(10, 20))


def upload_wait_time():
    return time.sleep(randint(5, 10))


def time_before_login():
    return time.sleep(randint(10, 20))


def time_after_login():
    return time.sleep(randint(10, 20))


def time_between_posts(min_t=15, max_t=30):
    return time.sleep(randint(min_t, max_t))


def time_between_follow(min_t=10, max_t=30):
    return time.sleep(randint(min_t, max_t))


def time_between_un_follow(min_t=10, max_t=30):
    return time.sleep(randint(min_t, max_t))


def time_between_profile_load():
    return time.sleep(randint(10, 15))


def wait_time_between(min_val=5, max_val=10):
    return time.sleep(randint(min_val, max_val))
