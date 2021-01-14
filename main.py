from random import *
from carte import *
from objets import *
import sys
import time

class Personnage:

    def __init__(self):
        self.nom=""
        self.niveau=1
        self.vie=0
        self.vie_max=0
        self.force=0
        self.agilite=0
        self.attaque=0
        self.defense=0

    def jet_degat(self, ennemie):

        #Fonction retournant le calcul du jet de dégats de "self" sur "ennemie"

        degats=self.attaque+self.force
        ennemie.vie -= degats
        if degats == 0 :
            print("%s esquive l'attaque" % ennemie.nom)
        else :
            print("%s inflige %i dégats à %s" % (self.nom, degats, ennemie.nom))


class Bandit(Personnage):

    def __init__(self, joueur):
        Personnage.__init__(self)
        self.nom="un Bandit"
        self.niveau= randint(1, joueur.niveau)
        self.vie_max = randint(10, joueur.niveau+10)
        self.vie=self.vie_max
        self.force=self.niveau
        self.attaque=0
        self.agilite=self.niveau
        self.gain_xp=self.niveau+1
        self.defense=1

    def Tour(self, joueur):

        if (self.vie > 0):
            self.jet_degat(joueur)

    def Loot(self, joueur):

        test= randint(1,10)
        if(test>3) :

            if 'banane' in joueur.inventaire :
                joueur.inventaire['banane']['nombre'] +=1
            else :
                joueur.inventaire.update(banane)


class Joueur(Personnage):
    
    def __init__(self):
        Personnage.__init__(self)
        self.nom="marcel"
        self.vie_max=12
        self.vie=12
        self.force=3
        self.attaque=0
        self.agilite=2
        self.position = [1,1]
        self.etat='normal'
        self.defense=0
        self.xp=0
        self.xp_max=10
        self.donjon=False

        self.equipement = {
            'arme' : ''
        }

        self.inventaire = {
            'vieux baton' : {'type': 'arme', 'nombre': 1, 'degats' : 1},
            'grenade' : {'type': 'combat', 'nombre' : 3,  'degats' : 5},
            'canette périmée' : {'type': 'consomable', 'nombre' : 3, 'effet' : 5}
            }

    def lancer_combat(self):
        self.etat='combat'
        self.Combat(Bandit(self))

    def Combat(self, Ennemi):
        #Fonction simulant un combat

        print("%s se retrouve face a face avec %s de niveau %i" % (self.nom, Ennemi.nom, Ennemi.niveau))
        
        while (self.etat == 'combat'):

            self.tour_effectue = False

            if (self.agilite >= Ennemi.agilite):
                self.Tour_Joueur(Ennemi)
                Ennemi.Tour(self)    
                self.test_victoire(Ennemi)

            else :
                Ennemi.Tour(self)
                self.Tour_Joueur(Ennemi)
                self.test_victoire(Ennemi)

    def test_victoire(self, Ennemi):

        #Fonction de test si le joueur ou son ennemi a gagné + gain de niveau

        if (Ennemi.vie < 0) :
            print("%s a vaincu %s" % (self.nom, Ennemi.nom))
            self.xp += Ennemi.gain_xp
            print("%s obtient %i points d'xp" % (self.nom, Ennemi.gain_xp))
            if (self.xp == self.xp_max):
                print("%s se sent plus fort" % (self.nom))
                self.xp = 0
                self.xp_max += 1
                self.niveau += 1
                self.force += 1
                self.agilite += 1
                self.vie_max += 2
                self.vie = self.vie_max
            self.etat='normal'

        elif  (self.vie < 0) :
            print("gg t mort")
            self.etat='mort'

    def Tour_Joueur(self,Ennemi):

        #Fonction simulant le tour du joueur

        if (self.vie > 0):
            while self.tour_effectue == False :
                print("Attaquer \nInventaire \nEtat \nFuite")
                Choix=input("> ").lower()
                if (Choix.isnumeric() and int(Choix) == 1) or (not Choix.isnumeric() and Choix== 'attaquer'): 
                    self.Attaquer(Ennemi)
                elif (Choix.isnumeric() and int(Choix) == 2) or (not Choix.isnumeric() and Choix== 'inventaire'): 
                    Afficher_inventaire(self)
                elif (Choix.isnumeric() and int(Choix) == 3) or (not Choix.isnumeric() and Choix== 'etat'): 
                    self.Etat_combat(Ennemi)
                elif (Choix.isnumeric() and int(Choix) == 4) or (not Choix.isnumeric() and Choix== 'fuite'): 
                    self.Fuite(Ennemi)
                else :
                    print("%s ne comprend pas la suggestion" % (self.nom))

    def Attaquer(self,Ennemi):

        self.jet_degat(Ennemi)  
        self.tour_effectue = True  

    def Etat_combat(self, Ennemi):

        print("pv : %i/%i \npv ennemi : %i/%i" % (self.vie, self.vie_max, Ennemi.vie, Ennemi.vie_max))
        self.Tour_Joueur(Ennemi)

    def Fuite(self, Ennemi):
        

        if (randint(1, self.agilite) > Ennemi.agilite) and self.donjon == False :
            print("%s arrive a fuir le combat" % self.nom)
            self.etat = 'normal'
        else :
            print("%s essaye de fuir le combat mais %s l'en empeche" % (self.nom, Ennemi.nom))   


