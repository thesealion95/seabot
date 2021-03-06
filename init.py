#!/usr/bin/python3

import string

def joinRoom(s):
    """ Protocol for joining chat room """

    readbuffer = ""
    loading = True
    while loading:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            loading = loadingComplete(line)
            if loading != True:
                break

    print 'Successfully joined chat!'
    # sendMessage(s, "Successfully joined chat!")

def loadingComplete(line):
    """ Check if bot has finished loading into chat """

    if "End of /NAMES list" in line:
        #print('false')
        return False
    else:
        #print('true')
        return True
