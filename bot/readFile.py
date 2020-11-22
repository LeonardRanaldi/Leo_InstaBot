'''
Created in 11/2020
@Author: Leo
'''



def readFromFile():

    f = open("login", "r")
    username_password = f.readlines()
    username = username_password[0].replace('\n','').replace("'","").replace('username:','')
    password = username_password[1].replace('\n','').replace("'","").replace('password:','')
    return username,password

def readLikesFromFile():
    file = open('likes', 'r')
    likes = file.readlines()
    likes = [x.replace('\n','') if '\n' in x else x for x in likes]
    likes = list(set(likes))
    return likes

def readUserFromFile():
    file = open('utenti', 'r')
    likes = file.readlines()
    likes = [x.replace('\n','') if '\n' in x else x for x in likes]
    likes = list(set(likes))
    return likes


def writeLikesFromFile(url):
    file = open("likes", "a")
    file.write(url)
    file.write('\n')
    file.close()

#readLikesFromFile()
