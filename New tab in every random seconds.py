# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:16:34 2020

@author: Administrator
"""


import webbrowser
import time
import random

while True:
    site=random.choice(['google.com','youtube.com','weather.gov'])
    visit="http://{}".format(site)
    webbrowser.open(visit)
    sec=random.randrange(5,20)
    time.sleep(sec)