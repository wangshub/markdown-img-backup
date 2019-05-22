
# coding=utf-8
import sys
import os
import re
import requests
import urllib
import urllib2


def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            print fp
            download(str(fp))
        elif os.path.isdir(fp):
            search(fp, word)


def download(file_path):
    # filename = "test"
    name = file_path.split(u"/")
    filename = name[-1]
    f_md = open(file_path)

    # all text of md file
    text = f_md.read().decode('utf-8')
    # regex
    img_reg = r'\!{1}\[(.*?)\]\((.*?)\)'
    # 非贪婪匹配
    result = re.findall('!\[(.*?)\]\((.*?)\)', text)

    for i in range(len(result)):
        img_quote = result[i][0]
        img_url = result[i][1]
        # download img
        request = urllib2.Request(img_url)
        response = urllib2.urlopen(request)
        img_contents = response.read()
        # img name spell
        urlname = img_url.split(u"/")
        img_name = filename + '_' + \
            str(i) + '_md_' + img_quote + str(urlname[len(urlname) - 1])
        print img_name, '~~~', img_url
        # write to file
        f_img = open('img/' + img_name, 'wb')
        f_img.write(img_contents)
        f_img.close()
    f_md.close()

search(sys.argv[1], '.md')
