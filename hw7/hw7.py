#!/usr/bin/env python3
import sys
import json
from pprint import pprint
from math import sqrt
from fractions import Fraction
import os.path
import statistics as stats
import scipy.stats as scistats
import scipy.misc as scimisc
from scipy.integrate import quad
from collections import OrderedDict

def book():
    book_red, book_func = parse_numbers('book')

    hour = book_red[0]
    coeff, a, b = book_func[0][:]

    a_sol = round(integral(a, 1, 0, coeff, 0), 3)
    b_sol = round(integral(0.5, 1.5, 0, coeff, 0), 3)
    c_sol = round(integral(1.5, b, 0, coeff, 0), 3)
    solns = [ a_sol, b_sol, c_sol ]

    print_solns(solns)

def chemical():
    chem_red, chem_func = parse_numbers('chemical')

    A, B, b_a, b_b, c_a, c_b, d_a, d_b = chem_red[:]
    coeff = 1/(B-A)

    a_sol = round(integral(A, 0, 0, 0, coeff), 3)
    b_sol = round(integral(b_a, b_b, 0, 0, coeff), 3)
    c_sol = round(integral(c_a, c_b, 0, 0, coeff), 3)
    d_sol = round(integral(0, 4, 0, 0, coeff), 3)
    solns = [ a_sol, b_sol, c_sol, d_sol ]

    print_solns(solns)

def checkout():
    print('checkout')

def weight():
    print('weight')

def measurement():
    print('measurement')

def ecologist():
    print('ecologist')

def laser():
    print('laser')

def lecture():
    print('lecture')

def headway():
    print('headway')

def propane():
    print('propane')

def print_solns(solutions):
    d = map_sol(solutions)

    for part in d:
        print('part {}: {}\n'.format(part, d[part]))

def map_sol(solutions):

    parts = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]

    d = OrderedDict()

    for part, sol in zip(parts, solutions):
        d[part] = sol

    return d


def integrand(x, a, b, c):
    return a * (x**2) + b * x + c

def integral(lower, upper, a, b, c):
    ans, err = quad(integrand, lower, upper, args=(a, b, c))
    return ans

def parse_numbers(obj):

    prob_obj = parse_object(obj)

    reds = prob_obj['reds']
    functions = prob_obj['function']

    red_lst = parse(reds)
    func_lst = parse_func(functions)

    return red_lst, func_lst

def parse_func(functions):
    lst = []

    for n in functions:
        lst.append(parse(functions[n]))

    return lst

def parse(nums):
    return [ float(num) for num in nums ]

def parse_object(obj):
    pasta_json = parse_json()
    return pasta_json[obj]

def parse_json():
    with open('pasta.json') as f:
        pasta = json.load(f, object_pairs_hook=OrderedDict)
    return pasta

user_options = [ 'book', 'chemical', 'checkout', 'weight', 'measurement',
                 'ecologist', 'laser', 'lecture', 'headway', 'propane'
               ]

options = { 1 : book, 2 : chemical, 3 : checkout, 4 : weight, 5 : measurement,
            6 : ecologist, 7 : laser, 8 : lecture, 9 : headway, 10 : propane
          }

def main():

    while True:
        print('Select an option:\n')

        for i, option in enumerate(user_options):
            print('   {}.  {}'.format(i+1, option))
        print('   ')

        try:
            sel = input()
        except KeyboardInterrupt:
            print('\nBye Felicia!')
            quit()

        if int(sel) >= 1 and int(sel) <= len(options):
            print(int(sel))
            options[int(sel)]()


if __name__ == "__main__":
    main()
