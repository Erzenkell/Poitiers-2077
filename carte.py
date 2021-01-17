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
            return 'metro des clodos'
        
        elif Map[joueur.position[0]][joueur.position[1]] == 4 :
            return 'Hetic'

        elif Map[joueur.position[0]][joueur.position[1]] == 5 :
            return 'Uno'

        elif Map[joueur.position[0]][joueur.position[1]] == 6 :
            return 'epee nice'        

        else :
            print("%s s'avance plus profondément dans la ville mais rien ne se passe" % joueur.nom)

def testMouvementPossible(positionX, positionY, direction, Map):

     # Fonction de test qui renvoie True ou False en fonction de si le moucement choisi est possible

    if direction ==1:

        if positionY - 1 < 0:
            return False
        else:
            return True

    elif direction ==2 :

        if positionY + 1 >len(Map[positionX])-1:
            return False
        else:
            return True

    elif direction ==3 :

        if positionX-1 <0:
            return False
        else :
            return True

    else:

        if positionX+1 >len(Map)-1:
            return False
        else :
            return True

def Repos(joueur):

    print("%s se repose" % joueur.nom)
    if joueur.vie < joueur.vie_max :
        print('%s se sent revigoré apres un peu de repos' % joueur.nom)
        joueur.vie = joueur.vie_max
    else :
        print("%s s'est reposé mais ne se sent pas plus en forme" % joueur.nom)

def Quitter(joueur):
    #Quitte le jeu

    print("Apres une longue aventure %s decide rentrer chez lui, pas de chance il trébuche sur un rocher et meurt sur le coup" % joueur.nom)
    joueur.vie=0

def Sauvegarder(joueur):
    #Fonction de sauvegarde --> récupere les données stockées dans joueur

    fichier = open("Desktop\Projet Python\save.txt", "w")
    fichier.write(str(joueur.nom))
    fichier.close()
    print('Sauvegarde effectuée')

def Etat(joueur):
    #Fonction affichant les pv / pc / etc ...
    
    print("pv : %i/%i \nPoints combat : %i" % (joueur.vie, joueur.vie_max, joueur.points_combat))    

def Aide(joueur):
    #Affiche les commandes disponibles et la direction a prendre

    print("Commandes disponibles : Etat / Reposer / Explorer / inventaire / Sauvegarder / Quitter / Aide")

    if joueur.metro_des_clodos == False :
        print("\033[32mNous devons commencer par savoir qui est ce choumeurt %s, essayons d'aller voir au metro des clodos si quelqu'un sait qui c'est. [3,4]\033[0m " % joueur.rn)
    else :
        print("\033[32mMaintenant que nous savons ou trouver choumeurt allons lui botter le cul et récupérer le vaccin %s ! [2,7]\033[0m" % joueur.rn)

    if joueur.Universite_visite == False :
        print("\033[32mTu devrai aller voir du coté de l'université peut-etre y trouvera-tu un objet important pour la suite ! [0,4]\033[0m")
    
    if joueur.epee_nice == False :
        print("\033[32mIl paraitrai qu'il y a une puissante arme dans le musée de la ville, tu devrai aller y faire un tour [4,0]\033[0m")

def initialisation_map():

    # Fonction d'intialisation de la map avec les endroits clé --> 0 = rien / 1 = combat / 2 = Evenement / 3 = Metro des clodos /  4 = Hetic / 5 = Universite / 6 = Epée nice

    liste = [
        [0,1,1,2,5],
        [2,2,1,2,0],
        [2,1,2,1,0,1,1,4],
        [1,1,1,2,0],
        [6,0,1,3,1]
    ]

    return liste

