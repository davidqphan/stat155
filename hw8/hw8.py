#!/usr/bin/env python3
import sys
import json
from pprint import pprint
from math import pi, sqrt
from fractions import Fraction
import os.path
import statistics as stats
import scipy.stats as scistats
import scipy.misc as scimisc
import scipy.special as scsp
import numpy as np
from scipy.integrate import quad
from collections import OrderedDict

def drawing():
    drawing_red = parse_numbers('drawing')

    a, b, c, d1, d2, e, f, g, h, i = drawing_red[:]

    a_sol = z_to_p(a) - z_to_p(0)
    b_sol = z_to_p(b) - z_to_p(0)
    c_sol = z_to_p(0) - z_to_p(c)
    d_sol = z_to_p(d2) - z_to_p(d1)
    e_sol = z_to_p(e)
    f_sol = 1 - z_to_p(f)
    g_sol = z_to_p(2) - z_to_p(g)
    h_sol = z_to_p(2.5) - z_to_p(h)
    i_sol = 1 - z_to_p(i)
    j_sol = z_to_p(2.5) - z_to_p(-2.5)
    solns = [ a_sol, b_sol, c_sol, d_sol, e_sol, f_sol, g_sol, h_sol, i_sol,
            j_sol]

    solns = round_list(solns, 4)
    print_solns(solns)

def constant_c():
    constc_red = parse_numbers('constant_c')

    a, b, c, d, e = constc_red[:]

    a_sol = round(scistats.norm.ppf(a), 2)
    b_sol = round(scistats.norm.ppf(0.5 + b), 2)
    c_sol = round(scistats.norm.ppf(1 - c), 2)
    d_sol = round(-1 * scistats.norm.ppf((1-d) * 0.5), 2)
    e_sol = round(-1 * scistats.norm.ppf(e * 0.5), 2 )
    solns = [ a_sol, b_sol, c_sol, d_sol, e_sol ]

    print_solns(solns)

def yield_strength():
    yield_red = parse_numbers('yield_strength')

    mu, sigma = yield_red[:]

    a1_sol = round(z_to_p((40-mu)/sigma), 4)
    a2_sol = round(1 - z_to_p((60-mu)/sigma), 4)
    b_sol = round(mu + (-0.67) * (sigma), 4)
    solns = [ a1_sol, a2_sol, b_sol ]

    print_solns(solns)

def force():
    force_red = parse_numbers('force')

    mean, std_dev, c = force_red[:]

    a_sol = round(z_to_p((18-mean)/std_dev), 4)
    b_sol = round(z_to_p((12-mean)/std_dev) - z_to_p((10-mean)/std_dev), 4)
    k = 1.5 * std_dev
    c1 = z_to_p(((mean + k) - mean) / std_dev)
    c2 = z_to_p(((mean - k) - mean) / std_dev)
    c_sol = round(c1 - c2, 4)

    solns = [ a_sol, b_sol, c_sol ]

    print_solns(solns)

def z_alpha():
    z_red = parse_numbers('z_alpha')

    a, b, c = z_red[:]

    a_sol = round(scistats.norm.ppf(1-a), 2)
    b_sol = round(scistats.norm.ppf(1-b), 2)
    c_sol = round(scistats.norm.ppf(1-c), 2)
    solns = [ a_sol, b_sol, c_sol]

    print_solns(solns)

def rockwell():
    rock_red = parse_numbers('rockwell')

    mean, b1, b2, d1, d2 = rock_red[:]

    a1 = round(z_to_p(round((67-mean)/3, 2)), 4)
    a2 = round(z_to_p(round((75-mean)/3, 2)), 4)
    a_sol = round(a2 - a1, 4)

    b_sol = 5.88
    c_sol = round(10 * a_sol, 4)

    d1 = round(z_to_p((d1-mean)/3), 4)
    d_sol = round(scistats.binom.cdf(8, 10, d1), 4)

    solns = [ a_sol, b_sol, c_sol, d_sol ]
    print_solns(solns)

def temperature():
    temp_red = parse_numbers('temperature')

    sigma = temp_red[0]

    a_sol = round(sigma / 1.96, 4)
    solns = [ a_sol ]
    print_solns(solns)

def standardize():
    std_red = parse_numbers('standardize')

    mean, std_dev, a, b, c1, c2, d, e1, e2, f1, f2 = std_red[:]

    a_sol = round(z_to_p((a-mean)/std_dev), 4)
    b_sol = round(z_to_p((b-mean)/std_dev), 4)
    c_sol = round(z_to_p((c2-mean)/std_dev), 4) - round(z_to_p((c1-mean)/std_dev), 4)
    d_sol = 1 - round(z_to_p((d-mean)/std_dev), 4)
    e_sol = round(z_to_p((e2-mean)/std_dev), 4) - round(z_to_p((e1-mean)/std_dev), 4)
    f_sol = round(z_to_p(((f2+f1)-mean)/std_dev), 4) - round(z_to_p(((-f2+f1)-mean)/std_dev), 4)
    solns = [ a_sol, b_sol, c_sol, d_sol, e_sol, f_sol ]
    solns = round_list(solns, 4)
    print_solns(solns)

def cargo():
    cargo_red = parse_numbers('cargo')

    meter, mean, std_dev = cargo_red[:]

    a1 = round((100-mean)/std_dev, 2)
    a = round(z_to_p(a1), 4)
    a2 = 1 - a

    a_sol = round(1 - (a2 ** 5), 4)
    solns = [ a_sol ]
    print_solns(solns)

def steel():
    steel_red = parse_numbers('steel')

    steel = steel_red[0]

    n = 200
    np = n * steel
    npq = n * steel * (1-steel)

    a_sol = round(z_to_p((30 + 0.5 - np)/sqrt(npq)), 4)
    b_sol = round(z_to_p((29 + 0.5 - np)/sqrt(npq)), 4)
    c_sol = (z_to_p((25 + 0.5 - np)/sqrt(npq))) - (z_to_p((14 + 0.5 - np)/sqrt(npq)))
    c_sol = round(c_sol, 4)
    solns = [ a_sol, b_sol, c_sol ]
    print_solns(solns)

def print_solns(solutions):
    d = map_sol(solutions)

    for part in d:
        print('part {}: {}\n'.format(part, d[part]))

def map_sol(solutions):
    parts = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]

    d = OrderedDict()

    for part, sol in zip(parts, solutions):
        d[part] = sol

    return d

def round_list(lst, decimal_place):
    return [ round(num, decimal_place) for num in lst ]

def z_to_p(z):
    return 0.5 * (1 + scsp.erf(z / np.sqrt(2)))

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
    red_lst = parse(reds)

    return red_lst

def parse(nums):
    return [ float(num) for num in nums ]

def parse_object(obj):
    pasta_json = parse_json()
    return pasta_json[obj]

def parse_json():
    with open('pasta.json') as f:
        pasta = json.load(f, object_pairs_hook=OrderedDict)
    return pasta

user_options = [ 'drawing', 'constant_c', 'yield_strength', 'force', 'z_alpha',
                 'rockwell', 'temperature', 'standardize', 'cargo', 'steel'
               ]

options = { 1 : drawing, 2 : constant_c, 3 : yield_strength, 4 : force, 5 : z_alpha,
            6 : rockwell, 7 : temperature, 8 : standardize, 9 : cargo, 10 : steel
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
