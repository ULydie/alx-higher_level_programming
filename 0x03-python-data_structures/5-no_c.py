#!/usr/bin/python3
def no_c(my_string):
    word = []
    for l in my_string:
        if l != 'c' and l != 'C':
            word.append(l)
    return ''.join(word)
