from random import *
from carte import *
from objets import *
from ascii import *
import socket
import platform
import webbrowser

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

    def jet_degat(self, ennemie, degats_base):

        #Fonction effectuant le calcul du jet de dégats de "self" sur "ennemie"

        degats=degats_base-ennemie.defense
        if degats < 0 :
            degats = 0
        ennemie.vie -= degats        
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
        self.compteur_tour = 1

    def Tour(self, joueur):

        if (self.vie > 0):
            if self.compteur_tour == 3 :
                print("%s donne un coup puissant a %s" % (self.nom, joueur.nom))
                self.jet_degat(joueur, self.force*2)
                self.compteur_tour = 0
            else :    
                print("%s donne un coup de couteau a %s" % (self.nom, joueur.nom) )
                self.jet_degat(joueur, self.force)
            self.compteur_tour += 1

    def Loot(self, joueur):

        test= randint(1,10)
        if(test>=3) :

            print("%s ramasse une banane sur le corp de %s" % (joueur.nom, self.nom))
            if 'banane' in joueur.inventaire :
                joueur.inventaire['banane']['nombre'] +=1
            else :
                joueur.inventaire.update(banane)

        else : 

            print("%s ramasse un couteau rouillé sur le corp de %s" % (joueur.nom, self.nom))
            if 'couteau rouillé' in joueur.inventaire :
                joueur.inventaire['couteau rouillé']['nombre'] += 1
            else : 
                joueur.inventaire.update(couteau_rouille)


class Loup(Personnage):

    def __init__(self, joueur):
        Personnage.__init__(self)
        self.nom="un loup"
        self.niveau= randint(1, joueur.niveau)
        self.vie_max = randint(5, joueur.niveau+5)
        self.vie=self.vie_max
        self.force=self.niveau
        self.attaque=2
        self.agilite=self.niveau+2
        self.gain_xp=self.niveau+1
        self.defense=0
        self.rage = False 

    def Tour(self, joueur):
        
        if self.vie > 0 :
            if (self.vie < self.vie_max/2) and (self.rage == False) :
                print("%s s'enrage" % self.nom)
                self.rage = True
        
            if self.rage == False :
                self.jet_degat(joueur, self.force)
            else :
                self.jet_degat(joueur, self.force+self.attaque)

    def Loot(self, joueur):

        test= randint(1,10)
        if(test>=3) :

            print("%s ramasse une canette de cola sur le corp de %s" % (joueur.nom, self.nom))
            if 'banane' in joueur.inventaire :
                joueur.inventaire['banane']['nombre'] +=1
            else :
                joueur.inventaire.update(banane)

        else : 

            print("%s ramasse un manteau de fourrure sur le corp de %s" % (joueur.nom, self.nom))
            if 'manteau de fourrure' in joueur.inventaire :
                joueur.inventaire['manteau de fourrure']['nombre'] += 1
            else : 
                joueur.inventaire.update(manteau_de_fourrure)
       

class Clodo(Personnage):

    def __init__(self, joueur):
        Personnage.__init__(self)
        self.nom="un clodo"
        self.niveau= joueur.niveau+1
        self.vie_max = randint(15, joueur.niveau+15)
        self.vie=self.vie_max
        self.force=self.niveau+1
        self.attaque=1
        self.agilite=self.niveau
        self.gain_xp=self.niveau+2
        self.defense=1

    def Tour(self, joueur):
        if self.vie > 0 :
            print("%s tappe %s avec son tesson de bouteille" % (self.nom, joueur.nom))
            self.jet_degat(joueur, self.force+self.attaque)

    def Loot(self, joueur):

        test= randint(1,10)
        if(test>=3) :

            print("%s ramasse une bouteille de Villageoise sur le corp de %s" % (joueur.nom, self.nom))
            if 'Villageoise' in joueur.inventaire :
                joueur.inventaire['Villageoise']['nombre'] +=1
            else :
                joueur.inventaire.update(villageoise)

        else : 

            print("%s ramasse un tesson de bouteille sur le corp de %s" % (joueur.nom, self.nom))
            if 'couteau rouillé' in joueur.inventaire :
                joueur.inventaire['tesson de bouteille']['nombre'] += 1
            else : 
                joueur.inventaire.update(tesson_de_bouteille)       


