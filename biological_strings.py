from gettext import find
from string import *
from posixpath import split 

def countSubStringMatch(target,key):
    count = 0
    lenstarget = len(target)
    key_count = 0
    while count <= lenstarget:
        string_count = str.find(target,key,count)
        count = string_count + 1
        if string_count > -1:
            key_count = key_count + 1
        if string_count == -1:
            return key_count
    return key_count
def subStringMatchExact(target, key):
    count = 0
    lenstarget = len(target)
    key_count = 0
    listposition = []
    while count <= lenstarget:
        string_count = str.find(target,key,count)
        count = string_count + 1
        if string_count > -1:
            listposition.append(string_count)
        if string_count == -1:
            return listposition

def breakString(target, key):
    count = 0
    list_of_letters = list(key)
    while count < len(key):
        new_key = key.split(list_of_letters[count])
        key1 = new_key[0]
        key2 = new_key[1]
        starts1 = subStringMatchExact(target, key1)
        starts2 = subStringMatchExact(target, key2)
        lenght = len(key1)
        count = count + 1
        if starts1 == None:
            starts1 = []
        if starts2 == None:
            starts2 = []
        constrainedMatchPair(starts1,starts2,lenght)

def constrainedMatchPair(starts1,starts2,lenght):
    tuples = []
    count = 0
    m = lenght
    while count < len(starts1):
        n = starts1[count]
        sum = n + m + 1
        for c in starts2:
            if sum == c:
                tuples.append(n)
        count = count + 1
    return print(tuples)
