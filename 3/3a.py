#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600 851 475 143 ?
"""

import math, json

def gen_primes(n):
	primes = [2]
	for i in range(3, n):
		prime = True
		for p in primes:
			if i % p == 0:
				prime = False
				break
		if prime:
			primes.append(i)
	return primes

limit = int(math.sqrt(600851475143)) + 1
handle = open('primes_upto_%s.json' % limit, 'w')
primes = gen_primes(limit)
handle.write(json.dumps(primes))
handle.close()
