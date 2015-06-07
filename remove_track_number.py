#!/usr/bin/env python
__author__ = 'tracyrohlin'

import os, shutil, sys
from string import capwords
import re

def remove_numbers(root, name, file_tag):
    print "I am in program"
    if re.match(r"\d\d", name[0:2]):
        new_name = capwords((name.split(file_tag))[0][3:])

        # gets rid of (featuring artist) and (ft. artist) from file name
        feat_pattern = re.compile(r'.feat.+')
        ft_pattern = re.compile(r'(ft.+)')
        patterns = [feat_pattern, ft_pattern]
        for pattern in patterns:
            match = re.search(pattern, new_name)
            if match:
                new_name = pattern.sub("", new_name)[:-1]
            else:
                pass

        # forces capitalization after a parentheses
        i=0
        pattern = re.compile(r"\(")
        for p_match in re.finditer(pattern, new_name):
            i = p_match.start()+1
        new_name = new_name[:i]+ new_name[i:].capitalize()
        new_name+= file_tag

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
            except Exception as error:
                print error

    print "I am done"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(*sys.argv[1:])

    else:
        raise ValueError("Argument must include full path to album, surrounded by double quotes")