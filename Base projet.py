from random import *

class Objet:

    def __init__(self):
        self.Utilisable_combat = True
        self.Quantité = 0
        self.nom = nom


class Potion(Objet):

    def __init__(self):
        self.nom = 'Potion de vie'

    def Effet(self, joueur):
        joueur.vie += 10
        if (joueur.vie > joueur.vie_max) :
            joueur.vie=joueur.vie_max


class Personnage:

    def __init__(self):
        self.nom=""
        self.niveau=1
        self.vie=0
        self.vie_max=0
        self.force=0
        self.agilite=0

    def jet_degat(self, ennemie):

        #Fonction retournant le calcul du jet de dégats de "self" sur "ennemie"

        degats=self.force
        ennemie.vie -= degats
        if degats == 0 :
            print("%s esquive l'attaque" % ennemie.nom)
        else :
            print("%s inflige %i dégats à %s" % (self.nom, degats, ennemie.nom))
        return degats


class Bandit(Personnage):

    def __init__(self, joueur):
        Personnage.__init__(self)
        self.nom="un Bandit"
        self.niveau= randint(1, joueur.niveau)
        self.vie_max = randint(10, joueur.niveau+10)
        self.vie=self.vie_max
        self.force=self.niveau
        self.agilite=self.niveau

    def Tour(self, joueur):

        if (self.vie > 0):
            degats=self.jet_degat(joueur)
            joueur.vie -= degats


class Loup(Personnage):

    def __init__(self, Joueur):
        Personnage.__init__(self)
        self.nom="un slime de mort"


class Joueur(Personnage):
    
    def __init__(self):
        Personnage.__init__(self)
        self.nom="marcel"
        self.vie_max=12
        self.vie=12
        self.force=2
        self.agilite=1
        self.position = [1,1]
        self.etat='normal'

        self.inventaire = {}
        self.inventaire["Grenade"] = [3]
        self.inventaire["zeubi"] = [1]

    def Inventaire(self):
        #Fonction affichant inventaire hors combat
        pass

    def Combat(self, Ennemi):
        #Fonction simulant un combat

        print("%s se retrouve face a face avec %s" % (self.nom, Ennemi.nom ))
        
        while (self.etat == 'combat'):

            if (self.agilite >= Ennemi.agilite):
                self.Tour_Joueur(Ennemi)
                Ennemi.Tour(self)    
                self.test_victoire(Ennemi)

            else :
                Ennemi.Tour(self)
                self.Tour_Joueur(Ennemi)
                self.test_victoire(Ennemi)

    def test_victoire(self, Ennemi):

        if (Ennemi.vie < 0) :
            print("gg ta gagné")
            self.etat='normal'

        elif  (self.vie < 0) :
            print("gg t mort")
            self.etat='mort'

    def Tour_Joueur(self,Ennemi):

        if (self.vie > 0):
            print("Attaquer \nSorts \nInventaire \nEtat \nFuite")
            Choix=input("> ")
            if(Choix=='Attaquer'):
                self.Attaquer(Ennemi)
            elif(Choix=='Sorts'):
                self.sorts()
            elif(Choix=='Inventaire'):
                self.Inventaire()
            elif(Choix=='Etat'):
                self.Etat()
            elif(Choix=='Fuite'):
                self.fuite()
            else :
                print("%s ne comprend pas la suggestion" % (self.nom))

    def Attaquer(self,Ennemi):

        degats=self.jet_degat(Ennemi)
        Ennemi.vie -= degats       

    def Sorts(self):

        #Afficher sorts
        #Demander le choix
        #vérifier si on le mana
        #faire les dégats

        pass

    def Fuite(self):
        #Fonction de test de fuite
        pass

    def Inventaire_combat(self):
        #Fonction affichant l'inventaire
        pass

    def Etat(self):
        #Fonction affichant les pv / mana / etc ...
    
        print("pv : %i/%i \nPosition : %s" % (self.vie, self.vie_max, self.position))

    def Aide(self):
        print(Commandes.keys())

    def Quitter(self):
        #Quitte le jeu

        print("Apres une longue aventure %s decide rentrer chez lui, pas de chance il trébuche sur un rocher et meurt sur le coup" % self.nom)
        self.vie=0

    def Repos(self):

        print("%s se repose" % self.nom)
        if self.vie < self.vie_max :
            print('%s se sent revigoré apres un peu de repos' % self.nom)
            self.vie = self.vie_max
        else :
            print("%s s'est reposé mais ne se sent pas plus en forme" % self.nom)

    def Exploration(self):
        #Fonction de déplacement dans le monde 

        mouvementEffectue = False
        while mouvementEffectue != True :
            print("Dans quelle direction ? \n Haut, Bas, Gauche, Droite") #Haut=1, Bas=2, Gauche=3, Droite=4
            TestDirection = input("> ")
            if TestDirection == ('haut' or 'Haut'):
                if testMouvementPossible(self.position[0],self.position[1],1) :
                    #self.positionPrecedente = self.position
                    self.position[1] -= 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == ('bas' or 'Bas') :
                if testMouvementPossible(self.position[0],self.position[1],2) :
                    #self.positionPrecedente = self.position
                    self.position[1] += 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == ('gauche' or 'Gauche') :
                if testMouvementPossible(self.position[0],self.position[1],3) :
                    #self.positionPrecedente = self.position
                    self.position[0] -= 1 
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == ('droite' or 'Droite') :
                if testMouvementPossible(self.position[0],self.position[1],4) :
                    #self.positionPrecedente = self.position
                    self.position[0] += 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            else :
                print("%s ne comprend pas dans quelle direction il doit aller" % self.nom)

        if Map[self.position[0]][self.position[1]] == 1 :
            self.etat='combat'
            self.Combat(Bandit(self))

        elif Map[self.position[0]][self.position[1]] == 2 :
            #self.Evenement()
            pass

        elif Map[self.position[0]][self.position[1]] == 3 :
            #self.Donjon()
            pass

        else :
            print("%s s'avance plus profondément dans la foret mais rien ne se passe" % self.nom)


def testMouvementPossible(positionX, positionY, direction):

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

def initialisation_map():    # Fonction d'intialisation de la map avec les endroits clé

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

Commandes = {
    'etat' : Joueur.Etat,
    'reposer' : Joueur.Repos,
    'explorer' : Joueur.Exploration,
    #'fuite' : Joueur.Fuite,
    #'attaquer' : Joueur.Attaque,
    'quitter' : Joueur.Quitter,
    'aide' : Joueur.Aide,
    #'examiner' : Joueur.examiner
}

J1 = Joueur()
Map = initialisation_map()
J1.nom = input("Quel est votre nom ? ")
print("Tapez 'aide' pour avoir une liste des commandes disponibles")
print("%s s'avance dans une foret sombre en quete d'aventures" % J1.nom)

while(J1.vie > 0):
    ligne = input("> ")
    arg = ligne.split()
    if len(arg) > 0:
        CommandeCheck = False
        for c in Commandes.keys() :
            if arg[0] == c[:len(arg[0])] :
                Commandes[c](J1)
                CommandeCheck = True
                break
        if not CommandeCheck :
            print("%s ne comprend pas la suggestion" % J1.nom)

