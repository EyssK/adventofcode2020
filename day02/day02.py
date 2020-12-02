#!/usr/bin/python3
import re

"""
    generator
    input is the puzzle input as list of strings
    output a tuple of (min,max,letter,password)
"""
def get_rules(passlist):
    s = re.compile("([0-9]+)\-([0-9]+) ([a-z]): ([a-z]+)")
    for rule in passlist:
        x = s.match(rule)
        if x:
            yield (int(x[1]),int(x[2]),x[3],x[4])

def check_rule(rule):
    (mn,mx,letter,passw) = rule
    a = [ l for l in passw if l == letter ]
    if mn <= len(a) <= mx:
        return True
    else:
        return False

def check_rule2(rule):
    (idx1,idx2,letter,passw) = rule
    if (passw[idx1-1] is letter) ^ (passw[idx2-1] is letter):
        return True
    else:
        return False

if __name__ == "__main__":
    with open("input") as file:
        lines = file.read().splitlines()

    #Part1
    res = sum( 1 for x in get_rules(lines) if check_rule(x) )
    print( "Part1: ", res )

    #Part2
    res = sum( 1 for x in get_rules(lines) if check_rule2(x) )
    print( "Part1: ", res )
