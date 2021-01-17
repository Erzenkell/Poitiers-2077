#Equipement
vieux_baton = {'vieux baton' : {'type': 'arme', 'nombre': 1, 'degats' : 1}}
couteau_rouille = {'couteau rouillé' : {'type': 'arme', 'nombre': 1, 'degats' : 2}}
tesson_de_bouteille = {'tesson de bouteille' : {'type': 'arme', 'nombre': 1, 'degats' : 3}}
epee_nice = {"épée nice" : {'type': 'arme', 'nombre': 1, 'degats' : 6}}

manteau_de_fourrure = {'manteau de fourrure' : {'type' : 'armure', 'nombre' : 1, 'armure' : 2}}
armure_roi_clodos = {'armure du roi des clodos' : {'type' : 'armure', 'nombre' : 1, 'armure' : 3}}

#Objets combat
grenade = {'grenade' : {'type': 'combat', 'nombre' : 1,  'degats' : 5}}

#Consomables
villageoise = {'Villageoise' : {'type': 'consomable', 'nombre' : 1, 'effet' : 10}}
canette_perimee = {'canette périmée' : {'type': 'consomable', 'nombre' : 1, 'effet' : 6}}
banane = {'banane' : {'type': 'consomable', 'nombre' : 1, 'effet' : 4}}

#Carte Uno
carte_uno = {'carte uno' : {'type': 'Uno', 'nombre': 1}}

def Afficher_inventaire(joueur, Ennemi):

    for clé in joueur.inventaire:
        print(clé)
        for clé2, valeur in joueur.inventaire[clé].items():
                if type(valeur) is int :
                    print(clé2, valeur)

    print("Voulez-vous utiliser un objet ?")
    test = input('> ').lower()
    if test == 'oui' :
        print('lequel ?')
        test2 = input('> ').lower()
        if test2 in joueur.inventaire.keys() :
            utiliser_objet(joueur, test2, Ennemi)
            joueur.tour_effectue = True   
    else :
        print('%s perd son temps a fouiller dans son sac' % joueur.nom)

def utiliser_objet(joueur, objet, Ennemi):

    if joueur.inventaire[objet]['type'] == 'arme' :
        print("vous vous équipez de %s" % objet)
        joueur.equipement['arme'] = objet
        joueur.attaque = joueur.inventaire[objet]["degats"]

    elif joueur.inventaire[objet]['type'] == 'armure' :
        print("vous vous équipez de %s" % objet)
        joueur.equipement['armure'] = objet
        joueur.attaque = joueur.inventaire[objet]['armure']

    elif joueur.inventaire[objet]['type'] == 'combat' :
        if joueur.etat == 'combat' :
            print("Vous utilisez %s et infligez %i dégats" % (objet, joueur.inventaire[objet]['degats']))
            Ennemi.vie -= joueur.inventaire[objet]['degats']
            joueur.inventaire[objet]['nombre'] -= 1
        else : 
            print("vous ne pouvez pas utiliser cet objet hors combat")

    elif joueur.inventaire[objet]['type'] == 'consomable' :
        print('vous utilisez %s' % objet)
        joueur.inventaire[objet]['nombre'] -= 1
        joueur.vie += joueur.inventaire[objet]['effet']
        if joueur.vie > joueur.vie_max :
            joueur.vie = joueur.vie_max
    
    elif joueur.inventaire[objet]['type'] == 'Uno' :
        if joueur.etat == 'combat' :
            if Ennemi.nom == 'Denis Chomel' :
                Ennemi.vie = 0
            else :
                print("A quel momment une carte Uno peut etre utile a un combat ?")
        else :
            print("Qu'est-ce que tu veux faire de cette vieille carte moisie maintenant ?")


