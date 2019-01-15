#!/usr/bin/env python
#
# get_related.py
#
# 2019/1/12

import wikipedia


def get_inno(word):
    try:
        wiki_page = wikipedia.page(word)
    except wikipedia.PageError:
        print("No name %s as a page." % word)
        return []

    word_list = []
    for l in wiki_page.links:
        word_list.append(str(l))

    return word_list


if __name__ == '__main__':
    word = input("Keyword >>> ")
    print(get_inno(word))
