#!/usr/bin/env python
# coding:utf-8

import os


# Each website you crawl is a seperate project(directory)
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Create queue and crawled files if not created
def create_data_files(project_name,base_url):
    queue = project_name + 'queue.txt'
    crawled = project_name + 'crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path,data):
    with open(path,'w') as f:
        f.write(data)

# Add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')
        
# Delete contents of a file
def delete_file_contents(path):
    with open(path,'w'):
        pass



