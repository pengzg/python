#!/usr/bin/python
# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup as bs

r = requests.get("http://www.cctv.com")

r.encoding  = r.apprent_encoding

soup = ba(r.txt)

text = soup.find_all("a")

for i in text:
    print(i.get_text())