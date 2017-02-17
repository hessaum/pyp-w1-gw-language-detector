# -*- coding: utf-8 -*-
#from language_detector.languages import LANGUAGES

def detect_language(text, languages):
    spanish_count = 0
    german_count = 0
    english_count = 0

    for i in range(len(languages)):
        for words in languages[0]['common_words']:
            if words in text:
                spanish_count += 1
        for words in languages[1]['common_words']:
            if words in text:
                german_count += 1
        for words in languages[2]['common_words']:
            if words in text:
                english_count += 1

    if (spanish_count > english_count) and (spanish_count > german_count):
        return 'Spanish'
    if (german_count > english_count) and (german_count > spanish_count):
        return 'German'
    if (english_count > german_count) and (english_count > spanish_count):
        return 'English'