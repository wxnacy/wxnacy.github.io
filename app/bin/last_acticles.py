#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from requests_html import HTMLSession

session = HTMLSession()

def print_last():
    '''打印最新文章'''
    r = session.get("https://wxnacy.com")
    sed = '#post-ffmpeg-split-video-audio > div > header > h1 > a'
    title_a = r.html.find('.article-title')
    for t in title_a:
        out = f'{t.text}: {t.attrs["href"]}'
        print(out)

if __name__ == "__main__":
    print_last()
     
