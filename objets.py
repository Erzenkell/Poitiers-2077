#Equipement
vieux_baton = {'vieux baton' : {'type': 'arme', 'nombre': 1, 'degats' : 1}}

#Objets combat
grenade = {'grenade' : {'type': 'combat', 'nombre' : 1,  'degats' : 5}}

#Consomables
canette_perimee = {'canette périmée' : {'type': 'consomable', 'nombre' : 1, 'effet' : 5}}
banane = {'banane' : {'type': 'consomable', 'nombre' : 1, 'effet' : 10}}


def Afficher_inventaire(joueur):

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
            utiliser_objet(joueur, test2)
            joueur.tour_effectue = True   
    else :
        print('%s perd son temps a fouiller dans son sac' % joueur.nom)

def utiliser_objet(joueur, objet):

    if joueur.inventaire[objet]['type'] == 'arme' :
        print("vous vous équipez de %s" % objet)
        joueur.equipement['arme'] = objet
        joueur.attaque = joueur.inventaire[objet]["degats"]

    elif joueur.inventaire[objet]['type'] == 'combat' :
        if joueur.etat == 'combat' :
            print("Vous utilisez %s" % objet)
            joueur.inventaire[objet]['nombre'] -= 1
        else : 
            print("vous ne pouvez pas utiliser cet objet hors combat")

    elif joueur.inventaire[objet]['type'] == 'consomable' :
        print('vous utilisez %s' % objet)
        joueur.inventaire[objet]['nombre'] -= 1
        joueur.vie += joueur.inventaire[objet]['effet']
        if joueur.vie > joueur.vie_max :
            joueur.vie = joueur.vie_max