class Roi_des_clodos(Personnage):

    def __init__(self, joueur):
        Personnage.__init__(self)
        self.nom="un clodo"
        self.niveau= joueur.niveau+2
        self.vie_max = randint(15, joueur.niveau+15)
        self.vie=self.vie_max
        self.force=self.niveau+1
        self.attaque=1
        self.agilite=self.niveau
        self.gain_xp=self.niveau+2
        self.defense=1

    def Tour(self, joueur):
        if self.vie > 0 :
            print("%s tappe %s avec son tesson de bouteille" % (self.nom, joueur.nom))
            self.jet_degat(joueur, self.force+self.attaque)

    def Loot(self, joueur):

        print("%s ramasse une bouteille de Villageoise sur le corp de %s" % (joueur.nom, self.nom))
        if 'Villageoise' in joueur.inventaire :
            joueur.inventaire['Villageoise']['nombre'] +=1
        else :
            joueur.inventaire.update(villageoise)

        print("%s ramasse aussi l'armure du roi du métro" % joueur.nom)
        joueur.inventaire.update(armure_roi_clodos)


class Chomel(Personnage):

    def __init__(self, joueur):
        Personnage.__init__(self)
        self.nom = 'Denis Chomel'
        self.niveau = joueur.niveau + 3
        self.vie_max = joueur.vie_max + 20
        self.vie = self.vie_max
        self.force = self.niveau + 3
        self.attaque = 0
        self.agilite = self.niveau + 10
        self.gains_xp = self.niveau * 2
        self.defense = 5

    def Tour(self, joueur):
        
        if self.vie > 0 :
            
            print("%s attaque %s avec son poing" % (self.nom, joueur.nom))
            self.jet_degat(joueur, self.force) 
        
    def Loot(self) :
        pass


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
        self.points_combat = 0
        self.donjon=False
        self.rn=socket.gethostname()
        self.Universite_visite = False
        self.epee_nice = False
        self.metro_des_clodos = False

        self.equipement = {
            'arme' : '',
            'armure' : ''
        }

        self.inventaire = {
            'vieux baton' : {'type': 'arme', 'nombre': 1, 'degats' : 1},
            'grenade' : {'type': 'combat', 'nombre' : 1,  'degats' : 5},
            'canette périmée' : {'type': 'consomable', 'nombre' : 2, 'effet' : 5}
            }


def lancer_combat_random(joueur):

    joueur.etat='combat'
    if randint(0,1) == 1 :
        Afficher_bandit()
        Combat(joueur, Bandit(joueur))
    else :
        Afficher_loup()
        Combat(joueur, Loup(joueur))

def Combat(joueur, Ennemi):
    #Fonction simulant un combat

    print("%s se retrouve face a face avec %s de niveau %i\n" % (joueur.nom, Ennemi.nom, Ennemi.niveau))
    time.sleep(1)
        
    while (joueur.etat == 'combat'):

        joueur.tour_effectue = False

        if (joueur.agilite >= Ennemi.agilite):
            Tour_Joueur(joueur, Ennemi)
            joueur.points_combat += 5
            Ennemi.Tour(joueur)    
            test_victoire(joueur, Ennemi)

        else :
            Ennemi.Tour(joueur)
            Tour_Joueur(joueur, Ennemi)
            joueur.points_combat += 5
            test_victoire(joueur, Ennemi)

def test_victoire(joueur, Ennemi):

    #Fonction de test si le joueur ou son ennemi a gagné + gain de niveau

    if (Ennemi.vie <= 0) :
        print("%s a vaincu %s" % (joueur.nom, Ennemi.nom))
        joueur.xp += Ennemi.gain_xp
        print("%s obtient %i points d'xp" % (joueur.nom, Ennemi.gain_xp))
        Ennemi.Loot(joueur)
        if (joueur.xp == joueur.xp_max):
            print("%s se sent plus fort" % (joueur.nom))
            joueur.xp = 0
            joueur.xp_max += 1
            joueur.niveau += 1
            joueur.force += 1
            joueur.agilite += 1
            joueur.vie_max += 2
            joueur.vie = joueur.vie_max
        joueur.etat='normal'

    elif  (joueur.vie < 0) :
        print("gg t mort")
        joueur.etat='mort'

