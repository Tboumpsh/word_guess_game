import random


def load_words(file_path):

    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words


def load_words_by_topic(file_path):
    return load_words(file_path)


def choose_word(words):
    return random.choice(words)
