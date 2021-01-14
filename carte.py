def Exploration(joueur, Map):
        #Fonction de déplacement dans le monde 

        mouvementEffectue = False
        while mouvementEffectue != True :
            print("Dans quelle direction ? \n Haut, Bas, Gauche, Droite") #Haut=1, Bas=2, Gauche=3, Droite=4
            TestDirection = input("> ").lower()
            if TestDirection == 'haut':
                if testMouvementPossible(joueur.position[0],joueur.position[1],1,Map) :
                    #self.positionPrecedente = self.position
                    joueur.position[1] -= 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == 'bas':
                if testMouvementPossible(joueur.position[0],joueur.position[1],2,Map) :
                    #self.positionPrecedente = self.position
                    joueur.position[1] += 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == 'gauche' :
                if testMouvementPossible(joueur.position[0],joueur.position[1],3,Map) :
                    #self.positionPrecedente = self.position
                    joueur.position[0] -= 1 
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == 'droite'  :
                if testMouvementPossible(joueur.position[0],joueur.position[1],4,Map) :
                    #self.positionPrecedente = self.position
                    joueur.position[0] += 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            else :
                print("%s ne comprend pas dans quelle direction il doit aller" % joueur.nom)

        if Map[joueur.position[0]][joueur.position[1]] == 1 :
            return 'combat'

        elif Map[joueur.position[0]][joueur.position[1]] == 2 :
            return 'evenement'

        elif Map[joueur.position[0]][joueur.position[1]] == 3 :
            return 'donjon'
            pass

        else :
            print("%s s'avance plus profondément dans la foret mais rien ne se passe" % joueur.nom)

def Etat(joueur):
    #Fonction affichant les pv / mana / etc ...
    
    print("pv : %i/%i \nPosition : %s" % (joueur.vie, joueur.vie_max, joueur.position))

def Aide():
    #Affiche les commandes disponibles

    #print(Commandes.keys())
    print("Commandes disponibles : Etat / Reposer / Explorer / Sauvegarder / Quitter / Aide")

def Sauvegarder(joueur):

    fichier = open("Desktop\Projet Python\save.txt", "w")
    fichier.write(str(joueur.nom))
    fichier.close()
    print('Sauvegarde effectuée')

def Quitter(joueur):
    #Quitte le jeu

    print("Apres une longue aventure %s decide rentrer chez lui, pas de chance il trébuche sur un rocher et meurt sur le coup" % joueur.nom)
    joueur.vie=0

def Repos(joueur):

    print("%s se repose" % joueur.nom)
    if joueur.vie < joueur.vie_max :
        print('%s se sent revigoré apres un peu de repos' % joueur.nom)
        joueur.vie = joueur.vie_max
    else :
        print("%s s'est reposé mais ne se sent pas plus en forme" % joueur.nom)

def testMouvementPossible(positionX, positionY, direction, Map):

     # Fonction de test qui renvoie True ou False en fonction de si le moucement choisi est possible

    if direction ==1:

        if positionY - 1 < 0:
            return False
        else:
            return True

    elif direction ==2 :

        if positionY + 1 >len(Map[positionX]):
            return False
        else:
            return True

    elif direction ==3 :

        if positionX-1 <0:
            return False
        else :
            return True

    else:

        if positionX+1 >len(Map):
            return False
        else :
            return True

def initialisation_map():

    # Fonction d'intialisation de la map avec les endroits clé

    # Declaration de la map vide

    liste = []
    i=0
    while i< 4:
        liste.append([0] * 4)
        i+=1

    # Remplissage de la map --> 0 = rien / 1 = combat / 2 = Evenement / 3 = Donjon ;)

    liste[0][0]=0
    liste[0][1]=1
    liste[0][2]=1  
    liste[0][3]=2
    liste[1][0]=0
    liste[1][1]=1
    liste[1][2]=2
    liste[1][3]=1
    liste[2][0]=1
    liste[2][1]=0
    liste[2][2]=1
    liste[2][3]=1
    liste[3][0]=0
    liste[3][1]=2
    liste[3][2]=3
    liste[3][3]=1

    return liste