def Tour_Joueur(joueur,Ennemi):

    #Fonction simulant le tour du joueur

    if (joueur.vie > 0):
        while joueur.tour_effectue == False :
            print_slow("Attaquer \nCompetences \nInventaire \nEtat \nFuite\n", 0.01)
            Choix=input("> ").lower()
            if (Choix.isnumeric() and int(Choix) == 1) or (not Choix.isnumeric() and Choix== 'attaquer'): 
                Attaquer(joueur, Ennemi)
            elif (Choix.isnumeric() and int(Choix) == 2) or (not Choix.isnumeric() and Choix== 'competences'): 
                Competences(joueur, Ennemi)
            elif (Choix.isnumeric() and int(Choix) == 3) or (not Choix.isnumeric() and Choix== 'inventaire'): 
                Afficher_inventaire(joueur, Ennemi)
            elif (Choix.isnumeric() and int(Choix) == 4) or (not Choix.isnumeric() and Choix== 'etat'): 
                Etat_combat(joueur, Ennemi)
            elif (Choix.isnumeric() and int(Choix) == 5) or (not Choix.isnumeric() and Choix== 'fuite'): 
                Fuite(joueur, Ennemi)
            elif (Choix.isnumeric() and int(Choix) == 6) :
                dev_atk(joueur, Ennemi)
            else :
                print("%s ne comprend pas la suggestion zeubi" % (joueur.nom))

def dev_atk(joueur, Ennemi) :

        joueur.jet_degat(Ennemi, Ennemi.vie_max+Ennemi.defense)  
        joueur.tour_effectue = True

def Attaquer(joueur,Ennemi):

        joueur.jet_degat(Ennemi, joueur.force+joueur.attaque)  
        joueur.tour_effectue = True  

def Competences(joueur, Ennemi):

    print("%s a %i pc" % (joueur.nom, joueur.points_combat))
    print("Attaque puissante : 7pc")
    if joueur.niveau >= 3 :
        print("Attaque revigorante : 9pc")
    if joueur.niveau >= 5 :
        print("Ca va barder : 20pc")

    Choix_c = input("> ").lower()

    if (Choix_c.isnumeric() and int(Choix_c) == 1) or (not Choix_c.isnumeric() and Choix_c== 'attaque puissante') :
        if joueur.points_combat >= 7 :
            print("%s assene un coup puissant a %s" % (joueur.nom, Ennemi.nom))
            joueur.jet_degat(Ennemi, joueur.attaque+joueur.force*2)
            pv_perdu = round(joueur.vie_max / 10)
            print("%s perd %i pv dans l'action" % (joueur.nom, pv_perdu))
            joueur.vie -= pv_perdu
            joueur.points_combat -= 7
            joueur.tour_effectue = True
        else :
            print("pas assez de pc pour lancer l'attaque")
    
    elif (Choix_c.isnumeric() and int(Choix_c) == 2) or (not Choix_c.isnumeric() and Choix_c== 'attaque revigorante') :
        if joueur.points_combat >= 9 :
            print("%s attaque %s et en profite pour manger une pomme"  % (joueur.nom, Ennemi.nom))
            joueur.jet_degat(Ennemi ,joueur.force)
            print("%s recupere %i pv" % (joueur.nom, joueur.force))
            joueur.vie += joueur.force 
            if joueur.vie > joueur.vie_max:
                joueur.vie = joueur.vie_max
            joueur.points_combat -= 9
            joueur.tour_effectue = True
        else :
            print("pas assez de pc pour lancer l'attaque")

    elif (Choix_c.isnumeric() and int(Choix_c) == 3) or (not Choix_c.isnumeric() and Choix_c== 'ca va barder') :
        if joueur.points_combat >= 18 :
            print("%s envoie la sauce" % joueur.nom)
            joueur.jet_degat(Ennemi, joueur.attaque+joueur.force*3)
            joueur.points_combat -= 18
            joueur.tour_effectue = True
        else : 
            print("pas assez de pc pour lancer l'attaque")

    else :
        print("ce n'est pas une compétence valide")

