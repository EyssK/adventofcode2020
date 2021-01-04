#!/usr/bin/python3
import re

def get_elems(passports, checks):
    for passport in passports:
        res = list()
        for check in checks:
            res.append(check_re(passport,check))
        yield res
        
def check_re(passport, regxp):
    for elem in passport:
        toto = regxp.search(elem)
        if toto:
            return toto[1]
    return False

def get_checks():
    checks = {
       "byr": re.compile("byr:(.*)"),
       "iyr": re.compile("iyr:(.*)"),
       "eyr": re.compile("eyr:(.*)"),
       "hgt": re.compile("hgt:(.*)"),
       "hcl": re.compile("hcl:(.*)"),
       "ecl": re.compile("ecl:(.*)"),
       "pid": re.compile("pid:(.*)"),
       "cid": re.compile("cid:(.*)") }
    return checks

def check_part1(check_res):
    nofalse = { key:value for (key,value) in check_res.items() if value }
    if len(nofalse) == 8:
        return True
    else:
        if (len(nofalse) == 7) and (check_res["cid"] == False):
            return True
    return False

def check_pass(passports):
    res = 0
    checks = get_checks()
    for passport in passports:
        passport = passport.split()
        check_res = { key:check_re(passport,value) for (key,value) in checks.items()}
        if check_part1(check_res):
            res +=1
    return res

def rangecheck(val,mn,mx):
    try:
        a = int(val)
        if (a < mn) or (mx < a):
            print(a,mn,mx)
            return False
        else:
            return True
    except ValueError:
        return False

def check_part2(check_res):
    if not rangecheck(check_res["byr"], 1920, 2002):
        print("Fail: ", "byr",check_res["byr"])
        return False
    if not rangecheck(check_res["iyr"], 2010, 2020):
        print("Fail: ", "iyr",check_res["iyr"])
        return False
    if not rangecheck(check_res["eyr"], 2020, 2030):
        print("Fail: ", "eyr",check_res["eyr"])
        return False

    if check_res["hgt"][-2:] == 'cm':
        if not rangecheck(check_res["hgt"][:-2], 150, 193):
            print("Fail: ", "hgt",check_res["hgt"])
            return False
    elif check_res["hgt"][-2:] == 'in':
        if not rangecheck(check_res["hgt"][:-2], 59, 76):
            print("Fail: ", "hgt",check_res["hgt"])
            return False
    else:
        print("Fail: ", "hgt",check_res["hgt"])
        return False
            
    if check_res["hcl"][0] == '#':
        try:
            int(check_res["hcl"][1:],base=16)
        except ValueError:
            print("Fail: ", "hcl",check_res["hcl"])
            return False
    else:
        print("Fail: ", "hcl",check_res["hcl"])

    if check_res["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
        print("Fail: ", "ecl",check_res["ecl"])
        return False

    if len(check_res["pid"]) == 9:
        try:
            int(check_res["pid"])
        except ValueError:
            print("Fail: ", "pid",check_res["pid"])
            return False
    else:
        print("Fail: ", "pid",check_res["pid"])
        return False

    
    return True
    

def check_pass2(passports):
    res = 0
    checks = get_checks()
    for passport in passports:
        passport = passport.split()
        check_res = { key:check_re(passport,value) for (key,value) in checks.items()}
        if check_part1(check_res):
            if check_part2(check_res):
                res +=1
            print(check_res,res)
    return res

if __name__ == "__main__":
    with open("input") as file:
        passports = file.read().split("\n\n")
        
    #passports = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm\n\niyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929\n\nhcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm\n\nhcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in".split("\n\n")

    #Part1
    print( "Part1: ", check_pass(passports))

    #Part2
    print( "Part2: ", check_pass2(passports))
