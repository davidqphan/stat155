import json
from pprint import pprint

def parse_all(reds, function):
    red_lst = parse(reds)
    func_lst = []

    for n in function:
        func_lst.append(parse(function[n]))

    return red_lst, func_lst

def parse(nums):
    return [ float(num) for num in nums ]

pasta_file = open('pasta.json')

pasta = json.load(pasta_file)

book_obj = pasta['book']

function = book_obj['function']
reds = book_obj['reds']

print('book obj: ')
pprint(book_obj)
print('\n')

print('function: ')
pprint(function)
print('\n')

print('reds: ')
pprint(reds)
print('\n')

red_nums = parse(reds)
print(red_nums)

red_lst, func_lst = parse_all(reds, function)
print(red_lst)
print(func_lst)

func_1st = func_lst[0]
print(func_1st)

for n in func_1st:
    print(n)

