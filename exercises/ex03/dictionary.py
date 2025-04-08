"""Practicing creating dictionary functions"""

__author__: str = "730655988"


def invert(dictionary: dict[str, str]) -> dict[str, str]:

    inverted_dict: dict[str, str] = {}
    keys = list(dictionary.keys())

    indx = 0
    while indx < len(keys):
        key = keys[indx]
        value = dictionary[key]
        if value in inverted_dict:
            raise KeyError(
                "WARNING duplicate values found in input. Inversion not possible"
            )
        inverted_dict[value] = key
        indx += 1
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}

    indx = 0

    while indx < len(values):
        item = values[indx]

        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
        indx += 1
    return count_dict


def favorite_color(favs: dict[str, str]) -> str:

    color_counts = count(list(favs.values()))

    indx = 0
    popular = ""

    for color in favs.values():
        if color_counts[color] > indx:
            indx = color_counts[color]
            popular = color
    return popular


def bin_len(words: list[str]) -> dict[int, set[str]]:
    length_bins: dict[int, set[str]] = {}

    indx = 0
    while indx < len(words):
        word = words[indx]
        word_length = len(word)

        if word_length not in length_bins:
            length_bins[word_length] = set()

        length_bins[word_length].add(word)

        indx += 1

    return length_bins
