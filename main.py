#!/usr/bin/env python3

# Script to find out available usernames on github
# - using dictionary words
# - using dynamically generated pronounceable words

# Author: Ashish Ranjan (https://github.com/musq)
# License: GNU GPLv3, or later version


from nltk.corpus import words
from pronounceable import PronounceableWord, Pronounceablity
import requests
from time import sleep


GITHUB_HOME = 'https://github.com/'
GITHUB_AVAILABLE_USERNAMES_FILE = 'github-available-usernames'
GITHUB_REQUESTS_FILE = 'github-all-username-requests'

MAX_DESIRED_RESULTS = 500
SLEEP_INTERVAL = 0.2
USERNAME_MAX_LENGTH = 5
USERNAME_MAX_SYLLABLE_COUNT = 2


open(GITHUB_AVAILABLE_USERNAMES_FILE, 'a').close()
open(GITHUB_REQUESTS_FILE, 'a').close()


def find_dictionary_words():
    words_list = list(set(
        [ w.lower() for w in words.words() \
            if len(w) == USERNAME_MAX_LENGTH ]
    ))
    words_list.sort()

    for username in words_list:
        if log_github_requests(username) \
            and github_availability(username):

            print(username)
            store_available_username(username)
            sleep(SLEEP_INTERVAL)


def find_pronounceable_words():
    pr = Pronounceablity()

    for x in range(0, MAX_DESIRED_RESULTS):
        available = False

        while (not available):
            username = PronounceableWord().length(
                USERNAME_MAX_LENGTH,
                USERNAME_MAX_LENGTH+1
            )
            syllable_count = pr.syllable(username)

            if (syllable_count <= USERNAME_MAX_SYLLABLE_COUNT) \
                and log_github_requests(username):

                available = github_availability(username)
                sleep(SLEEP_INTERVAL)

        print(username)
        store_available_username(username)


def github_availability(username):
    try:
        github_profile_url = GITHUB_HOME + username

        r = requests.get(github_profile_url)

        if (r.status_code == 404):
            return True
    except Exception as err:
        print('\nError occured during pinging Github')
        print(err, '\n')

    return False


def log_github_requests(username):
    with open(GITHUB_REQUESTS_FILE, 'r') as file:
        for row in file:
            if (username == row.rstrip()):
                return False

    with open(GITHUB_REQUESTS_FILE, 'a') as file:
        file.write(username + '\n')

    return True


def main():
    find_dictionary_words()
    # find_pronounceable_words()


def store_available_username(username):
    with open(GITHUB_AVAILABLE_USERNAMES_FILE, 'a') as file:
        file.write(username + '\n')


if __name__ == "__main__":
    main()
