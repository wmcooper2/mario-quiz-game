#!/usr/bin/python3

from juniorhighenglishwords import Junior_High_English_Words as jhs

from verbforms import verb_forms as verbs

def count():
    (sum(1 for verb in verbs.keys()))

def find_paren_in_nested_value():
    for k,v in verbs.items():
        for key, value in v.items():
            if "(" in value:
                print(k)


def find_paren_in_nested_value2():
    for k,v in jhs.items():
        for key, value in v.items():
            if "(" in value or "[" in value:
                print(k)

find_paren_in_nested_value2()
