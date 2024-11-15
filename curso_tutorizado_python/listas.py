#The list in python are a structure that allow to reserve multiple space in memory for many values or even different types values
miLista=["Juan","Pepe","Antonio"]#an index are use to locate the position of each value

print(miLista[-3])#we could use a negative index, and that will be starting by the last of the list and so on until the first one
print(miLista[1:3])#to exclude elements
print(miLista[1:])#show the next ones starting by the postition before :

miLista.append("Samuel")#To add a value in list in the last position
miLista.insert(0,"Sara")#Add a value in some specific position given by the
miLista.extend(["Sandra","Ana","Lucia"])#Join an array with a another

print(miLista[:])
print(miLista.index("Juan"))#INDEX: Find the position of a value given

print("Juan" in miLista)# IN return a boolean and check in there is the value given in the list

laLista=["diverso",5,False,3.14]
print(laLista[2])

miLista.remove("Juan")#Delete the element given in a list
print("Juan" in miLista)#To check is there is still there

laLista.pop()#delete the last element of a list
print(laLista[:])

#to sum some differents  in another list

sumaLista=(miLista+laLista)*3 #It is possible to put a number at the end and multiply by the times of list 
print(sumaLista[:])

print(len(sumaLista))#Len, to count the element that are in the list

