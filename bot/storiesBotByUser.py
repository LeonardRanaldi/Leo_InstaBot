'''
Created in 11/2020
@Author: Leo
'''

# imported libraries
import os
import consoleArt
import readFile
import random
import readFile
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def functionStoriesByName(mySystem):

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
        way = Path('/usr/local/bin/geckodriver') # path to the file
        geckoFile = way




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
    print('\033[0;32mLOGIN INFORMATION\033[m')
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


    def storiesByName(): # function to view the stories of certain user read from the list

        print('Mette like ad utenti presenti nel file di testo utenti.txt')

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

        listUser = readFile.readUserFromFile()

        print('Utenti presenti nella lista: ',listUser)

        for name in listUser:

            try:

                driver.get(f'https://www.instagram.com/{name}/') # instagram tag page url

            except:
                print('\033[0;33mUtente non trovato! (riscrivi nome corretto o vedi se è ancora attivo)\033[m', name)


            sleep(delay)

            driver.find_element_by_class_name('_6q-tv').click() # click on the tab where the stories are
            sleep(delay-1)

            loadstories = '' # variable to terminate the loop without errors

            while loadstories != 0:

                sleep(random.randint(delay, delay+6))

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

        storiesByName()

    except KeyboardInterrupt:

        print('\033[0;33mProgram terminated by the user!\033[m')

    except:

        print('\033[0;31mUNEXPECTED ERROR ON STORIES\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')

    #driver.quit()

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem)


#functionStoriesByName('Linux')
