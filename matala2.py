# -*- coding: utf-8 -*-
"""
matala 2

Danielle Gamish
205454127
"""

## A:
def  reverse(sentence, reverse_word):
    
    if not isinstance(reverse_word, str):
        return('invalid input')
    
    reverse = sentence.find(reverse_word)
    new_word = reverse_word[::-1]
    
    if reverse == -1:
        
        up = reverse_word.upper()
        sentence_up = sentence.upper()
        reverse_up = sentence_up.find(up)
        if reverse_up >=0:
            return('no match word found')
        else:
            return('The word was not found')

    else:   
        newsen = sentence.replace(reverse_word, new_word, 1)
        return(newsen)
    

