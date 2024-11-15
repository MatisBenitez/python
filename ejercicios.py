#Exercise 1: FizzBuzz Game
# a program that prints the numbers from 1 to 100.
#  But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz".
#  For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# Using a loop and a modulo % to check divisibility

#first a fuction to check if which number should be called fizz or buzz
def divisores(num):
    if num%3==0 and num%5==0:
        print("FizzBuzz")

    elif num%3==0:
        print("Fizz")

    elif  num%5==0:
        print("Buzz")

    else:
        print(num)

a=0
while a!=100:
    a+=1
    divisores(a)
    

