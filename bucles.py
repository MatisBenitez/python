#Loops are usefull when is needed to repeat multiple times some blocks of code, functions, ...etc whithout having heavy unefficiency code
#In loops there could be a condition to set how many times an action has to be done. For example in a login page if the dates are incorrect it will be need to refresch and run again the same structure

#Types of loops as flow handle code: defined:These are previous set the times that the code should repeat;  undefined: has a certain condition(could happend or not)that set the times the has to still going it could be infinitive.

for i in [10,7,5]:#For each element(not number) will print a the element, as many times are given
    i*=10
    print(i)

#Get throught an string is usefull to check if dates are correct, commonly use in logins, verify password etc

email=False
miCorreo=input("Introduce tu email:")
for i in miCorreo:
    if(i=="@"):#With only = is for setting, == is for compare
        email=True
    
if email==True:
    print("El email es correcto")
else:
    print("El email es incorrecto")


#for i in"LetraALetra":
#    print(i, end=",")
#Range type allow to use "for" loop with a numeric counter like other languages:java... 





#Special notations with print

for i in "cero":#As many times as character are in the string
    print("Hola", end=" ")#End instruction keep the content show in the same line




