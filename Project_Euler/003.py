#! /usr/bin/env python

# Largest Prime Factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# John Pellman, October 6th 2014

'''
First, find the largest factor of the number.  Then, find the largest prime
number that is less than the number.  Compare the two.  If the factor is larger
than the prime, find the next largest factor and compare that to the prime.
If the prime is larger than the factor, find the next largest prime and
compare that to the factor.  When the factor and the prime are equal,
the largest prime factor is all that should remain.
'''

#number=13195
number=600851475143

def isPrime(x):
	''' isPrime
		Arguments:	x - An arbitrary integer.
		Returns:	A boolean indicating whether or not x is prime.	
	'''
	''' An especially computationally horrid method.  I should replace this
	with a Sieve of Eratosthenes but it is Monday evening. If it isn't
	obvious (it probably isn't) I just recycled this from one of my shell
	scripts.
	'''	
	divisor=x-1
	primeTruth=True
	while primeTruth:
		if divisor==1:
			break
		if x%divisor==0:
			primeTruth=False
		divisor=divisor-1
	return primeTruth	
	
def nextLargestPrime(currentPrime):
	''' primeValues
	Arguments:	currentPrime - The current large prime number under
			scrutiny.	
	Returns:	The next largest prime value below the orignal number
			that is less than currentPrime.	
	'''
	nextPrime=currentPrime-1
	while not isPrime(nextPrime):
		nextPrime=nextPrime-1
	return nextPrime

def nextLargestFactor(originalVal, currentFactor):
	''' nextLargestFactor
	Arguments:	originalVal - The original value of the number
			whose largest prime factor is to be determined.
			currentFactor - The current large factor under
			scrutiny.	
	Returns:	The next largest factor of originalVal that is less
			than currentFactor.	
	'''
	nextFactor=currentFactor-1
	while not originalVal%nextFactor==0:
		nextFactor=nextFactor-1
	return nextFactor

def largestPrimeFactor(x):
	''' largestPrimeFactor
	Arguments:	x - An arbitrary integer.
	Returns:	The largest prime factor of x.
	'''
	nextPrime=nextLargestPrime(x)
	nextFactor=nextLargestFactor(x,x)
	while nextFactor != nextPrime:
		if nextFactor>nextPrime:
			nextFactor=nextLargestFactor(x,nextFactor)
		elif nextPrime>nextFactor:
			nextPrime=nextLargestPrime(nextPrime)
	return nextFactor

print largestPrimeFactor(number)
