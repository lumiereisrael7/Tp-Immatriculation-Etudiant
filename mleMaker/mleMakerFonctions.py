import variables

def inserer(x,nom):
    Find = False
    if nom in x.keys():
        x[nom] += 1
        Find = True
        
    if Find == False:
        x[nom] = 1

def extractFromNamePren(nom, prenom):
    j = 0
    Nom = ''
    
    for i in nom :
        if j < 3:
            if i in 'AaEeIiOoUuYy':
                continue
            Nom += str(i)
            j += 1
    
    for i in range(j, 3):
        Nom += 'X'
    
    Nom += prenom[:3]
    
    for i in range(len(Nom), 6):
        Nom += 'X'
    
    Nom = Nom.upper()
    
    inserer(variables.Mle, Nom)
    
    return Nom

def numberString(x):
    if int(x) < 10:
        return '00' + str(x)
    elif int(x) < 100:
        return '0' + str(x)
    elif int(x) < 1000:
        return x

def assignMle(nom):
    return nom + numberString(variables.Mle[nom])
