#First lesson, basic type of operators and variables

#Python is object oriented so each var is an object

# There are different types of numbers: integers, float numbers and complex number 
#There are String types
#logic types: booleans(true or false), & !=
#special operators (is,in,not in, is not)

variable="Im a variable"
print(type(variable))#to know what type is the var

#A variable is space of the memory of the computer with value that could change in the program thats why the name

operadores="These are the results of operations: "
print(10%3,10**2,9//2)
#modulo, potency and natural split
#the type is defined by the content of the same so its not like java

menssage="""Aqui hay algunos
...saltos 
...de linea"""
print(menssage)


print(variable)
a=0
for i in range (100):
    a+=2
print(a)

#Functions are a group of code that could make a task or a group of them and
#Functions could return values, have parameters and arguments
#Are also call methods that may belong to a class
# Utilities: code optimization, 
#BASIC SINTAX:
 #def function():#parameter zones(optional)
 #instructions and returned values(optional)
#There are default options that cames with python and then our define funtions 
def mensaje():#this is the set of the function
    print("This line is going to appear 5 times")#this is the body of the function

#There is an example of a simple loop using a function inside 
o=0
while o!=5:
    mensaje()#this is the call of the function
    o+=1



