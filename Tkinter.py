from tkinter import *
from d4 import *
#main
root = Tk()
root.title('Anagram finder')
root.configure(background='black')
#My functions
def click():
    entered_text = textentry.get()
    wordbook=open("french_noaccents.txt").read().lower().split()
    list(set(wordbook)).sort()
    mot = entered_text
    lst_word = word_anagrams(mot,wordbook)
    if mot in wordbook:
        lst_word.append(mot)
    fin_lst = sorted(lst_word)
    if lst_word == []:
        output_anagram = ("Il n'y a aucun mot avec ces lettres.",mot)
    else:
        output_anagram = ("Voici les mots avec exactement ces lettres:",fin_lst)
    Label(root, text="\nThe Anagrams for "+entered_text,bg='black',fg='white',font='none 12 bold') .grid(row=4, column=0, sticky = W)    
    y = Label(root, text=output_anagram,bg='black',fg='white',font='none 12 bold')
    y.grid(row=5, column=0, sticky = W)
def leave():
    root.destroy
    exit()

#my photo
photo1 = PhotoImage(file='anagramsgif.png')
Label (root, image = photo1, bg='black') .grid(row=0, column=0,sticky=W)
#label
Label(root, text='Enter the word you would like an anagram for:',bg='black',fg='white',font='none 12 bold') .grid(row=1, column=0, sticky = W)

#text entry
textentry= Entry(root, width = 80, bg="white")
textentry.grid(row=2, column=0, sticky=W)
#submit button
Button(root, text='SUBMIT', width = 6, command = click) .grid(row=3, column = 0, sticky = W)
#exit label and button
Label(root, text='Click To Exit',bg='black',fg='white',font='none 12 bold') .grid(row=6, column=0, sticky = W)
Button(root, text='EXIT', width = 6, command = leave) .grid(row=7, column = 0, sticky = E)

#run the main loop
root.mainloop()

print('hello world')
x = input('whats your namesf')
print('your name is', x)
