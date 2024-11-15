#tuples inmutable list like fixed list
#It is possible to make list or tuples from one another tuple
#No index allow, it is posible to check if there is an element
#ADVANTAGES: The runtime is faster than the list, optimize space, format strings, there are possible to use like a key in data dictionay

miTupla=("David",12,True,19.4)
miLista=list(miTupla)#Tuple can be convert in a list throuhgt the function
print(miTupla[:])
print(miLista[:])
laTupla=tuple(miLista)

print(laTupla[:])#A list can also change to a Tuple
print("David" in laTupla)#now Check there are the same values
print(laTupla.count(12),len(miTupla))

#Unit tuple, decoup only one element
unitTupla=("Rey")
sinParentesis="noche",67,"perro"#A tuple could be set without param

dia, numero, animal=sinParentesis#A group of variables could be insert the values of a tuple just simply by defining and equalizing
print(numero,animal,dia)
