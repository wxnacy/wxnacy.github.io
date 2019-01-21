#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import os

DIR="/Users/wxnacy/WebstormProjects/wxnacy.github.io/hexo/source/_posts"

def filter_art(name):
    if not name.endswith(".md"):
        return None

    file_path = '{}/{}'.format(DIR, name)
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()

    is_right = False
    index = 0
    for l in lines:
        if '<!-- toc -->' in l:
            is_right = True
            break
        index = index + 1

    if not is_right:
        return None

    if lines[index-1] == '\n':
        return None


    return file_path

def fix(name):
    file_path = '{}/{}'.format(DIR, name)
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()
    index = 0
    nlines = []
    for l in lines:
        nlines.append(l)
        if '<!-- toc -->' in l:
            is_right = True
            break
        index = index + 1

    #  print(lines)
    new_lines = nlines[0:index]
    new_lines.append('\n')
    new_lines.extend(lines[index:])
    #  print(new_lines)
    #  new_text = ''.join(new_lines)
    #  print(new_text)
    #  f.writelines(new_lines)

    nf = open(file_path, 'w+')
    nf.writelines(new_lines)
    nf.close()



if __name__ == "__main__":
    files = os.listdir(DIR)
    files = list(filter(lambda x: filter_art(x), files))
    #  print(len(files), files)
    print(len(files))

    #  for name in files[-1:]:
    for name in files:
        fix(name)

    
