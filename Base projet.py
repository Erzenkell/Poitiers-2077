from random import *

""" j'ai fait ça """

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

class Epee_en_fer(Objet):

    def __init__(self):
        self.Utilisable_combat = False
        self.nom = "Epee en fer"
        self.attaque = 1


class Personnage:

    def __init__(self):
        self.nom=""
        self.niveau=1
        self.vie=0
        self.vie_max=0
        self.force=0
        self.agilite=0
        self.mana=0
        self.mana_max=0

    def jet_degat(self, ennemie):
        degats=min(randint(0, 6+self.force),ennemie.vie)
        ennemie.vie -= degats
        if degats == 0 :
            print("%s esquive l'attaque" % ennemie.nom)
        else :
            print("%s inflige %i dégats à %s" % (self.nom, degats, ennemie.nom))
        return degats


class Bandit(Personnage):

    def __init__(self, Joueur):
        Personnage.__init__(self)
        self.nom="un Bandit"
        self.niveau= randint(1, Joueur.niveau)
        self.vie_max = randint(10, Joueur.niveau+10)
        self.vie=self.vie_max
        self.force=self.niveau
        self.agilite=self.niveau

    def Tour(self, marcel):

        degats=self.jet_degat(marcel)
        marcel.vie -= degats
        if (marcel.vie < 0):
            print("T'es mort cheh")
            marcel.etat='mort'


class slime(Personnage):

    def __init__(self, Joueur):
        Personnage.__init__(self)
        self.nom="un slime de mort"


class Joueur(Personnage):
    
    def __init__(self):
        Personnage.__init__(self)
        self.nom="marcel"
        self.vie_max=12
        self.vie=12
        self.force=1
        self.agilite=1
        self.mana_max=10
        self.mana=10
        self.position = [1,1]
        self.etat='normal'
        
        self.inventaire = []

        self.sorts = {}
        self.sorts["boule de feu"] = [True, 2, 10]
        self.sorts["eclair"] = [1,6]



    def Exploration(self):
        #Fonction de déplacement
        pass

    def TestMouvement(self):
        #Fonction testant si le mouvement est possible
        pass

    def Inventaire(self):
        #Fonction affichant inventaire hors combat
        pass

    def Combat(self, Ennemi):
        #Fonction simulant un combat
        
        while (self.etat == 'combat'):
            if (self.agilite >= Ennemi.agilite):

                self.Tour_Joueur(Ennemi)
                Ennemi.Tour(self)    

            else :

                Ennemi.Tour(self)
                self.Tour_Joueur(Ennemi)

    def Tour_Joueur(self,Ennemi):

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
        if(Ennemi.vie < 0):
            #self.victoire(Ennemi)
            self.etat='normal'   

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
        pass

    def Victoire(self, Ennemie):

        pass


def init_Carte():
    #Fonction initialisation carte
    pass



J1=Joueur()
Ennemi1=Bandit(J1)
J1.etat = 'combat'
while(J1.vie > 0 and Ennemi1.vie > 0):
    J1.Combat(Ennemi1)