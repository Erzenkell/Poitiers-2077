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

    def jet_degat(self, Ennemi):
        #fonction simulant l'attaque de "self" sur "Ennemi"

        degats=self.force
        Ennemi.vie -= degats

        print("%s a infligé %i dégats a %s" % (self.nom, degats, Ennemi.nom))


class Bandit(Personnage):

    def __init__(self, Joueur):
        Personnage.__init__(self)
        self.nom=" un Bandit"
        self.niveau= randint(1, Joueur.niveau)
        self.vie_max = randint(10, 10+Joeur.niveau)
        self.vie=self.vie_max
        self.force=self.niveau
        self.agilite=self.niveau

class slime(Personnage):

    def __init__(self, Joueur):
        Personnage.__init__(self)
        self.nom="un slime de mort"

class Joueur(Personnage):
    
    def __init__(self):
        Personnage.__init__(self)
        self.vie_max=10
        self.vie=10
        self.attack=1
        self.agilite=1
        self.mana_max=10
        self.mana=10
        self.position = [1,1]

    def Exploration(self):
        #Fonction de déplacement

    def TestMouvement(self):
        #Fonction testant si le mouvement est possible

    def Inventaire(self):
        #Fonction affichant inventaire

    def Combat(self, Ennemi):
        #Fonction simulant un combat

        afficher menu combat
        demander choix
        si c'est attaque   
            fonction attaque
        si c'est sort
            fonction Sorts
        si c'ets fuite



    def Menu_Combat(self):
        #Fonction 
    
    def Attaque(self):
        #Fonction simulant un attaque

    def Sorts(self):
        #Fonction de selection d'un sort

    def Fuite(self):
        #Fonction de test de fuite

    def Inventaire_combat(self)
        #Fonction affichant l'inventaire

def init_Carte():
    #Fonction initialisation carte

