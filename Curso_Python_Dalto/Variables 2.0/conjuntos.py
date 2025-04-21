#Creando un conjunto con (set)
conjunto = set(["Dato 1","Dato 2"])

#Creando un conjunto dentro de otro
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}
print (conjunto2)

#Teoría de Conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

#Verificando si conjunto1 es un subconjunto de conjunto2
resultado = conjunto1.issubset(conjunto2)
resultado = conjunto2 <= conjunto1 #Segunda manera. Comentamos la primera para que ejecute el print()

#Verificando si conjunto1 es un superconjunto de conjunto2
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto2 > conjunto1 #Tiene que ser mayor o igual que

#Verificar si hay algun conjunto en común
resultado = conjunto2.isdisjoint(conjunto1)
print (resultado)