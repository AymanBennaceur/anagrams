# COPYRIGHT 2020, Vida Dujmovic and Diana Inkpen. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Entrez le nom du fichier: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("Il n'y a pas aucun fichier avec ce nom. Essayez encore une fois.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Retourne une nouvelle chaine de caracteres a partir de la chaine word, 
    en minuscule, sans les caracteres specieux et sans les chiffres

    La chaine retournee ne doit pas contenir:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 \t \n

    >>> clean_word("co-operation.")
    'cooperation'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'
    >>> clean_word("SEO : 5 outils gratuits pour trouver des mots-cles pertinents")
    'seo   outils gratuits pour trouver des motscles pertinents'
    '''
    #VOTRE CODE ICI    
    x = word.lower()
    lstx = list(x)
    lst = ['!','.','?',':',',',"'",'"','-','_','\\','(',')','[',']','{','}','%','0','1','2','3','4','5','6','7','8','9','\t','\n']
    for i in x:
        if i in lst:
            lstx.remove(i)
    stringx =''.join(lstx)
    return stringx    


def test_letters(w1, w2):
    '''(str,str, list of str)->bool
    La fonction retourne True si les mots w1 et w2 ont exactement les memes
    lettres, et False sinon

    >>> test_letters("mais", "amis")
    True
    >>> test_letters("lapin", "pinla")
    True
    >>> test_letters("lapin", "alpin")
    True
    >>> test_letters("alin", "alpin")
    False
    '''
    #VOTRE CODE ICI
    if len(w1)!= len(w2):
        return False
    for i in w1:
        if i in w2 and w1.count(i) == w2.count(i):
            continue
        else:
            return False
    return True
                
    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Pour la chaine s qui represente le texte, la fonction retourne une liste avec ces exigences:
    - les mot ne contient pas des caracteres specieux our des chiffres)
    - il n'y a pas de mots qui se repetent dans la liste
    - la liste est triee en ordre alphabetique (vous pouvez utilser s.sort() ou sorted())

    La fonction doit applelez la fonction clean_word.

    Vous pouvez utiliser s.split() pour obtenir une liste coupee par des espaces.
    
    >>> create_clean_sorted_nodupicates_list("Consultez notre site de web pour tout savoir de l'actualite internationale, nationale et regionale.")
    ['consultez', 'de', 'et', 'internationale', 'lactualite', 'nationale', 'notre', 'pour', 'regionale', 'savoir', 'site', 'tout', 'web']

    '''

    #VOTRE CODE ICI
    cleaned = clean_word(s)
    lst = cleaned.split()
    n = 0
    for i in range(len(lst)-1):
        x = lst.count(lst[n])
        if x != 1:
            lst.remove(lst[n])
        n +=1
    clean_sorted = sorted(lst)
    return clean_sorted
            
        
def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - word est une chaine de caractere qui represente un mot
    - wordbook est une liste des mots (sans des mots repetes)

    La fonction retourne une liste des anagrammes de mot word dans la liste wordbook
    Il faut utiliser la foction test_letters
    
    >>> word_anagrams("liste", wordbook)
    ['lites']
    >>> word_anagrams("lapin", wordbook)
    ['alpin', 'plain']
    >>> word_anagrams("elephant", wordbook)
    []
    '''

    #VOTRE CODE ICI
    lst = []
    for i in wordbook:
        x = test_letters(word, i)
        if x == True and i != word:
            lst.append(i)
    return lst       
    

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l est une liste des mots (sans des mots repetes)
    - wordbook est une liste des mots (sans des mots repetes)

    La fonction retourne une liste des entiers ou l'entier de index i represente
    le nombre des anagrammes dans la liste wordbook pour le mot de index i dans liste l.
    
    Quand un mot dans la liste l est le meme que le mot dans la liste wordbook, on ne le compte pas.

    >>> count_anagrams(["liste","amis", "lapin", "anee", "race", "oreilles"], wordbook)
    [1, 4, 2, 0, 5, 2]
    '''
    #VOTRE CODE ICI
    lst = []
    for i in l:
        count = 0
        for k in wordbook:
            if test_letters(i,k) and k != i:
                count +=1
        lst.append(count)         
    return lst            
            
def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l est une liste des mots (sans de repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans la liste wordbook pour le mot des index i dans la liste l.

    La fonction retournes tous les mots de la liste l qui ont exactement k anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> k_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2],2)
    ['lapin', 'oreilles']

    '''
    
    #VOTRE CODE ICI
    lst = []
    count = 0
    for i in anagcount:
        if i == k:
            lst.append(l[count])
        count += 1
    return lst

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans liste wordbook pour le mot de index i dans la liste l.

    La fonction retournes tous les mots de l avec le nombre maximal des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)
    
    >>> max_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['race']
    '''
    
    #VOTRE CODE ICI
    lst = []
    for i in range(len(anagcount)):
        if anagcount[i] == max(anagcount):
            lst.append(l[i])
    return lst
    

def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i integer dans la liste
    represente le nombre des anagrammes dans wordbook pour le mot de index i en l.

    La fonction retournes tous les mots de l sans des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)
    
    >>> zero_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['anee']
    '''
    
    #VOTRE CODE ICI
    lst = []
    for i in range(len(anagcount)):
        if anagcount[i] == 0:
            lst.append(l[i])
    return lst
            
    