def Etat_combat(joueur, Ennemi):

    print("pv : %i/%i \npv ennemi : %i/%i" % (joueur.vie, joueur.vie_max, Ennemi.vie, Ennemi.vie_max))
    Tour_Joueur(joueur, Ennemi)

def Fuite(joueur, Ennemi):        

    if (randint(1, joueur.agilite) > randint(1,Ennemi.agilite)) and joueur.donjon == False :
        print("%s arrive a fuir le combat" % joueur.nom)
        joueur.etat = 'normal'
    elif joueur.donjon == True :
        print("%s ne peut pas fuir ce combat" % joueur.nom)
    else :
        print("%s essaye de fuir le combat mais %s l'en empeche" % (joueur.nom, Ennemi.nom))   

def Universite(joueur) :

    if joueur.Universite_visite == False :
        print_slow("%s arrive dans une université en ruine, en se baladant dans les décombres %s voit au loin un coffre sur lequel se repose quelqu'un, %s s'approche discretement et il ne semble pas remarquer votre présence\n" % (joueur.nom, joueur.nom, joueur.nom), 0.01)
        time.sleep(1)
        print_slow("Que faites vous ? (Attaquer / Négocier)\n", 0.01)
        test = input('> ').lower()
        if test == 'négocier' :
            print("\033[32mTu va vraiment négocier avec ce clodo ? On est en 2077 on leur pete la gueule et on récupere le loot\033[0m")
            time.sleep(1)
            joueur.etat = 'combat'
            afficher_clodo()
            Ennemi = Clodo(joueur)
            Combat(joueur, Ennemi)
        else :
            print("\033[32mC'est bien pete lui la gueule a ce clodo et récupere le contenu du coffre\033[0m")
            time.sleep(1)
            joueur.etat = 'combat'
            afficher_clodo()
            Ennemi = Clodo(joueur)
            Combat(joueur, Ennemi)

        print_slow("Apres avoir bien combattu %s esssaye d'ouvrir le coffre mais celui-ci est protégé par un code." % joueur.nom, 0.01)
        test_c = 'canard'
        while test_c != 'non' :
            test_c = input("Voulez vous essayer de l'ouvrir ?\n> ")
            if test_c == 'oui' :
                test_c2 = input("Combinaison : ")
                if test_c2 == '1431' :
                    print_slow("En fouillant dans le coffre la seule chose que %s trouve est une vieille carte Uno" % joueur.nom, 0.01)
                    time.sleep(1)
                    joueur.inventaire.update(carte_uno)
                    print("\033[32mC'est quoi cette vieille carte toute moisie, quest-ce que tu veux faire de cette merde ? Tirons nous d'ici %s\033[0m" % joueur.rn)
                    joueur.Universite = True 
                    test_c = 'non'          
                else : 
                    print("Ce n'est pas la bonne combinaison, peut-etre est-elle écrite quelque part ?")
    else :
        print("\033[32mOn a plus rien a faire ici %s\033[0m" % joueur.rn)

def Epee_nice(joueur):

    if joueur.epee_nice == False :
        print_slow("En entrant dans un batiment étrangement bien conservé ressemblant a un musée %s apperçoit au centre de la piece principale une épée plantée dans un rocher" % joueur.nom, 0.01)
        time.sleep(2)
        afficher_epee_nice()
        print("\033[32mC'est la légendaire épée Nice on raconte qu'elle donnerai une tres grande puissance a quiconque arriverai a la retirer de son socle\033[0m")
        Q = input("Voulez vous retirer l'épée du rocher ?\n> ").lower()
        if Q == 'oui' :
            if joueur.niveau >= 3 :
                print_slow("%s empoigne l'épée et parviens a la retirer plutot facilement comme si elle était plantée dans du beurre et la met dans son sac" % joueur.nom, 0.01)
                joueur.inventaire.update(epee_nice)
                joueur.epee_nice = True
            else :
                print_slow("%s ne semble pas assez fort pour pouvoir retire l'épée nice de son socle" % joueur.nom, 0.01)
        else :
            print("%s décide de tourner les talons et de partir" % joueur.nom)
    else : 
        print("\033[32mOn a plus rien a voir ici partons %s\033[0m" % joueur.rn)

