#Dictionaries, are a characteristic data structure associate with key value for each element store
#Each value inside has a unique key, 
#inside could be list, tuples or even another dictionarie

miDiccionario={"Espagna":"Madrid","Fracia":"París","Inglaterra":"Londres","Sri Lanka":"Colombo"}
miDiccionario["Portugal"]="Ljubliana"
print(miDiccionario["Portugal"])
miDiccionario["Portugal"]="Lisboa"
print(miDiccionario["Portugal"])
print(miDiccionario["Espagna"])#That will show the value assign to his key
#del miDiccionario["Francia"]#To delete an element
 
 #A tuple could be use to asign values to a dicctionarie then assign a dictionary with a key/value

miTupla=["España","Portugal","Italia","Francia"]
miDiccionario={miTupla[0]:"Valencia"}
print(miDiccionario["España"])

basketDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[91,92,93,96,97,98]}
print(basketDiccionario["Anillos"])

#See values and the keys
print(basketDiccionario.keys())
print(basketDiccionario.values())
print(len(basketDiccionario))