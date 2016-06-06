#! /bin/bash
# isPrime.sh
# Authored by John Pellman
# Birthday: April 8th, 2014
# Last Revision: April 8th, 2014

# Defines a shell function that will take in a value and determine if it is prime.

function isprime {
	# Integrity checks on number of arguments.
	if [  $# -eq 0 ]; then
		echo "Error: No arguments were provided.  This function requires one integer argument."
		return	
	elif [ ! $# -eq 1 ]; then
		echo "Error: More than one argument provided.  This function requires one integer argument."
		return
	fi
	# Rains rage upon the silly earthling if a string is passed in.
	if [ $(( $1 + 1 )) -eq 1 ]; then
		echo "Error: Either a string or 0 was entered.  Neither a string nor zero can be prime."
		return
	fi
	# Determines the primehood using a loop.
	divisor=$(( $1 - 1 ))
	primeTruth=1
	while [ $primeTruth -eq 1 ]; do
		if [ $divisor -eq 1 ]; then 
			break
		fi
		if [ $(expr $1 % $divisor) -eq 0 ]; then
			primeTruth=0
		fi
		divisor=$(( $divisor - 1 ))
	done
	if [ $primeTruth -eq 1 ]; then
		echo "PRIME"
	else
		echo "NOT PRIME"
	fi
}

isprime 13
isprime 4
