#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://www.gavbus558.com').content
soup = BeautifulSoup(html_doc)
print(soup.title)

urls = soup.find_all('a', class_="movie-box")
for url_doc in urls:
    print(url_doc['href'])
