from variables import *
import mleMakerFonctions

def printMenu():
    print('')
    print('')
    print('1- Obtenez un matricule')
    print('')
    
    print('2- Afficher la liste des étudiants enrégistrés')
    print('')
    
    print('3- Modifiez vos informations')
    print('')
    
    print('4- Quitter')
    print('')
    print('')
    return input('Entrez votre choix: ')

def enterInformation():
    Etu = {'nom': '', 'prenom': ''}
    
    nom = input('Entrez votre nom: ')
    while not nom.isalpha():
        nom = input('Entrez un nom valide: ')
    Etu['nom'] = nom.upper()
    
    prenom = input('Entrez votre prenom: ')
    while not prenom.isalpha():
        prenom = input('Entrez un prenom valide: ')
    Etu['prenom'] = prenom
    
    Etu['mle'] = assignMle(extractFromNamePren(Etu['nom'], Etu['prenom']))
    
    variables.Etudiant.append(Etu)
    
    print('')
    print('')
    print('Vos informations: ')
    print(Etu['nom'], Etu['prenom'], Etu['mle'])
    print('')
    
def printList():
    """Cette fonction affiche la liste des etudiants enrégistrés"""
    
    print('La liste des étudiants enrégistré: ')
    
    j = 1
    if len(variables.Etudiant) > 0:
        print('Matricule', '\t', 'Nom', '\t', 'Prenom')
        for i in variables.Etudiant:
            print(j, '-', i['mle'], i['nom'], i['prenom'])
            j += 1
    else:
        print("Aucun étudiant n'est encore enregistré")
