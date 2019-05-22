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

# example
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
    # 匹配封面图
    # photos: 
    #  - imgurl
    # result = re.findall('photos\:\n \- (.*?)\n', text)
    # 匹配封面图 photos: imgurl
    # result = re.findall('photos\: (.*?)\n', text)
    # 匹配fancybox插件语法 {% fb_img imgurl desc %}
    # result = re.findall('\{\% fb_img (.*?) ', text)
    # 匹配html <img src="imgurl">
    # result = re.findall('src\=\"(.*?)\"', text)
    # 匹配markdown ![XXX](imgurl)
    result = re.findall('!\[(.*?)\]\((.*?)\)', text)
    
    print(result)
    try:
        for i in range(len(result)):
            # markdown 有两个匹配用这个
            img_quote = result[i][0]
            img_url = result[i][1]
            # 其他的只有一个匹配用这个 注意之后的代码要哦删掉img_quote
            # img_url = result[i]
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