def Metro_des_clodos(joueur):

    if joueur.metro_des_clodos == False :
        print("%s arrive devant une station de metro désafectée qui semble etre le 'métro des clodo' dont vous a parlé la fée bronshit une fois a l'intérieur il n'y a pas de retour en arriere possible" % joueur.nom)
        Q=input("Voulez vous entrer ?\n> ").lower()
        if Q == 'oui' :
            joueur.donjon = True
            print("%s s'avance dans le metro et tombe face a un premier ennemi" % joueur.nom)
            time.sleep(1)
            joueur.etat = 'combat'
            afficher_clodo()
            Combat(joueur, Clodo(joueur))
            print("A peine %s a fini de se debattre avec son premier ennemi qu'un deuxieme lui tombe dessus" % joueur.nom)
            time.sleep(3)
            joueur.etat = 'combat'
            afficher_clodo()
            Combat(joueur, Clodo(joueur))
            print("Apres en avoir fini avec ses deux ennemis %s arrive devant un chateau en carton" % joueur.nom)
            time.sleep(2)
            print("\033[32mOn dirai le chateau du roi des clodos fait attention a toi %s\033[0m" % joueur.rn)
            Q=input("Voulez vous vous reposer avant d'entrer ?\n> ").lower()
            if Q == 'oui' :
                Repos(joueur)
            time.sleep(1)
            print("%s rentre dans le chateau en carton et se retrouve face a face avec le roi du Métro" % joueur.nom)
            time.sleep(1)
            print("celui attaque %s sans crier garde" % joueur.nom)
            time.sleep(1)
            joueur.etat = 'combat'
            afficher_roi_des_clodos()
            Combat(joueur, Roi_des_clodos(joueur))
            print("Apres avoir vaincu le roi des clodos la fée bronshit l'interroge (le torture) puis viens rendre compte de ce qu'elle a apprit")
            print("\033[32mok %s j'en ai appris plus sur choumeurt, il se terre dans un batiment nommé Hetic au fond de la ville ([2,7]) allons-y sans plus attendre et récupérons le vaccin !\033[0m" % joueur.rn)
            joueur.metro_des_clodos = True
        else :
            print("%s se décourrage et tourne les talons, il faudra bien revenir plus tard" % joueur.nom)
    else :
        print("\033[32mNous n'avons plus rien a faire ici %s allons vite nous occuper de Choumeurt\033[0m" % joueur.rn)

def Hetic(joueur):
    if joueur.metro_des_clodos == True :
        print_slow("%s arrive face au batiment d'Hetic, deumeure de chomel, il ne lui reste qu'un seul pas a faire pour entrer\n " % joueur.nom, 0.01)
        time.sleep(1)
        print("\033[32mOn y est %s allons nous occuper de Chomel, récupérer le vaccin, et enfin sauver l'humanité !\033[0m" % joueur.rn)
        Q = input("Voulez vous entrer ?\n> ")
        if Q == 'oui' :

            print_slow("%s prend son courage a deux mains et se décide a entrer dans le batiment\n" % joueur.nom, 0.01)
            time.sleep(1)
            print_slow("Le batiment est étrangement bien conservé, %s arpente les couloirs a la recherche de son objectif en inspectant soigneusement chaque piece\n" % joueur.nom, 0.01)
            time.sleep(1)
            print_slow("Soudainement %s entend un bruit sourd venant de l'exterieur interompant ainsi ses recherche, il décide de se rendre a la source du bruit sans plus attendre\n" % joueur.nom, 0.01)
            time.sleep(1)
            print_slow("En arrivant a l'exterieur %s se retrouve face a Chomel qui le toise du regard un l'air étonné\n" % joueur.nom, 0.01)
            time.sleep(1)
            print("\033[32mC'est vous choumeurt ? Donnez nous le vaccin raclure ou vous aurez affaire a moi\033[0m")
            time.sleep(1)
            print_slow("Chomel se met a rire, il tient dans sa main un serringue, avant meme que %s ait le temps d'agir Chomel s'injecte la contenu de la serringue et disparait dans une explosion soulevant un nuage de poussiere a travers le quel il est impossible de voir\n" % joueur.nom, 0.01)
            time.sleep(5)
            afficher_chomel()
            print_slow("Lorsque la fumée se dissippe %s se trouve face a un titan de plusieurs metres de haut qui ne lui laisse pas le temps de réfléchir et engage le combat\n" % joueur.nom, 0.01)
            time.sleep(1)
            joueur.etat = 'combat'
            Combat(joueur, Chomel(joueur))
            time.sleep(1)
            print_slow("Grace au pouvoir de la carte Reverse Uno %s parvient a vaincre Ultimate Chomel, et trouve a coté du corps du titant une malette remplie de serringue miraculeusement intacte\n")
            time.sleep(1)
            print("\033Bravo %s tu a réussi a vaincre cette enflure récupere la malette et tirons nous d'ici en vitesse\033[0m" % joueur.nom)

        else : 
            print("\033[32mQuoi ? Maintenant que nous y sommes tu décide de fuir comme un lache ? Il va faloir affronter notre destin un jour ou l'autre %s\033[0m" % joueur.rn)
    else :
        print("%s s'enfonce dans la ville mais il serait préférable de faire demi-tour" % joueur.nom)

