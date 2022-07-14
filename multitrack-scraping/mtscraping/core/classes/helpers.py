import requests


class Helper:
    def __init__(self, page_url):
        self.page_url = page_url
        self.response = requests.get(self.page_url)