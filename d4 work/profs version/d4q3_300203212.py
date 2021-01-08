def sequenceMax(lis):
    '''
(list) --> int
la fct prend comme entré une liste d'entier ou float
la fonction retourne  la longueur de la plus longue séquence
d’éléments consécutifs égaux
s’il n’y a aucune séquence la fct retourne 1
    '''
    n = 1
    i = 0
    sequence = 1
    sequence_max = 1
    while n < len(lis):
            if lis[i] == lis[n]:
                sequence += 1
            else:
                sequence = 1
                i = n
            if sequence > sequence_max:
                sequence_max = sequence
                
            n += 1
    return sequence_max



x = input("Veuillez entrer une liste des valeurs séparées par des espaces: ").split()
i = 0
lis = []
while i<len(x):
    try:
        lis.append(int(x[i]))
    except ValueError:
        lis.append(float(x[i]))
    i += 1
print(sequenceMax(lis))

