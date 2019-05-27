# Github available usernames

Find out available usernames in Github.

It works by iterating over a list of words which fit the specified parameters and pinging Github to check if the profile page of these words (usernames) exist. If it does not exist, this word is stored as an available username.

### Requirements

- python 3.6+
- pipenv

### Installation

1. Clone this repository and `cd` into it
1. Create a virtualenv using `python3 -m venv vendor`
1. Activate the virtualenv using `source vendor/bin/activate`
1. Run `pipenv install` to install dependencies
1. Run `python main.py` to begin extraction

### Configuration

There are two modes to choose candidates for potential usernames. Check the `main()` function in `main.py`.

1. **Dictionary** *(default)* --- Use words from a dictionary
1. **Pronounceable** --- Use random pronounceable words with a threshold on syllables. Use following parameters:
    - USERNAME_MAX_SYLLABLE_COUNT - Maximum syllables count
    - MAX_DESIRED_RESULTS - Number of usernames to scout

Other generic parameters ---

- USERNAME_MAX_LENGTH - Length of desired username
- SLEEP_INTERVAL - Break after each Github ping. (Keep this greater than 200ms to avoid being blacklisted by Github)
- GITHUB_AVAILABLE_USERNAMES_FILE - File name to store the available usernames
- GITHUB_REQUESTS_FILE - File name to store all tried words

### Optimizations

- Check if the current word has already been pinged. If yes, do not ping it again.
