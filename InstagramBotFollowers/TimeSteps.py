import time
from random import randint


def time_between_click(min_t=5, max_t=10):
    return time.sleep(randint(min_t, max_t))


def time_between_instruction():
    return time.sleep(randint(2, 6))


def reload_login_section():
    return time.sleep(randint(10, 20))


def time_before_login():
    return time.sleep(randint(10, 20))


def time_after_login():
    return time.sleep(randint(15, 30))


def time_between_follow(min_t=10, max_t=30):
    return time.sleep(randint(min_t, max_t))


def time_between_un_follow(min_t=10, max_t=30):
    return time.sleep(randint(min_t, max_t))


def custom_time_between(min_t=2, max_t=10):
    return time.sleep(randint(min_t, max_t))

