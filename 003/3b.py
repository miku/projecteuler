#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import sys

def primes_up_to(n): 
	if n == 2:
		return [2]
	elif n < 2:
		return []
	s = range(3, n + 1, 2)
	mroot = n ** 0.5
	half = (n + 1) / 2 - 1
	i, m = 0, 3
	while m <= mroot:
		if s[i]:
			j = (m * m - 3) / 2
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i + 1
		m = 2 * i + 3
	return [2] + [x for x in s if x]

if __name__ == '__main__':
	number = 600851475143
	try:
		number = int(sys.argv[1])
	except IndexError:
		pass
	except ValueError:
		pass

	print 'Prime factors of', number

	root = int(number ** 0.53)
	primes = primes_up_to(root)
	rest = number
	factors = []
	while rest > 1:
		if rest in primes:
			factors.append(rest)
			rest = -1
			break
		for p in primes:
			if rest % p == 0:
				rest = rest / p
				factors.append(p)
				break
		if not factors:
			print number, "appears to be a prime"
			break

	if factors:
		print factors, 'Largest prime factor:', max(factors)
	