from secret import TOKEN, CID
import requests as r
import json as j
from time import sleep
from telebot import TeleBot
from scraper import fetch
bot = TeleBot(TOKEN)

base_url = "https://tesla.com"
cached = []
while(True):
    print("fetching..")
    scList = fetch()
    print("fetched: " + str(scList))
    if not cached == []: # do not run until 2nd fetch onwards
        for s in scList: # compare with previous fetch
            found = 0
            for c in cached:
                if (s['name'] == c['name']):
                    found = 1
            if found == 1:
                print(str(s['name']) + " found in cache")
            else:
                bot.send_message(CID, "New Tesla Supercharger found at " + str(s['name'] + "\nURL: " + base_url + str(s['url'])))
    cached = scList
    print("waiting..")
    sleep(69)