def Evenement(joueur) :
    
    test = randint(1,3)
    if test == 1 :
        print("En explorant un batiment abandonné celui-ci commence a s'écrouler sur %s" % joueur.nom)
        degats = randint(0,4)
        joueur.vie -= degats
        print("%s se blesse dans la précipitation et perd %i pv" % (joueur.nom, degats))

    elif test == 2 :
        pass

    else : 
        pass

def Jeu():

    J1 = Joueur()
    Map = initialisation_map()
    J1.nom = input("Quel est votre nom ? ")

    print_slow("il y a peu, un virus mondial a décimé la quasi-totalité de la planète à cause d'un gars qui a mangé un écureuil ou un truc comme ça, aucun vaccin n’a été trouvé et 99% des chercheurs sont morts. Ce monde est apocalyptique, il vous sera difficile de survivre seul.\n", 0.015)
    time.sleep(2)

    print_slow("Vous vous réveillez d’une longue sieste, vous regardez votre journal de poche electroconnecté, il indique 3 février 2077,  position : ville Poitiers, vous vous levez et ouvrez la fenêtre..\n", 0.015)
    time.sleep(2)

    print_slow("Au loin, entre les débris des autres immeubles écroulés vous parvenez à distinguer une personne aussi haute que 3 pommes, elle se fait agresser par un bandit, elle à l’air en danger, souhaitez vous l’aider? (oui/non)\n", 0.015)

    Q1_intro = input("> ").lower()

    if(Q1_intro == 'oui'):

        J1.donjon = True
        J1.etat='combat'
        Afficher_bandit()
        Combat(J1, Bandit(J1))
        time.sleep(1)
        J1.donjon = False
        afficher_bronshit()
        print("\033[32mMerci de ton aide, meme si je me débrouillais tres bien par moi meme, je suis la fée bronshit et toi ton pseudo %s je m'en fout je vais t'appeller %s, j'ai besoin de quelqu'un pour m'accompagner dans une mission de la plus haute importance, va-tu venir avec moi ?\033[0m" % (J1.nom, J1.rn))
        Q2_intro="canard"        
        while (Q2_intro != 'oui'):

            Q2_intro=input("Voulez vous l'aider ? (oui/non) : ").lower()
            if (Q2_intro != 'oui'):
                print("\033[32mPourquoi tu ne veux pas pas m'aider ? **Elle vous attache à un arbre** Ecoute, je me suis fait dérober un vaccin qui pourra sauver l'humanité, j'ai besoin d'une personne qui pourra m'aider à retrouver ce vaccin, je sais déjà qui est la personne qui m'a volé, son nom est 'choumeurt' tant que tu ne voudras pas m'aider je te laisserai attaché là et un bandit viendra te dépouiller ou peut être les loups.. qui sait ! Ahahaha.\033[0m")

        print("\033[32mJ'ai besoin d'une personne qui fonce dans le tas sans réfléchir, ça peut servir.\nBon alors, je me suis fait dérober par un certain 'choumeurt', ouais c'est son nom, un vaccin capable de sauver l'humanité, il faut qu'on le retrouve à tout prix !\nOn va commencer par partir receuillir des informations sur ce mec\nPense a te reposer régulierement et ainsi éviter une mort stupide\033[0m")

        print("Tapez 'aide' pour avoir une liste des commandes disponibles")

        while(J1.vie > 0):
            print("Vous etes en %s" % J1.position)
            ligne = input("> ").lower()
            if ligne == 'etat' :
                Etat(J1)
            elif ligne == 'reposer' :
                Repos(J1)
            elif ligne == 'explorer' :
                Ev = Exploration(J1, Map)
                if Ev == 'combat' :
                    lancer_combat_random(J1)
                elif Ev == 'evenement' :
                    Evenement(J1)
                elif Ev == 'Uno' :
                    Universite(J1)
                elif Ev == 'epee nice' :
                    Epee_nice(J1)
                elif Ev == 'metro des clodos' :
                    Metro_des_clodos(J1)
                elif Ev == 'Hetic' :
                    Hetic(J1)
            elif ligne == 'sauvegarder' :
                Sauvegarder(J1)
            elif ligne == 'quitter' :
                Quitter(J1)
            elif ligne == 'aide' :
                Aide(J1)
            elif ligne == 'inventaire' :
                Afficher_inventaire(J1, 0)
            else :
                print("%s ne comprend pas la suggestion" % J1.nom)

    else : 

        print("Vous décidez que c'est pas votre probleme et retournez vous coucher")
        time.sleep(2)
        webbrowser.open('https://www.youtube.com/watch?v=_amuu7ekAPM', new=1)

