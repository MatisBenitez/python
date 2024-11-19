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
    
#Ejercicio 1 Condicionales:(Aplicacion que devuelve el numero mas alto)

num1=int(input("Introduce un numero:"))
num2=int(input("Introduce otro numero:"))

def devuelveNumero(num1,num2):
    mens="El mayor es:"
    if num1>num2:
        print(mens)
        print(num1)
        
    elif num1<num2:
        print(mens)
        print(num2)
    else:
        print("Son iguales")


devuelveNumero(num1,num2)

#Ejercicio 2
nombre=input("Introduce nombre:")
direccion=input("Introduce direccion:")
telefono=input("Introduce un telefono:")

cliente=[nombre,direccion,telefono]

print("Los datos personales son: "+cliente[0]+" "+cliente[1]+" "+cliente[2])





















#Ejercicio 3

numero1=int(input("Introduce un primer numero para media:"))
numero2=int(input("Introduce un segundo numero para media:"))
numero3=int(input("Introduce un tercer numero para media:"))
def devuelveMedia(num1,num2,num3):
    print("La media es:")
    print((num1+num2+num3)/3)

devuelveMedia(numero1,numero2,numero3)

