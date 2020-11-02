import random
import emoji


def thumbs_up():
    return emoji.emojize(":thumbs_up:", use_aliases=True)


def ok_hand():
    return emoji.emojize(":ok_hand:", use_aliases=True)


def open_mouth():
    return emoji.emojize(":open_mouth:", use_aliases=True)


list_emoji = [thumbs_up(),
              ok_hand(),
              open_mouth()]


def get_emoji_list(item_repeated):
    return [emoji_elm * item_repeated for emoji_elm in list_emoji]


def get_repeated_emoji(times):
    return random.choice(list_emoji) * times

