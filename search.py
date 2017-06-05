# search.py
import os
import sys


def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            print fp
        elif os.path.isdir(fp):
            search(fp, word)

search(sys.argv[1], sys.argv[2])
