#!/bin/env python

import os
import shutil



def scan_files():
    files = os.listdir()
    for f in files:
        if f.endswith('.zip') or f.endswith('.gz') or f.endswith('.bz2'):
            return f
    


def unzip(f):
    folder_name = f.split('.')[0]
    target_path = './' + folder_name
    if not target_path:
        os.makedirs(target_path)
    shutil.unpack_archive(f,target_path)

def delete(f):
    os.remove(f)


while True:
    zip_file = scan_files()
    if zip_file:
        unzip(zip_file)
        delete(zip_file)    


