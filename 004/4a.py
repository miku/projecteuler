#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# 1) Corollary: The product of two 3-digit numbers is at most 6-digits long.
#
# 2) The number of palindromes is really the number of 3 digit permutations.
#		number of candidates = 10^10^10 = 1000 
# 
# 3) For each 3-digit number, generate the approriate 6-digit palindrome,
#		then for each three digit number (100 -- 999) try to divide it until
#		division has no remainder

import itertools

three_digits = sorted([ j for j in 
	[ ''.join(map(str, i)) for i in 
		itertools.product(range(10), repeat=3) ] if int(j) > 99], reverse=True)

for number in three_digits:
	six_digit = '%s%s' % (number, number[::-1])
	for factor in map(int, three_digits):
		if int(six_digit) % factor == 0:
			other = int(six_digit) / factor
			if len(str(other)) < 4:
				print int(six_digit), factor, other
