
from tkinter import *
#main
root = Tk()
root.title('Anagram finder')
root.configure(background='black')
#My functions
def click():
    entered_text = textentry.get()
#my photo
photo1 = PhotoImage(file='anagramsgif.png')
Label (root, image = photo1, bg='black') .grid(row=0, column=0,sticky=W)
#label
Label(root, text='Enter the word you would like an anagram for:',bg='black',fg='white',font='none 12 bold') .grid(row=1, column=0, sticky = W)
Label(root, text="\nThe Anagrams are:",bg='black',fg='white',font='none 12 bold') .grid(row=4, column=0, sticky = W)
#text entry
textentry= Entry(root, width = 40, bg="white")
textentry.grid(row=2, column=0, sticky=W)
#submit button
Button(root, text='SUBMIT', width = 6, command = click) .grid(row=3, column = 0, sticky = W)
#run the main loop
root.mainloop()

print('hello world')
x = input('whats your namesf')
print('your name is', x)