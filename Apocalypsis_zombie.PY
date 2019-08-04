print("EJERCICIO FINAL")

print("CASO 0")

armas = ['pistola','escopeta']

cargadores = {
    'pistola': [10, 10], 
    'escopeta': [2, 2, 2, 2, 2]
}

suma = sum(cargadores["pistola"]) + sum(cargadores["escopeta"])


print(str("puedes matar a"),suma, str("zombies"))

print("CASO 1")

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4]
}

suma1 = sum(cargadores["pistola"]) + sum(cargadores["ametralladora"]) + sum(cargadores["escopeta"]) + sum(cargadores["fusil de francotirador"])

print(str("puedes matar a"),suma1, str("zombies"))

print("CASO 2")

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4], 
    'bazoka': [1, 1]
}



municion={key:sum(values) for key,values in cargadores.items() if key in armas}
print(str("puedes matar a"),sum(municion.values()),str("zombies"))

print("CASO 3")

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1] 
}

municion={key:sum(values) for key,values in cargadores.items() if key in armas}
print(str("puedes matar a"),sum(municion.values()),str("zombies"))