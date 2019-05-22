# coding=utf-8
import sys
import os
import re
import requests
import urllib.request


def backup():
    try:
        # 备份指定文件的img
        download(str('你的markdown文件路径' + sys.argv[1]))
    except IndexError:
        # 备份文件夹下的所有img
        search('你的markdown文件路径', '.md')

# def backup():
#     try:
#         download(str('E:\\blog\\hojunBlog19.05.21\\source\\links\\' + sys.argv[1]))
#     except IndexError:
#         search('E:\\blog\\hojunBlog19.05.21\\source\\links', '.md')

def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            print(fp)
            download(str(fp))
        elif os.path.isdir(fp):
            search(fp, word)


def download(file_path):
    # filename = "test"
    name = file_path.split(u"\\")
    filename = name[-1]
    f_md = open(file_path, 'rb')

    # all text of md file
    text = f_md.read().decode('utf-8')
    # regex
    # img_reg = r'\!{1}\[(.*?)\]\((.*?)\)'
    # result = re.findall('photos\:\n \- (.*?)\n', text)
    # result = re.findall('photos\: (.*?)\n', text)
    # result = re.findall('\{\% fb_img (.*?) ', text)
    # result = re.findall('src\=\"(.*?)\"', text)
    result = re.findall('!\[(.*?)\]\((.*?)\)', text)
    
    print(result)
    try:
        for i in range(len(result)):
            img_quote = result[i][0]
            img_url = result[i][1]
            # download img
            request = urllib.request.Request(img_url)
            response = urllib.request.urlopen(request)
            img_contents = response.read()
            # img name spell
            urlname = img_url.split(u"/")
            img_name = filename + '_' + \
            str(i) + '_md_' + img_quote + str(urlname[len(urlname) - 1])
            img_name = img_quote + str(urlname[len(urlname) - 1])
            # img_name = str(urlname[len(urlname) - 1])
            print (img_name + '~~~' + img_url)
            # write to file
            f_img = open('img/' + img_name, 'wb')
            f_img.write(img_contents)
            f_img.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
    f_md.close()

backup()