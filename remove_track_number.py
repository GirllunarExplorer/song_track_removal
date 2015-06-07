#!/usr/bin/env python
__author__ = 'tracyrohlin'

import os, shutil, sys
from string import capwords
from re import match

def remove_numbers(root, name, file_tag):
    if match(r"\d\d", name[0:2]):
        new_name = capwords((name.split(file_tag))[0][3:]) + file_tag
        new_file_path = os.path.join(root, new_name)
        old_file_path = root + "/" + name
        shutil.move(old_file_path, new_file_path)


def main(file_path):

    for root, dirs, files in os.walk(file_path):
        for name in files:
            try:
                if name.endswith("m4a"):
                    remove_numbers(root, name, ".m4a")
                elif name.endswith("m4p"):
                    remove_numbers(root, name, ".m4p")
                elif name.endswith("mp3"):
                    remove_numbers(root, name, ".mp3")
                elif name.endswith("flac"):
                    remove_numbers(root, name, ".flac")
                else: pass
            except:
                pass

    print "I am done"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(*sys.argv[1:])

    else:
        raise ValueError("Argument must include full path to album, surrounded by double quotes")