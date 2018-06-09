#!usr/bin/env python  
# coding:utf-8
""" 
@author:xuqing 
@file: main.py 
@time: 2018/06/07 
"""
import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r"D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_url('http://www.srcb.com','srcb.pdf',configuration=config)