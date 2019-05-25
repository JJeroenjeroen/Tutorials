def nr_to_roman(num):
    rom = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L','XC', 'C','CD', 'D', 'CM', 'M']
    val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    i = (len(val)-1)
    roman_numeral = ""
    while num > 0:
        if num // val[i] != 0:
            roman_numeral += (num // val[i]) * rom[i]
            num -= (num // val[i]) * val[i]
        i -= 1
    return roman_numeral

print(nr_to_roman(345))



def roman_to_nr(roman):
    rom_special = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    rom_normal = ['I', 'V', 'X', 'L','C','D', 'M']
    val_special = [4, 9, 40, 90, 400, 900]
    val_normal = [1, 5, 10, 50, 100, 500, 1000]

    nr = 0
    while len(roman) > 0:
        for x in rom_special:
            if x in roman:
                i = rom_special.index(x)
                nr += val_special[i]
                roman = roman.replace(x, "")
        for y in rom_normal:
            if y in roman:
                i = rom_normal.index(y)
                nr += (roman.count(y) * val_normal[i])
                roman = roman.replace(y, "")
    return nr


print(roman_to_nr('MMMCMLXXXVI'))


def bracket_validity(string):
    bracket_open = ['(', '{', '[']
    bracket_close = [')', '}', ']']
    for i in range(len(string)):
        if string[i] in bracket_open:
            if string[i+1] != bracket_close[bracket_open.index(string[i])]:
                return "Invalid"
    return "Valid"


def find_sum(list, target):
    for i in list:
        for y in list:
            if i + y == target and list.index(i) != list.index(y):
                return [list.index(i), list.index(y)]
                pass
    return "There are no valid combinations"

print(find_sum([10,20,10,40,50,60,70], 130))