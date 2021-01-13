from time import *
from random import *

def uno():
    pass

inventory = {

    'épée' : {'nombre': 1, 'dégats' : 2, 'combat' : 'oui', },
    'carte uno' : {'nombre' : 3,  'fonction' : uno(), 'combat' : 'oui'},
    'canette' : {'nombre' : 3, 'combat' : 'non'}

}

def afficher_inventaire(inventaire):

    for clé in inventaire:
        print(clé)
        for clé2, valeur in inventaire[clé].items():
                if type(valeur) is int :
                    print(clé2, valeur)

banane = {'banane' : {'nombre' : 3,}}
chien = {'chien' : {'nombre' : 3}}

def Loot():

    a= randint(1,10)

    if(a>3) :
        if 'banane' in inventory :
            inventory['banane']['nombre'] +=3
        else :
            inventory.update(banane)


afficher_inventaire(inventory)

Loot()

afficher_inventaire(inventory)