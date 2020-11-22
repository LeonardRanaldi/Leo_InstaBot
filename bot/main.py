
# imported libraries
import os
print(os.path)
import consoleArt
import platform
import likeBot
import commentBot
import storiesBot
import storiesBotByUser



mySystem = platform.system() #os running for select geckodriver folder

while True:

    consoleArt.artName(2) #print console pyfiglet

    menu = ['Like', 'Comment and Like', 'View Stories', 'View Stories of Users']

    for indice, lista in enumerate(menu): # loop to generate an index in the list of options

        print(f'\033[0;34m[{indice}]\033[m {lista}') # print the list of options

    print('')
    print('\033[0;33m(per uscire premi Ctrl + C)\033[m')

    selected = int(input('Scegli cosa vuoi fare: (0 Like, 1 Comment and Like, 2 View Stories, 3 View Stories of Users) ')) # receive the function that will be started

    print('')

    if selected == 0:

        likeBot.functionLike(mySystem) # bot to like

    elif selected == 1:

        commentBot.functionComment(mySystem) # bot to like and comment

    elif selected == 2:

        storiesBot.functionStories(mySystem) # bot to see stories

    elif selected == 3:

        storiesBotByUser.functionStories(mySystem) # bot to see stories of users in list

    else:

      print('Opzione non valida, riprova!')
