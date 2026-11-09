
from LireFichier import *
from Nettoyage import *
import config

class Rapprochement:

  def rapprochement_produit(self):
      lire = LireFichier()
      nettoyage = Nettoyage()
      lire.lire_fichier(config.CHEMIN_EXCEL,config.CHEMIN_CSV,config.CHEMIN_JSON,config.CHEMIN_REFERENCE)
      nettoyage.nettoyer_prix_marche_lagune(lire.liste_donner)
      nettoyage.nettoyage_prix_comptoir_ivoire(lire.liste_donner)

      for i in range(len(lire.liste_produit)):
          for j in range(len(lire.liste_donner[0])):
              if len(set(lire.liste_produit[i]["nom"].split()) & set(lire.liste_donner[0][j]["Article"].split())) >= 1:
                  lire.liste_produit[i]


#rapprochement = Rapprochement()
#rapprochement.rapprochement_produit()