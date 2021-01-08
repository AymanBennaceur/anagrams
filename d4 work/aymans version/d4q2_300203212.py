def sequenceDesDeux(lis):
    '''
(list) --> boolean
la fct prend comme entré une liste d'entier ou float
la fonction retourne True s’il y a au moins une séquence
de deux éléments consécutifs égaux et False dans le cas contraire
    '''
    n = 1
    for i in lis:
        if n == len(lis):
            break
        if i == lis[n]:
            return True
        n +=1
    return False

x = input("Veuillez entrer une liste des valeurs séparées par des espaces: ").split()
i = 0
lis = []
while i<len(x):
    try:
        lis.append(int(x[i]))
    except ValueError:
        lis.append(float(x[i]))
    i += 1
print(sequenceDesDeux(lis))
