---
title: 使用python备份博客图片
date: 2017-06-05T23:09:29.000Z
categories:
  - python
  - markdown
  - code
tags:
  - python
  - markdown
  - code
---

<!-- more -->

 # 说明

最近在写markdown文档的过程中,经常需要插入一些图片.因为托管博客的服务器空间有限,所以上传图片到图床再插入到markdown中.有时候又插入网上的图片,这些图片随时可能失效.导致我的博客网站显示图片错误.<br>
所以花了一点时间,用python _正则匹配_ markdown中图片链接,然后下载图片保存到本地文件夹`img`中.这样就不用担心图片失效啦,当我找到稳定的图床,可以随时把这些图片再上传更新,美滋滋~~~

# 功能

- [x] `.md`文件自动搜索
- [x] 正则匹配图片链接
- [x] 爬取图片内容
- [x] 保存文本到本地

# 步骤

**读取文件** => **正则匹配** => **图片下载** => **保存本地**

# python代码

详细见我的github地址: www.github.com/wangshub

```python

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
    result = re.findall('!\[(.*)\]\((.*)\)', text)

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
            str(i) + '_' + img_quote + str(urlname[len(urlname) - 1])
        print img_name, '~~~', img_url
        # write to file
        f_img = open('img/' + img_name, 'wb')
        f_img.write(img_contents)
        f_img.close()
    f_md.close()

search(sys.argv[1], '.md')
```

# 食用方法

`python md_image_bacup.py /path/to/your/file/`

# 作者

> Author : _WangSong_<br>
> E-mail : _easternslope@yeah.net_
