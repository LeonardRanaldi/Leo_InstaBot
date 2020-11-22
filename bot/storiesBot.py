# -*- coding: utf-8 -*-

'''
Created in 11/2020
@Author: Leo
'''

# imported libraries
import os
import consoleArt
import readFile
import random
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def functionStories(mySystem):

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
        mySystem = 'clear' #https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-macos.tar.gz
        #way = Path('./geckodriver-v0.28.0-macos') # path to the file
        geckoFile = '/usr/local/bin/geckodriver' # way to geckodriver




    # input for config bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    consoleArt.artName(0)

    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')

    #delay = int(input('Delay (just number): ')) # loading delay time

    delay = 2

    # input info for bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    #consoleArt.artName(0)

    print('')
    print('\033[0;32mLOGIN INFORMATION OK\033[m')
    print('')

    username_pass = readFile.readFromFile()
    username = username_pass[0]
    password = username_pass[1]

    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    #consoleArt.artName(0)

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


    # function to access the login page and log in
    def botlogin (user, pwd):

        username = user
        password = pwd

        driver.get('https://www.instagram.com/') # instagram url
        sleep(delay)

        userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
        userelement.clear()
        userelement.send_keys(username) # user insertion in 'user' element

        pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
        pwdelement.clear()
        pwdelement.send_keys(password) # password insertion in 'password' element

        pwdelement.send_keys(Keys.RETURN) # log in to page

        sleep(4)


    def stories(): # function to view the stories

        driver.find_element_by_xpath("//button[contains(text(),'Accetta')]").click()

        try:

            driver.find_element_by_xpath('//button[contains(text(), "Non ora")]').click() # press the notification button that appears most of the time, denying the option
            sleep(delay)

        except:
            pass

        try:

            driver.find_element_by_xpath('//button[contains(text(), "Non ora")]').click() # press the notification button that appears most of the time, denying the option
            sleep(delay)

        except:
            pass

        driver.find_element_by_class_name('_6q-tv').click() # click on the tab where the stories are
        sleep(delay)

        loadstories = '' # variable to terminate the loop without errors

        while loadstories != 0:

            sleep(delay)

            try:

                driver.find_element_by_class_name('coreSpriteRightChevron').click() # next storie button

            except KeyboardInterrupt:

                print('\033[0;33mProgram terminated by the user!\033[m')
                loadstories = 0

            except:

                print('\033[0;33mEND! Non ci sono più storie da vedere\033[m')
                loadstories = 0


    # running function for login
    try:

        botlogin(username, password)

    except KeyboardInterrupt:

        print('\033[0;33mProgram terminated by the user!\033[m')

    except:

        print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')

    # running function to see the stories
    try:

        stories()

    except KeyboardInterrupt:

        print('\033[0;33mProgram terminated by the user!\033[m')

    except:

        print('\033[0;31mUNEXPECTED ERROR ON STORIES\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem)


#functionStories('Linux')
