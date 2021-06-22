from mleMaker import designFonctions

def Menu():
    """Ce programme vous aide à attribuer un numero matricule à un étudiant suite à la saisie de son nom et prenom"""

    print('Hi!!!')
    print(help(Menu))

    while True:
        if designeFonctions.printMenu() == str(1):
            designFonctions.enterInformation()
        elif designFonctions.printMenu() == str(2):
            designFonctions.printList()
        elif designFonctions.printMenu() == 3:
            print('')
            print('Aurevoir')
            print('')
            break;
        else:
            print('')
            print('Entrez un bon choix: ')


Menu()
