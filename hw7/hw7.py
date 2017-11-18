import sys
import json
from pprint import pprint
from math import pi, sqrt
from fractions import Fraction
import os.path
import statistics as stats
import scipy.stats as scistats
import scipy.misc as scimisc
import numpy as np
from scipy.integrate import quad
from collections import OrderedDict

def book():
    book_red, book_func = parse_numbers('book')

    hour = book_red[0]
    coeff, a, b = book_func[0][:]

    a_sol = round(integral(a, 1, 0, 2,  coeff, 0), 3)
    b_sol = round(integral(0.5, 1.5, 0, 2, coeff, 0), 3)
    c_sol = round(integral(1.5, b, 0, 2, coeff, 0), 3)
    solns = [ a_sol, b_sol, c_sol ]

    print_solns(solns)

def chemical():
    chem_red, chem_func = parse_numbers('chemical')

    A, B, b_a, b_b, c_a, c_b, d_a, d_b = chem_red[:]
    coeff = 1/(B-A)

    a_sol = round(integral(A, 0, 0, 2,  0, coeff), 3)
    b_sol = round(integral(b_a, b_b, 0, 2, 0, coeff), 3)
    c_sol = round(integral(c_a, c_b, 0, 2, 0, coeff), 3)
    d_sol = round(integral(0, 4, 0, 2, 0, coeff), 3)
    solns = [ a_sol, b_sol, c_sol, d_sol ]

    print_solns(solns)

def checkout():
    check_red, check_func = parse_numbers('checkout')

    coeff, a, b = check_func[1][:]

    a_sol = (coeff/25) * (1**2)
    b_sol = a_sol - ((coeff/25) * (0.5**2))
    c_sol = 1 - ((coeff/25) * (0.5**2))
    d_sol = round(sqrt( (0.5 * 25) / coeff ), 3)
    e_sol = 'x * ' + str(Fraction(coeff * 2 / 25).limit_denominator())
    f_sol = round(integral(a, b, (coeff * 2/25), 2, 0, 0), 3)
    h_sol = round(integral(a, b, (coeff * 2/25), 3,  0, 0), 3)

    g_var = round(h_sol - (f_sol ** 2), 3)
    g_dev = round(sqrt(g_var), 3)
    g_sol = { 'V(X)' : g_var, 'sigma(X)' : g_dev }

    solns = [ a_sol, b_sol, c_sol, d_sol, e_sol, f_sol, g_sol, h_sol ]
    print_solns(solns)

    print('checkout')

def weight():

    weight_red, weight_func = parse_numbers('weight')

    weight, a, b = weight_func[0][:]

    u_a = a - weight
    u_b = b - weight

    temp = integral(u_a, u_b, -1, 2, 0, 1)
    a_sol = round(1 / temp, 3)

    b_1 = (-1 * a_sol) * integral(0, u_b, 1, 2, 0, 0)
    b_2 = (a_sol) * integral(weight, b, 0, 0, 0, 1)
    b_sol = round(b_1 + b_2, 3)

    u_a = (weight - 0.25) - weight
    u_b = (weight + 0.25) - weight

    c_sol = round(a_sol * integral(u_a, u_b, -1, 2, 0, 1), 3)

    u_a = (weight - 0.5) - weight
    u_b = (weight + 0.5) - weight

    d_sol = round(1 - (a_sol * integral(u_a, u_b, -1, 2, 0, 1)), 3)

    solns = [ a_sol, b_sol, c_sol, d_sol ]

    print_solns(solns)

def measurement():

    msmt_red, msmt_func = parse_numbers('measurement')

    k, n, a, b = msmt_func[0][:]

    a_sol = 'aint nobody got time to draw graphs'
    b_sol = round(k * integral(0, b, -1, 2, 0, n), 3)
    c_sol = round(k * integral(-1, 1, -1, 2, 0, n), 3)
    d_sol = round(1 - (k * integral(-0.5, 0.5, -1, 2, 0, n)), 3)
    solns = [ a_sol, b_sol, c_sol, d_sol ]

    print_solns(solns)

def ecologist():

    eco_red, eco_func = parse_numbers('ecologist')
    radius = eco_red[0]
    k, n, a, b = eco_func[0][:]

    i = n ** 2
    j = (-1 * n) - n

    ans, err = quad(derpegrand, a, b, args=(-1, (-1) * j, 1-i))
    a_sol = round(k * ans * pi, 2)
    solns = [ a_sol ]

    print_solns(solns)

def laser():

    laser_red, laser_func = parse_numbers('laser')
    i, j, k, a, b = laser_func[1][:]

    f = lambda x : i + j * ((k * x) - ((x ** 3) / 3))

    a_sol = round(f(0), 4)
    b_sol = round(f(1) - f(-1), 4)
    c_sol = round(1 - f(0.5), 4)
    d_sol = str(str(j) + ' * (' + str(k) + '-' + 'x^2)')
    solns = [ a_sol, b_sol, c_sol, d_sol ]

    print_solns(solns)

def lecture():
    lec_red, lec_func = parse_numbers('lecture')

    a_sol = 0.375
    b_sol = 0.125
    c_sol = 0.2969
    d_sol = 0.5781
    solns = [ a_sol, b_sol, c_sol, d_sol ]

    print_solns(solns)


def headway():
    head_red, head_func = parse_numbers('headway')
    power, i = head_func[0][:]

    a_sol = (-1 * power) - 1
    b_sol = { str(str(1) + ' - x^(-' + str(a_sol) + ')') : 'x > 1',
              str(0) : 'x <= 1'
            }

    f = lambda x : 1 - (x ** (-1 * a_sol))
    c_sol = round(f(3) - f(2), 3)

    d_expected = round(integral(1, np.inf, a_sol, power+1, 0, 0), 3)
    d_exp_sqrd = integral(1, np.inf, a_sol, power+2, 0, 0)
    d_std_dev = round(sqrt(d_exp_sqrd - (d_expected ** 2)), 3)
    d_sol = { 'E(x)' : d_expected, 'sigma(x)' : d_std_dev }

    e_sol = round(f(d_expected + d_std_dev), 4)
    solns = [ a_sol, b_sol, c_sol, d_sol, e_sol]

    print_solns(solns)

def propane():
    prop_red, prop_func = parse_numbers('propane')

    a_sol = '3x + (4/x) - 7'
    b_sol = 1.729
    c_exp = 1.727
    c_var = 0.016
    c_sol = { 'E(X)' : c_exp, 'V(X)' : c_var }
    d_sol = 0

    solns = [ a_sol, b_sol, c_sol, d_sol ]

    print_solns(solns)

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

def derpegrand(x, a, b, c):
    return a * (x**4) + b * (x**3) + c * (x**2)

def integrand(x, a, power, b, c):
    return a * (x**power) + b * x + c

def integral(lower, upper, a, power, b, c):
    ans, err = quad(integrand, lower, upper, args=(a, power,  b, c))
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
