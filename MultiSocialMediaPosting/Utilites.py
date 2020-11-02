import os
import random
import shutil
from os import listdir
from os.path import isfile, join
import Exceptions as Ex
import json
import emojiModel
import autoit
import enum


class DriverType(enum.Enum):
    chrome = 1,
    firefox = 2


def concat_file_to_path(path, file_name):
    return os.path.join(path, file_name)


def read_account_info(file_path):
    with open(concat_file_to_path(file_path, r"Assets\settings.json"), 'r') as info_file:
        data = info_file.read()
    if data is None:
        return None
    return json.loads(data)


def get_relative_path():
    return os.path.dirname(os.path.abspath(__file__))


def list_directory_file(path=concat_file_to_path(get_relative_path(), "Source Directory"), ext=".jpg"):
    try:
        files_list = [concat_file_to_path(path, file) for file in listdir(path) if isfile(join(path, file))
                      and (ext in file)]
        return files_list
    except Exception as e:
        Ex.print_exception(e)


def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (
                child.name,
                next(i for i, s in enumerate(siblings, 1) if s is child)
                )
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


def get_list_keywords(content_list):
    try:
        content = [x.strip() for x in content_list]
        return content
    except Exception as e:
        Ex.print_exception(e)


def move_file(source_file_path, dest=concat_file_to_path(get_relative_path(), "Destination Directory")):
    try:
        shutil.move(source_file_path, dest)
    except Exception as e:
        Ex.print_exception(e)


def get_twitter_user_name(url):
    url_seg = str(url).split('/')
    return '/' + url_seg[3]


def get_random_keyword_file(content_list):
    content = get_list_keywords(content_list)
    return random.choice(content)


def get_random_emoji_text(content_list=None, times=3):
    content = emojiModel.get_emoji_list(times) + get_list_keywords(content_list)
    return random.choice(content)


def firefox_upload_file(file_path):
    try:
        handle = "[CLASS:#32770; TITLE:File Upload]"
        autoit.win_wait(handle, 60)
        autoit.control_set_text(handle, "Edit1", file_path)
        autoit.control_click(handle, "Button1")
    except Exception as e:
        Ex.print_exception(e)


def chrome_upload_file(file_path):
    try:
        handle = "[CLASS:#32770; TITLE:Open]"
        autoit.win_wait(handle, 60)
        autoit.control_set_text(handle, "Edit1", file_path)
        autoit.control_click(handle, "Button1")
    except Exception as e:
        Ex.print_exception(e)

