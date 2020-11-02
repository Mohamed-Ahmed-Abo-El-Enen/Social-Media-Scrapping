import random
import emoji


def kissing_heart():
    return emoji.emojize(":kissing_heart:", use_aliases=True)


def kissing():
    return emoji.emojize(":kissing:", use_aliases=True)


def kissing_closed_eyes():
    return emoji.emojize(":kissing_closed_eyes:", use_aliases=True)


def kissing_smiling_eyes():
    return emoji.emojize(":kissing_smiling_eyes:", use_aliases=True)


def heart_eyes():
    return emoji.emojize(":heart_eyes:", use_aliases=True)


def heartbeat():
    return emoji.emojize(":heartbeat:", use_aliases=True)


def star2():
    return emoji.emojize(":star2:", use_aliases=True)


def star():
    return emoji.emojize(":star:", use_aliases=True)


def hot_pepper():
    return emoji.emojize(":hot_pepper:", use_aliases=True)


def fire():
    return emoji.emojize(":fire:", use_aliases=True)


def thumbs_up():
    return emoji.emojize(":thumbs_up:", use_aliases=True)


def heart():
    return emoji.emojize(":heart:", use_aliases=True)


def ok_hand():
    return emoji.emojize(":ok_hand:", use_aliases=True)


def open_mouth():
    return emoji.emojize(":open_mouth:", use_aliases=True)


list_emoji = [kissing_heart(),
              kissing(),
              kissing_closed_eyes(),
              kissing_smiling_eyes(),
              heart_eyes(),
              heartbeat(),
              star(),
              star2(),
              hot_pepper(),
              fire(),
              thumbs_up(),
              ok_hand(),
              open_mouth()]


def get_emoji_list(item_repeated):
    repeated_list = [emoji_elm * item_repeated for emoji_elm in list_emoji]
    composite_list = random.sample(list_emoji, random.randrange(1, 6, 1))
    return repeated_list + composite_list


def get_repeated_emoji(times):
    return random.choice(list_emoji) * times

