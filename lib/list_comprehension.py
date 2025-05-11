#!/usr/bin/env python3

def return_evens(num_list):
    print(num_list)
    evens=[num for num in num_list if num%2 == 0]
    print(evens)
    return evens

def make_exclamation(sentence_list):
    print(sentence_list)
    print( [f"{sentence}!" for sentence in sentence_list])

    return [f"{sentence}!" for sentence in sentence_list]
    pass

return_evens([5,3,4,6,8,7,5,12,10,59,32])
make_exclamation(["Hello", "Hey", "Whats up"])