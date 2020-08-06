import os


def getDir():
    basedir = os.getcwd() + "/"
    print('I am at ' + os.getcwd() + "!")
    return basedir
