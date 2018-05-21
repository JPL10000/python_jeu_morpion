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
  
  
        
