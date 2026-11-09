


"""
from LireFichier import *
import config
from Nettoyage import *
lire = LireFichier()
nettoyage = Nettoyage()
lire.lire_fichier(config.CHEMIN_EXCEL,config.CHEMIN_CSV,config.CHEMIN_JSON,config.CHEMIN_REFERENCE)
nettoyage.nettoyage_prix_comptoir_ivoire(lire.liste_donner)
nettoyage.nettoyer_prix_marche_lagune(lire.liste_donner)

for lignes in lire.liste_produit:
    print(lignes["nom"])
"""























"""
print(lire.liste_donner[0][20]["Prix catalogue (FCFA)"]+2000000000)

nettoyage.nettoyage_prix_comptoir_ivoire(lire.liste_donner)

for i in range(len(lire.liste_donner[0])):
    if "\u202f" in str(lire.liste_donner[0][i]["Prix catalogue (FCFA)"]):
              print("trouver ! ")
              print(lire.liste_donner[0][i]["Prix catalogue (FCFA)"])

for i in range(len(lire.liste_donner[0])):
    print(lire.liste_donner[0][i]["Prix catalogue (FCFA)"])


²
nettoyage.nettoyer_prix_marche_lagune(lire.liste_donner)
#print(lire.liste_donner[1][3]['prix'])
for i in range(len(lire.liste_donner[1])):
    print(lire.liste_donner[1][i]["prix"])
"""

