'''
Documentation, License etc.

@package projet_morpion
'''

# 1ère étape : Ecrire une fonction pour afficher le tableau de jeu. Configurer votre tableau comme une liste, où chaque index 1-9 correspond à un nombre sur un clavier, de sorte que vous obtenez un terrain de 3 par 3.

from IPython.display import clear_output

def affiche_tableau(tableau):
    clear_output()
    print('   |   |')
    print(' ' + tableau[7] + ' | ' + tableau[8] + ' | ' + tableau[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tableau[4] + ' | ' + tableau[5] + ' | ' + tableau[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tableau[1] + ' | ' + tableau[2] + ' | ' + tableau[3])
    print('   |   |')
    
affiche_tableau(['sert à rien','','','','','','','','',''])
  

import tkinter as Tk
import time

def affiche_canevas_tk() :
    N = 3 
    pas=600/N 
    root = Tk.Tk() 
    c = Tk.Canvas(root,height=600,width=600) 
    listidrec=N*[[]] 
    for i in range(N): 
        listidrec[i]=N*[-1] 
    for i in range(N): 
        for j in range(N): 
            listidrec[i][j] = c.create_rectangle(pas*i, pas*j, pas*(i+1), pas*(j+1), fill='#00FF00') 
 
    c.pack()
    def test():
        for i in range(17,256):
            c.itemconfig(listidrec[1][1],fill='#0000'+hex(i)[2:])
            print(hex(i)[2:])
            time.sleep(0.05)        
            root.update()
    
    
    b = Tk.Button(text = 'test', command= test)
    b.pack()
    root.mainloop()

# affiche_canevas_tk()
