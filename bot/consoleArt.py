# -*- coding: utf-8 -*-

'''
Created in 11/2020
@Author: Leo
'''

# imported libraries
from time import sleep
from pyfiglet import Figlet

def artName(timeSleep=0): # function to print text in ascii art

    f = Figlet(font='slant')
    instagramName = f.renderText('LeoBot Instagram')
    print(instagramName)
    sleep(timeSleep)
