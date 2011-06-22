#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms. 
"""

CACHE = {1 : 1, 2 : 2}

def rfib(n):
	""" Recursive fib. """
	if n in CACHE:
		return CACHE[n]
	if n < 2: 
		return 1
	else:
		CACHE[n] = rfib(n - 1) + rfib(n - 2)
		return CACHE[n]

def ifib(n):
	""" Iterative (dynamic) fib. """	
	for i in range(3, n + 1):
		CACHE[i] = CACHE[i - 1] + CACHE[i - 2] 
	return CACHE[n]

def fib_below(m):
	i = 1
	f = ifib(i)
	while f < m:
		i += 1
		f = ifib(i)
	return i - 1

last, sum_of_evens = fib_below(4000000), 0
for i in range(1, last + 1):
	if CACHE[i] % 2 == 0:
		sum_of_evens += CACHE[i]

print sum_of_evens
# You are the 124398th person to have solved this problem.