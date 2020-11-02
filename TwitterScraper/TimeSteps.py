import time
from random import randint


def time_between_click():
    return time.sleep(randint(5, 8))


def time_between_alter():
    return time.sleep(randint(10, 15))


def time_between_instruction():
    return time.sleep(randint(2, 5))


def upload_wait_time():
    return time.sleep(randint(5, 10))


def time_before_login():
    return time.sleep(randint(30, 60))


def time_after_login():
    return time.sleep(randint(30, 60))


def time_between_tweets(min_t=60, max_t=120):
    return time.sleep(randint(min_t, max_t))


