import requests

from bs4 import BeautifulSoup

languages = {1: "arabic", 2: "german", 3: "english", 4: "spanish", 5: "french", 6: "hebrew", 7: "japanese",
             8: "dutch", 9: "polish", 10: "portuguese", 11: "romanian", 12: "russian", 13: "turkish"}
your_lang, trans_lang = '', ''


def get_input():
    global languages, your_lang, trans_lang
    your_lang = int(input())
    print("Type the number of a language you want to translate to or '0' to translate to all languages:")
    trans_lang = int(input())

    your_language = dict.setdefault(languages, your_lang)
    translate_language = dict.setdefault(languages, trans_lang)

    if trans_lang == 0:
        languages.pop(your_lang)
        translate_language = "all"

    word = input('Type the word you want to translate:\n')
    return your_language, translate_language, word


def create_url(your_language, translate_language, word):
    url = f'https://context.reverso.net/translation/{your_language}-{translate_language}/{word}'
    return url