def Menu():

    afficher_poitiers()

    choix = False
    while choix == False :

        print_slow("1. Jouer\n", 0.01)
        print_slow("2. Charger\n", 0.01)
        print_slow("3. Credits\n", 0.01)
        print_slow("4. Musique (pour l'immersion)\n", 0.01)
        print_slow("5. Poitiers (pour encore plus d'immersion)\n", 0.01)
        print_slow("6. Quitter \n", 0.01)

        if platform.system() == 'Darwin' :
            q=input("T'es vraiment sur MAC ?")
            if q=='oui' :
                webbrowser.open('https://www.microsoft.com/fr-fr/windows/get-windows-10', new=1)
            else :
                print("tu mens j'ai acces a toute tes données")
                webbrowser.open('https://www.microsoft.com/fr-fr/windows/get-windows-10', new=1)

        reponse = input("> ").lower()

        if (reponse.isnumeric() and int(reponse) == 1) or \
          (not reponse.isnumeric() and reponse== 'jouer'):            
            Jeu()

        elif (reponse.isnumeric() and int(reponse) == 3) or \
          (not reponse.isnumeric() and reponse== 'credits'):
            print_slow("By Alexandre Thibord, ", 0.01)
            print_slow("Théo Wizman, ", 0.01)
            print_slow("Sammy Ferrier\n", 0.01)
    
        elif (reponse.isnumeric() and int(reponse) == 2) or \
          (not reponse.isnumeric() and reponse== 'charger'):
            #charger()
            pass

        elif (reponse.isnumeric() and int(reponse) == 6) or \
          (not reponse.isnumeric() and reponse== 'quitter'):            
            choix = True

        elif (reponse.isnumeric() and int(reponse) == 4) or \
          (not reponse.isnumeric() and reponse== 'musique'):            
            webbrowser.open('https://www.youtube.com/watch?v=MBIKBy_B24o', new=74)

        elif (reponse.isnumeric() and int(reponse) == 5) or \
          (not reponse.isnumeric() and reponse== 'poitiers'):    
            afficher_steph()        
            lore_poitiers()
            afficher_pepe_ok()
            afficher_poitiers()

        else:
            print("Veuillez vérifier votre orthographe ou choisir un numéro valide")

Menu()

