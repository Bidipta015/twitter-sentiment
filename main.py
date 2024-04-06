# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from src.main.config import *
from src.main.read_tweets import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_directory = os.getcwd()
    config_file_path = os.path.join(current_directory, 'src/main/application.conf')
    print_hi('PyCharm')

    config = Config.from_file(config_file_path)
    client = connect(config)

    hashtag = "#100daysofcode"
    tweets = client.get_home_timeline(query=hashtag, max_results=2, user_auth=True)
    for tweet in tweets:
        print(tweet.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
