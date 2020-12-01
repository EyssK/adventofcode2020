#!/usr/bin/python3


if __name__ == "__main__":
    with open("input") as file:
        lines = file.read().splitlines()

    elem = [ int(x) for x in lines ]

    find = False
    for i in elem:
        for j in elem:
            if i+j == 2020:
                print("Part1: ",i*j)
                find = True
                break
        if find:
            break

    find = False
    for i in elem:
        for j in elem:
            for k in elem:
                if i+j+k == 2020:
                    print("Part2: ",i*j*k)
                    find = True
                    break
            if find:
                break
        if find:
            break
