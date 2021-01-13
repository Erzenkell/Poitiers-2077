from random import *

class Objet:

    def __init__(self):
        self.Utilisable_combat = False
        self.Quantité = 0
        self.nom = nom


class Grenade(Objet):

    def __init__(self):
        self.nom = 'Grenade'
        self.Utilisable_combat = True
        self.Quantité = 0

    def Effet(self, ennemie):
        ennemie.vie -= 10   


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

        degats=self.attaque
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
        self.attaque=self.force
        self.agilite=self.niveau
        self.gain_xp=self.niveau
        self.defense=1

    def Tour(self, joueur):

        if (self.vie > 0):
            degats=self.jet_degat(joueur)


class Joueur(Personnage):
    
    def __init__(self):
        Personnage.__init__(self)
        self.nom="marcel"
        self.vie_max=12
        self.vie=12
        self.force=3
        self.attaque=self.force
        self.agilite=1
        self.position = [1,1]
        self.etat='normal'
        self.defense=0
        self.xp=0
        self.xp_max=10

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

        #Fonction de test si le joueur ou son ennemi a gagné + gain de niveau

        if (Ennemi.vie < 0) :
            print("%s a vaincu %s" % (self.nom, Ennemi.nom))
            self.xp += Ennemi.gain_xp
            if (self.xp == self.xp_max):
                print("%s se sent plus fort" % (self.nom))
                self.xp = 0
                self.xp_max += 1
                self.niveau += 1
                self.force += 1
                self.agilite += 1
                self.vie_max += 1
                self.vie = self.vie_max
            self.etat='normal'

        elif  (self.vie < 0) :
            print("gg t mort")
            self.etat='mort'

    def Tour_Joueur(self,Ennemi):

        #Fonction simulant le tour du joueur

        if (self.vie > 0):
            print("Attaquer \nSorts \nInventaire \nEtat \nFuite")
            Choix=input("> ").lower()
            if (Choix.isnumeric() and int(Choix) == 1) or (not Choix.isnumeric() and Choix== 'attaquer'): 
                self.Attaquer(Ennemi)
            elif (Choix.isnumeric() and int(Choix) == 2) or (not Choix.isnumeric() and Choix== 'inventaire'): 
                self.Inventaire()
            elif (Choix.isnumeric() and int(Choix) == 3) or (not Choix.isnumeric() and Choix== 'etat'): 
                self.Etat()
            elif (Choix.isnumeric() and int(Choix) == 4) or (not Choix.isnumeric() and Choix== 'fuite'): 
                self.fuite()
            else :
                print("%s ne comprend pas la suggestion" % (self.nom))

    def Attaquer(self,Ennemi):

        self.jet_degat(Ennemi)    

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
            TestDirection = input("> ").lower()
            if TestDirection == 'haut':
                if testMouvementPossible(self.position[0],self.position[1],1) :
                    #self.positionPrecedente = self.position
                    self.position[1] -= 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == 'bas':
                if testMouvementPossible(self.position[0],self.position[1],2) :
                    #self.positionPrecedente = self.position
                    self.position[1] += 1
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == 'gauche' :
                if testMouvementPossible(self.position[0],self.position[1],3) :
                    #self.positionPrecedente = self.position
                    self.position[0] -= 1 
                    mouvementEffectue=True
                else :
                    print("Impossible d'aller dans cette direction")
            elif TestDirection == 'droite'  :
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

def Jeu():

    J1.nom = input("Quel est votre nom ? ")

    print("il y a peu, un virus mondial a décimé la moitié de la planète à cause d'un gars qui a mangé un écureuil ou un truc comme ça, aucun vaccin n’a été retrouvé et 80% des chercheurs sont morts. Ce monde est apocalyptique, il vous sera difficile de survivre seul.")

    print("Vous vous réveillez d’une longue sieste, vous regarder votre journal de poche electroconnecté, il indique 3 février 2077,  position : ville MonQ, vous vous levez et ouvrez la fenêtre..")

    print("Au loin, entre les débris des autres immeubles écroulés vous parvenez à distinguer une personne aussi haute que 3 pommes, elle se fait agresser par un bandit, elle à l’air en danger, souhaitez vous l’aider? (oui/non)")

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

    else : 

        print("Vous décidez que c'est pas votre probleme et retournez vous coucher")

def Menu():

  print("1. Jouer")
  print("2. Charger")
  print("3. Credits")

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
      (not reponse.isnumeric() and reponse== 'sauvegarde'):
      #charger()
      pass

  else:
    print("Veuillez vérifier votre orthographe ou choisir un numéro valide")

J1 = Joueur()
Map = initialisation_map()
Menu()