def print_slow(texte):
    for lettre in texte:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        time.sleep(0.015)

def Jeu():

    J1 = Joueur()
    Map = initialisation_map()
    J1.nom = input("Quel est votre nom ? ")

    print_slow("il y a peu, un virus mondial a décimé la moitié de la planète à cause d'un gars qui a mangé un écureuil ou un truc comme ça, aucun vaccin n’a été retrouvé et 80% des chercheurs sont morts. Ce monde est apocalyptique, il vous sera difficile de survivre seul.\n")
    time.sleep(2)

    print_slow("Vous vous réveillez d’une longue sieste, vous regardez votre journal de poche electroconnecté, il indique 3 février 2077,  position : ville MonQ, vous vous levez et ouvrez la fenêtre..\n")
    time.sleep(2)

    print_slow("Au loin, entre les débris des autres immeubles écroulés vous parvenez à distinguer une personne aussi haute que 3 pommes, elle se fait agresser par un bandit, elle à l’air en danger, souhaitez vous l’aider? (oui/non)\n")

    Q1_intro = input("> ").lower()

    if(Q1_intro == 'oui'):

        J1.etat='combat'
        J1.Combat(Bandit(J1))
        print("Dialogue apres combat")
        Q2_intro="canard"        
        while (Q2_intro != 'oui'):

            Q2_intro=input("Voulez vous l'aider ? (oui/non) : ").lower()
            if (Q2_intro != 'oui'):
                print("Pourquoi tu ne veux pas pas m'aider ? **Elle vous attache à un arbre** Ecoute, je me suis fait dérober un vaccin qui pourra sauver l'humanité, j'ai besoin d'une personne qui pourra m'aider à retrouver ce vaccin, je sais déjà qui est la personne qui m'a volé, son nom est 'choumeurt' tant que tu ne voudras pas m'aider je te laisserai attaché là et un bandit viendra te dépouiller ou peut être les loups.. qui sait ! Ahahaha.")

        print("Quoi, tu veux m'aider à sauver l'humanité ? Bon, c'est vrai que j'aurai peut être besoin de toi, une personne qui fonce dans le tas sans réfléchir, ça peut servir.\nBon alors, je me suis fait dérober par un certain 'choumeurt', ouais c'est son nom, un vaccin capable de sauver l'humanité, il faut qu'on le retrouve à tout prix !\nOn va commencer par partir receuillir des informations sur ce mec")

        print("Tapez 'aide' pour avoir une liste des commandes disponibles")

        while(J1.vie > 0):
            ligne = input("> ").lower()
            if ligne == 'etat' :
                Etat(J1)
            elif ligne == 'reposer' :
                Repos(J1)
            elif ligne == 'explorer' :
                Ev = Exploration(J1, Map)
                if Ev == 'combat' :
                    J1.lancer_combat()
                elif Ev == 'evenement' :
                    pass
                elif Ev == 'donjon' :
                    pass
            elif ligne == 'sauvegarder' :
                Sauvegarder(J1)
            elif ligne == 'quitter' :
                Quitter(J1)
            elif ligne == 'aide' :
                Aide()
            else :
                print("%s ne comprend pas la suggestion" % J1.nom)

    else : 

        print("Vous décidez que c'est pas votre probleme et retournez vous coucher")

def Menu():

    choix = False
    while choix == False :

        print("1. Jouer")
        print("2. Charger")
        print("3. Credits")
        print("4. Quitter")

        reponse = input("> ").lower()

        if (reponse.isnumeric() and int(reponse) == 1) or \
          (not reponse.isnumeric() and reponse== 'jouer'):            
            Jeu()

        elif (reponse.isnumeric() and int(reponse) == 3) or \
          (not reponse.isnumeric() and reponse== 'credits'):
            print("By Alexandre Thibord")
            print("Théo Wizman")
            print("Sammy Ferrier")
    
        elif (reponse.isnumeric() and int(reponse) == 2) or \
          (not reponse.isnumeric() and reponse== 'charger'):
            #charger()
            pass

        elif (reponse.isnumeric() and int(reponse) == 4) or \
          (not reponse.isnumeric() and reponse== 'quitter'):            
            choix = True

        else:
            print("Veuillez vérifier votre orthographe ou choisir un numéro valide")

Menu()