# -*- coding: utf-8 -*-

'''
Created in 11/2020
@Author: Leo
'''

# imported libraries
import os
import consoleArt
import random
import readFile
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def functionComment(mySystem):

    # check the system
    if mySystem == 'Linux':

        mySystem = 'clear'
        way = Path('./geckodriver-v0.26.0-linux64') # path to the file
        geckoFile = way / 'geckodriver' # way to geckodriver

    elif mySystem == 'Windows':

        mySystem = 'cls'
        way = Path('geckodriver/windows') # path to the file
        geckoFile = way / 'geckodriver.exe' # way to geckodriver

    elif mySystem == 'Darwin':
        mySystem = 'clear'
        #way = Path('./geckodriver-v0.28.0-macos') # path to the file
        geckoFile = '/usr/local/bin/geckodriver' # way to geckodriver




    # input for config bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    consoleArt.artName(0)

    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')

    delay = int(input('Delay time(just number): ')) # loading delay time

    # input login for bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    consoleArt.artName(0)

    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')

    username_pass = readFile.readFromFile()
    username = username_pass[0]
    password = username_pass[1]

    # input info for bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    consoleArt.artName(0)

    print('')
    print('\033[0;32mBOT INFORMATION\033[m')
    print('')

    hashtag = str(input('Hashtag (senza #): ')) # hashtag
    likes = int(input('Numero di Like: ')) # amount of photos to like
    comment = str(input('Commento: ')) # comment in photos

    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    try:

        driver = webdriver.Firefox(executable_path=f'{geckoFile}')

    except:

        try:

            driver = webdriver.Firefox()

        except:

            print('\033[0;31mDRIVER ERROR!\033[m Check installed drive or path.')


    def botlogin (user, pwd): # function to access the login page and log in

        username = user # your user
        password = pwd # your password

        driver.get('https://www.instagram.com/') # instagram url
        sleep(delay)

        '''
        this page / button was removed by Instagram
        driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button element
        '''

        userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
        userelement.clear()
        userelement.send_keys(username) # user insertion in 'user' element

        pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
        pwdelement.clear()
        pwdelement.send_keys(password) # password insertion in 'password' element

        pwdelement.send_keys(Keys.RETURN) # log in to page
        sleep(delay + 2)


    def findhashtag(hashtag): # function hashtag search page

        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


    def typephrase(comment, field): # function to type letter by letter

        for letter in comment: # commentary and lyrics

            field.send_keys(letter) # type the letter in the field
            sleep(1) # input time of each letter


    def likecomment(likes=1, comment=''): # function to like the photos

        driver.find_element_by_xpath("//button[contains(text(),'Accetta')]").click()

        driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload

        likesAlready = readFile.readLikesFromFile()

        item = 1
        while item <= likes: # loop with how many photos to like

            try:

                sleep(delay)

                if driver.current_url not in likesAlready:

                    driver.find_element_by_class_name('fr66n').click() # click the like button
                    readFile.writeLikesFromFile(driver.current_url) #append new url to list of url liked


                driver.find_element_by_class_name('Ypffh').click() # click the field to insert comment
                field = driver.find_element_by_class_name('Ypffh')
                field.clear()
                typephrase(comment, field) # insert comment typing each letter
                sleep(delay)

                # the 'publish' button name changes according to your instagram language
                driver.find_element_by_xpath('//button[contains(text(), "Pubblica")]').click() # click the post 'comment' button element
                sleep(random.randint(1,5)) # break time between likes and comment due to instagram policy against bots
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
                item = item + 1

            except:

                sleep(60) # if connection errors occur

        print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')


    # running function for login
    try:

        botlogin(username, password)

    except KeyboardInterrupt:

        print('\033[0;33mProgram terminated by the user!\033[m')

    except:

        print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')

    # executing function search hastag
    try:

        findhashtag(hashtag)

    except KeyboardInterrupt:

        print('\033[0;33mProgram terminated by the user!\033[m')

    except:

        print('\033[0;31mUNEXPECTED ERROR ON HASHTAG PAGE\033[m, please try again and verify your connection!')

    # executing function to enjoy and comment
    try:

        likecomment(likes, comment)

    except KeyboardInterrupt:

        print('\033[0;33mProgram terminated by the user!\033[m')

    except:

        print('\033[0;31mUNEXPECTED ERROR ON COMMENT\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem)
