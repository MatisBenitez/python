"""""
edad=99

if  edad<100 and 0<edad:#Also could work 0<edad<100
    print("Edad correcta")
else:
    print("Edad incorrecta")

#Examples of priority evaluators ins conditionals structures

salarioPresidente=int(input("Introduce el salario del presidente"))
print("Salario presidente: "+str(salarioPresidente))

salarioDirector=int(input("Introduce el salario del presidente"))
print("Salario presidente: "+str(salarioDirector))

salarioAdministrativos=int(input("Introduce el salario del presidente"))
print("Salario presidente: "+str(salarioAdministrativos))

if salarioAdministrativos<salarioDirector<salarioPresidente:#Concat comparation operators
    print("Funciona correctamente")
else:
    print("Algo falla en la empresa")
"""

#logic operator: and,or 

#Ejemplo evaluador de becas, there are multiple combination and concat of operantors
print("Programa becas 2024")
distanciaEscuela=int(input("Introduce la distancia a la escuela en km:"))
print(distanciaEscuela)
numeroHermanos=int(input("Numero de hermanos:"))
print(numeroHermanos)
salarioFamiliar=int(input("Introduce el salario familiar anual:"))
print(salarioFamiliar)

if distanciaEscuela>40 or numeroHermanos>2 and salarioFamiliar<=20000:
    print("El estudiante tiene derecho a beca")
else:
    print("No tiene derecho a beca")


#Uses of the logic operator: or

print("Asignaturas optativas:")
print("Informatica gráfica-Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida:")#Python is case sensitive language so it's important to know or then asumme and change it

asignatura=opcion.lower()#It change the char to minus

if asignatura in ("informática gráfica","pruebas de software","usabilidad y accesibilidad"):
    print("Asignatura elegida: "+asignatura.upper())
else:
    print("La asinatura "+asignatura+" no esta comtemplada")

