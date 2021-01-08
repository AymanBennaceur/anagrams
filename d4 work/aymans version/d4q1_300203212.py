def nombreDivisibles(lis,n):
    '''
(list,int) --> int
la fct prend comme entré une liste d'entier et un entier
la fonction retourne le nombre d’éléments divisible par n trouvés dans la
liste
    '''
    count = 0
    for k in lis:
        if k % n == 0:
            count +=1
    return count


x = input("Veuillez entrer une liste des entiers par des espaces: ").split()
lis = []
for i in x:
    lis.append(int(i))
n = int(input("Veuillez entrer un entier positif: "))
nomb = nombreDivisibles(lis,n)
print("Le nombre des éléments divisibles par",n,"est",nomb)
