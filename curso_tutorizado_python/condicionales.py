#An execution flow in a programe in the order for wich instruction are in
#Conditionals work as intruction flow manager 
#A conditional contain a block of code that will check if some condition happend to choose wich one run or not, to continue executing
print("Programa de evaluación de Notas:")
notaAlumno=input("Introduce tu nota: ")#This variable will receive a value by console, just intput will be consider as a String
def evaluar(nota):#An example using a function that check if the condition happend and depend the note the value of the value returned will be different
    valoracion="aprobado"
    if nota <5:
        valoracion="suspenso"
    return valoracion
#variable nota is only able to handle in his ambito, in his block or function therefore that variable only make sense in his ambito

    # print(evaluar(int(notaAlumno)))#Class integer to trasform the input into str to int