# Author : Alex Muncer
# Date: 23/11/2021
# Universtiy of Hertfordfordshire SRN: 14152188
#
# This program takes any positive integer and continually calculates until it reaches 1, 
# if the value is even it will divide by 2, and if the value is odd it will multiply it by 3 and add 1.
#
# Parameter "n" of the function "collatzConjecture" is a integer inputed by the user.
# Variable "numOfCalcs" keeps track of how many calculations have taken place. 
# The program prints the result of each calculation.
# When the program reaches 1, it will print the total number of calculations performed and its operation time.
#
# e.g.  collatzConjecture(1)= 1. Collatz conjecture is complete, n = 1. Number of calculations performed to reach 1 = 0 .
#       collatzConjecture(0)= Invalid Input.
#       collatzConjecture(-1)= Invalid Input.
#       collatzConjecture(10)= 5.0
#                              16.0 
#                              8.0
#                              4.0
#                              2.0
#                              1.0
#                              Collatz conjecture is complete, n = 1. Number of calculations performed to reach 1 = 6 .
#                              Operation time in nanoseconds = 20474 .

import time

timeStart = time.perf_counter_ns() #Records time at start of the function.
def collatz_Conjecture(n: int): #Function is initilized and requires a integer data type.
    number_of_ops = 0 #This vairable keeps track of the amount of operations.
    if n <= 0: #Tests if the input is a positive integer.
        print ("Invalid Input.") #Error message if a negative integer/0 has been entered.
    else:
        while n > 1: #Ensures continual (loop) of calculations until it reaches a value of 1.
            if n % 2 == 0: #Assesses if the number is even by being divisable by 2 with no remainder.
                n = n / 2 #Divides value by 2 if even.
                number_of_ops = number_of_ops + 1 #Adds 1 to the calculation tracking variable.
                print(n) 
            else:
                n = n * 3 + 1 #Multiplies value by 3 and adds 1 if odd.
                number_of_ops = number_of_ops + 1 #Adds 1 to the calculation tracking variable.
                print(n)
        return print("Collatz conjecture is complete, n = 1. Number of elementary operations performed to reach 1 =",number_of_ops,".")

timeEnd = time.perf_counter_ns() #Records time at end of the function.

            
print("Enter Integer:") #Prompts user to input a integer.
collatz_Conjecture(int(input())) #Calls the function with the user's input for the parameter n.

print("Operation time in nanoseconds =",timeEnd - timeStart,".") #Prints the operation time.

