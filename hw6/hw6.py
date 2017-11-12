#!/usr/bin/env python3
import sys
from math import sqrt
from fractions import Fraction
import os.path
import statistics as stats
import scipy.stats as scistats
import scipy.misc as scimisc

cwd = os.getcwd()

def binomials():
    with open(cwd+'/binomials.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    a_x, a_n, a_p = numlst[0:3]
    b_x, b_n, b_p = numlst[3:6]
    c_n, c_p = numlst[6:8]
    d_n, d_p = numlst[8:10]

    print('part a: ')
    a_binom_prob = scistats.binom.pmf(a_x, a_n, a_p)
    print('b({0:0.0f}; {1:0.0f}, {2:0.2f}) = {3:0.4f}\n'.format(a_x, a_n, a_p,
        a_binom_prob))

    print('part b: ')
    b_binom_prob = scistats.binom.pmf(b_x, b_n, b_p)
    print('b({0:0.0f}; {1:0.0f}, {2:0.2f}) = {3:0.4f}\n'.format(b_x, b_n, b_p,
        b_binom_prob))

    print('part c: ')
    c_prob = 0
    for i in range(3, 6):
        c_prob += scistats.binom.pmf(i, c_n, c_p)
    print('P(3 <= X <= 5) = {0:0.4f}\n'.format(c_prob))

    print('part d: ')
    d_prob = 1 - scistats.binom.pmf(0, d_n, d_p)
    print('P(1 <= X) = {0:0.4f}\n'.format(d_prob))

def circuits():
    with open(cwd+'/circuits.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    n, p = numlst[0:2]
    print('part a: ')
    a_prob = scistats.binom.cdf(2, n, p)
    print('P(X <= 2) = {0:0.4f}\n'.format(a_prob))

    print('part b: ')
    b_prob = 1 - scistats.binom.cdf(4, n, p)
    print('P(X >= 5) = {0:0.4f}\n'.format(b_prob))

    print('part c: ')
    c_prob = scistats.binom.cdf(4, n, p) - scistats.binom.cdf(0, n, p)
    print('P(1 <= X <= 4) = {0:0.4f}\n'.format(c_prob))

    print('part d: ')
    d_prob = scistats.binom.cdf(0, n, p)
    print('P(X = 0) = {0:0.4f}\n'.format(d_prob))

    print('part e: ')
    expected = n * p
    std_dev = sqrt(expected * (1-p))
    print('E(X) = {0:0.4f}\n'.format(expected))
    print('sigma(X) = {0:0.4f}\n'.format(std_dev))


def tornadoes():
    with open(cwd+'/tornadoes.txt') as f:
        nums = list(f.read().split())

    poisson = float(nums[0])

    print('part a: ')
    a_prob = scistats.poisson.cdf(5, poisson)
    print('P(X <= 5) = {0:0.4f}\n'.format(a_prob))

    print('part b: ')
    b_prob = scistats.poisson.cdf(9, poisson) - scistats.poisson.cdf(5, poisson)
    print('P(6 <= X <= 9) = {0:0.4f}\n'.format(b_prob))

    print('part c: ')
    c_prob = 1 - scistats.poisson.cdf(9, poisson)
    print('P(10 <= X) = {0:0.4f}\n'.format(c_prob))

    print('part d: ')
    d_std_dev = sqrt(poisson)
    d_prob = 1 - scistats.poisson.cdf(poisson+d_std_dev, poisson)
    print('{0:0.4f}\n'.format(d_prob))

def boiler():
    with open(cwd+'/boiler.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    poisson = numlst[0]
    a_x = numlst[1]
    b_x = numlst[2]
    c_x = numlst[3]
    d_x1, d_x2 = numlst[4:6]
    e_x1, e_x2 = numlst[6:8]

    print('part a: ')
    a_prob = scistats.poisson.cdf(a_x, poisson)
    print('P(X <= {0:0.0f}) = {1:0.4f}\n'.format(a_x , a_prob))

    print('part b: ')
    b_prob = scistats.poisson.pmf(b_x, poisson)
    print('P(X = {0:0.0f}) = {1:0.4f}\n'.format(b_x , b_prob))

    print('part c: ')
    c_prob = 1 - scistats.poisson.cdf(c_x-1, poisson)
    print('P({0:0.0f} <= X) = {1:0.4f}\n'.format(c_x , c_prob))

    print('part d: ')
    d_prob = scistats.poisson.cdf(d_x2, poisson) - scistats.poisson.cdf(d_x1-1,
            poisson)
    print('P({0:0.0f} <= X <= {1:0.0f}) = {2:0.4f}\n'.format(d_x1, d_x2, d_prob))

    print('part e: ')
    e_prob = scistats.poisson.cdf(e_x2-1, poisson) - scistats.poisson.cdf(e_x1,
            poisson)
    print('P({0:0.0f} < X < {1:0.0f}) = {2:0.4f}\n'.format(e_x1, e_x2, e_prob))

def camera():
    with open(cwd+'/camera.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    N, M, n = numlst[0:3]

    print('part a: ')
    print('Distribution: hypergeometric\n')
    print('N = {0:0.0f}, M = {1:0.0f}, n = {2:0.0f}'.format(N, M, n))

    print('part b: ')
    b_prob = scistats.hypergeom.pmf(2, N, n, M)
    b_frac = str(Fraction(b_prob).limit_denominator())
    print('P(X = 2) = {}\n'.format(b_frac))

    print('part c: ')
    c_prob = scistats.hypergeom.cdf(2, N, n, M)
    c_frac = str(Fraction(c_prob).limit_denominator())
    print('P(X <= 2) = {}\n'.format(c_frac))

    print('part d: ')
    d_prob = 1 - scistats.hypergeom.cdf(1, N, n, M)
    d_frac = str(Fraction(d_prob).limit_denominator())
    print('P(X >= 2) = {}\n'.format(d_frac))

    print('part e: ')
    expected = n * (M / N)
    std_dev = scistats.hypergeom.std(N, n, M)
    print('E(X) = {0:0.04f}\n'.format(expected))
    print('sigma(X) = {0:0.04f}\n'.format(std_dev))

def emergency():
    with open(cwd+'/emergency.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    poisson, rate = numlst[0:2]

    print('part a: ')
    a_prob = scistats.poisson.pmf(4, poisson)
    print('P(X = 4) = {0:0.04f}\n'.format(a_prob))

    print('part b: ')
    b_prob = 1 - scistats.poisson.cdf(3, poisson)
    print('P(X >= 4) = {0:0.04f}\n'.format(b_prob))

    print('part c: ')
    c_prob = poisson * (rate / 60)
    print('{0:0.04f}\n'.format(c_prob))

def pulse():
    with open(cwd+'/pulse.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    poisson = numlst[0]

    print('part a: ')
    a_prob = scistats.poisson.pmf(1, poisson)
    print('P(X = 1) = {0:0.04f}\n'.format(a_prob))

    print('part b: ')
    b_prob = 1 - scistats.poisson.cdf(1, poisson)
    print('P(X >= 2) = {0:0.04f}\n'.format(b_prob))

    print('part c: ')
    c_prob = scistats.poisson.pmf(0, poisson) ** 2
    print('P(neither) = {0:0.04f}\n'.format(c_prob))

def children():

    prob_b = 0.5
    prob_g = 0.5

    prob_3 = 2 * (prob_b ** 3)
    prob_4 = 2 * scimisc.comb(3, 2) * (prob_b ** 4)
    prob_5 = 1 - prob_3 - prob_4

    x_dict = { 0 : 0,
               1 : 0,
               2 : 0,
               3 : prob_3,
               4 : prob_4,
               5 : prob_5,
               6 : 0
             }
    print(x_dict)


def diodes():
    with open(cwd+'/diodes.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    p, n = numlst[0], numlst[1]

    print('part a: ')
    expected = n * p
    std_dev = sqrt(expected * (1-p))
    print('E(X) = {0:0.04f}\n'.format(expected))
    print('sigma(X) = {0:0.04f}\n'.format(std_dev))

    print('part b: ')
    b_prob = 1 - scistats.poisson.cdf(3, expected)
    print('P(X >= 4) = {0:0.04f}\n'.format(b_prob))

    print('part c: ')
    c_prob = scistats.poisson.pmf(0, expected)

    c_n = 5

    c_probb = scistats.binom.pmf(4, c_n, c_prob) + scistats.binom.pmf(5, c_n,
            c_prob)

    print('P(all diodes) = {0:0.04f}\n'.format(c_probb))

def interview():
    with open(cwd+'/interview.txt') as f:
        nums = f.read().split()

    numlst = list(float(num) for num in nums)

    N, n, M = numlst[0:3]

    print('part a: ')
    print('h(x, {0:0.0f}, {1:0.0f}, {2:0.0f})\n'.format(M, n, N))

    print('part b: ')
    expected = n * (M / N)
    print('E(X) = {0:0.04f}\n'.format(expected))

user_options = [ 'binomials',
                 'circuits',
                 'tornadoes',
                 'boiler',
                 'camera',
                 'emergency',
                 'pulse',
                 'children',
                 'diodes',
                 'interview'
               ]

options = { 1 : binomials,
            2 : circuits,
            3 : tornadoes,
            4 : boiler,
            5 : camera,
            6 : emergency,
            7 : pulse,
            8 : children,
            9 : diodes,
            10 : interview
          }

def main():

    while True:
        print('Select an option:\n')

        for i, option in enumerate(user_options):
            print('   {}.  {}'.format(i+1, option))
        print('   ')

        try:
            sel = input()
            break
        except KeyboardInterrupt:
            print('\nBye Felicia!')
            quit()

    options[int(sel)]()

if __name__ == "__main__":
    main()
