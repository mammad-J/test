from URLs import *
import requests
import json
import os
import random

# docs = https://www.waifu.im/docs/

class WaifuIm:
    def __init__(self, is_nsfw=False, gif=False, many=False):
        self.sfw_tags = ["maid",
                         "waifu",
                         "marin-kitagawa",
                         "mori-calliope",
                         "raiden-shogun",
                         "oppai",
                         "selfies",
                         "uniform"]
        self.nsfw_tags = ["ass",
                          "hentai",
                          "milf",
                          "oral",
                          "paizuri",
                          "ecchi",
                          "ero"]
        self.url = URLs()
        self.base_url = url.base_url()
        self.tags_list = url.tags_list()
        self.search_url = url.search_url()
    
    def random():
        self.response = requests.get(self.search_url + "?many=" + self.many + "&is_nsfw" + self.is_nsfw + "&gif=" + self.gif).json()
        return self.response


    def get_by_tag(included_tags:str):
        self.response = requests.get(self.search_url + "?many=" + self.many + "&is_nsfw" + self.is_nsfw + "&gif=" + self.gif + "&included_tags=" + included_tags).json()
        return self.response


'''
    def download(path=os.getcwd(), links=[]):
        try:

'''
            





waifu = WaifuIm()