
armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17],
    'ametralladora': [33, 40],
    'escopeta': [2, 2, 2, 1]
}

resultado=0
for i in armas:
    a= any("pistola" in string for string in armas)
    b= any("pistola" in string for string in cargadores)
    if a and b ==True:
        pis=sum(cargadores["pistola"])
        resultado=pis
    c= any ("ametralladora" in string for string in armas)
    d= any ("ametralladora" in string for string in cargadores)
    if c and d==True:
        ame=sum(cargadores["ametralladora"])
        resultado=resultado + ame
    e=any ("escopeta" in string for string in armas)
    f=any ("escopeta" in string for string in cargadores)
    if e and f==True:
        esc=sum(cargadores["escopeta"])
        resultado=resultado+ esc
    g=any ("fusil de francotirador" in string for string in armas)
    h=any ("fusil de francotirador" in string for string in cargadores)
    if g and h==True:
        fus=sum(cargadores["fusil de francotirador"])
        resultado=resultado+fus
    i=any("bazoka" in string for string in armas)
    j=any("bazoka" in string for string in cargadores)
    if i and j==True:
        baz=sum(cargadores["bazoka"])
        resultado=resultado+baz
print("Si no fallas ni un tiro", "matarías unos",resultado, " Zombis.")
print("¡¡¡Enhorabuena!!!", "y ahora a correr.", sep="...")