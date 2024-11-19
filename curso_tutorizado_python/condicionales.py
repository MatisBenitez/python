#An execution flow in a programe in the order for which instruction are in
#Conditionals work as intruction flow manager 
#A conditional contain a block of code that will check if some condition happend to choose wich one run or not, to continue executing
print("Programa de evaluación de Notas:")
notaAlumno=int(input("Introduce tu nota: "))#This variable will receive a value by console, just intput will be consider as a String
def evaluar(nota):#An example using a function that check if the cndition happend and depend the note the value of the value returned will be different
    valoracion="nota"
    if nota<5:
        print("InSuficiente")
    elif nota<6:
        print("Suficiente")
    elif nota<8:
            print("Bien")
    elif nota<9:
        print("Notable")
    else:
        print("Sobresaliente")
 
evaluar(notaAlumno)
#variable nota is only able to handle in his ambito, in his block or function therefore that variable only make sense in his ambito

    # print(evaluar(int(notaAlumno)))#Class integer to trasform the input into str to int

edad=int(input("Cual es tu edad:"))
def checkEdad(age):
    mensaje="La edad"
    if 18>age:
        print("No puedes pasar")
    elif age>100:
        print("La edad no es valida")
    else:
        print("puedes pasar")
    

checkEdad(edad)

#In python doesn't exist a switch instruction like conditional so it's  possible to do with if 
#Python offer logic operator and, or, in, join of differents conditional structures


