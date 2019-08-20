import requests
import json


API_ROOT = 'https://mashape-community-urban-dictionary.p.rapidapi.com/define?term='


def Get_Define(query):
    print(API_ROOT + query)
    return requests.get(API_ROOT + query,
   headers={
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
        "X-RapidAPI-Key": "Your Key Here"
  }
).json()

def unknown_word(query):
    print("Try a different spelling, that word is coming up:")
    request_word()


def display_UD(meaning):
    print("This should help: \n")
    for entry in meaning['list']:
        define = entry['definition']
        permalink = entry['permalink']
        word = entry['word']
        example = entry['example']
        print(f"\n\nDefinition: {define}\n\nURL: {permalink}\n\nSlang: {word}\n\nHow to use: {example}\n\n")

def request_word():
    try:
        lingo = ''
        while not lingo:
            lingo = input("What word is your kid using, that you want looked up?\t")
        uw = Get_Define(lingo)
        if len(lingo) == 0:
            print("Lets start by typing a word.")
        else:
            search = uw
            display_UD(search)
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Is the network up?")


if __name__ == '__main__':
    while True:
        request_word()
