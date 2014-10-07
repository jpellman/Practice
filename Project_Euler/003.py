#! /usr/bin/env python

# Largest Prime Factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# John Pellman, October 6th 2014

'''
 First, find all the prime factors of 600851475143 and store them in a list.
 Accomplish this by determining a) all of the factors of 600851475143 and
 b) all of the prime values up until 600851475143.  Take the the intersection
 of a and b.  The last value of the list in the intersection is the largest
 prime factor. Computationally, this method will be horrid, but it's what
 I want to start with because my feeble human mind feels inclined towards it.
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
	
def primeValues(x):
	''' primeValues
	Arguments: 	x - An arbitrary integer.
	Returns:	A list containing all of the prime values up until x.
	'''
	return [1] + filter(isPrime, range(2,x+1))

def allFactors(x):
	''' allFactors
	Arguments:	x - An arbitrary integer.
	Returns:	A list containing all of the factors of x.
	'''
	def isFactor(y) : return x%y==0
	return filter(isFactor, range(1,x+1))

primevalues=set(primeValues(number))
allfactors=set(allFactors(number))
print max(primevalues & allfactors)

''' I will most likely take a shower while this is running because it will
take hell and half to finish executing. 

Actually, it seems that I have run into a memory error, so I will need to 
optimize it anyways.  Still taking a shower first though.''' 
