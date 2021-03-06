import urllib.request
from bs4 import BeautifulSoup
import re
from googlesearch import search


# This is an algorithm for searching various websites' top results in Python 3.5, seems to break in 3.7.
# Theoretically, it will return links to top posts so that this string/link can be used for GUIs/other things.

# adapted from: https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
def youtube_search(message):
    query_string = urllib.parse.urlencode({"search_query": message})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    video_string = "http://www.youtube.com/watch?v=" + search_results[0]
    return video_string


# a very basic way of just pulling the top list of the day. Could be better, but without PRAW seems hard to do.
def reddit_search(message):
    if message.__contains__(" "):
        message = message.replace(" ", "")
    reddit_search_string = 'http://www.reddit.com/search?q=' + message + "=top"
    return reddit_search_string

# adapted from: https://stackoverflow.com/questions/3898574/google-search-using-python-script
def google_search(message):
    user_query = message
    for j in search(user_query, tld="co.in", num=10, stop=1, pause=2):
        search_string = j
    return search_string


def top_search():
    message = input("What would you like to search for? ")
    print("One moment...")
    youtube_string = "here is the top YouTube result: " + youtube_search(message)
    google_string = "here is the top Google result: " + google_search(message)
    reddit_string = "here is the top Reddit result: " + reddit_search(message)

    print(youtube_string)
    print("\n")
    print(google_string)
    print(reddit_string)


top_search()
