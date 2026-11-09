


class Nettoyage:

   def nettoyage_prix_comptoir_ivoire(self,liste:list):
       for i in range(len(liste[0])-1):
           if "\u202f" in str(liste[0][i]["Prix catalogue (FCFA)"]):
               liste[0][i]["Prix catalogue (FCFA)"] =float(liste[0][i]["Prix catalogue (FCFA)"].replace("\u202f","").strip())


   def nettoyer_prix_marche_lagune(self,liste:list):
         cptr = 0
         cptr1 = 0
         cptr2 = 0
         cptr3 = 0
         liste_valeurs_supprimer =  []
         for i in range(len(liste[1])):
            if "\u202f" in liste[1][i]["prix"] :
              liste[1][i]["prix"]  =float(liste[1][i]["prix"].replace("\u202f","").replace("FCFA","").strip())
            elif "Prix sur demande" in  str(liste[1][i]["prix"]):
               liste_valeurs_supprimer.append(i)
               cptr += 1
            elif "" in str(liste[1][i]["prix"]):
                liste_valeurs_supprimer.append(i)
                cptr1 += 1
            #Fonctionnaliter inachever ! je reviendrais dessus car l'occurence se repète deux fois dans la boucle se qui n'est pas normal
            if liste[1].count(liste[1][i]) > 1:
                liste_valeurs_supprimer.append(i)
                cptr2 += 1
         #print(liste_valeurs_supprimer)
         #On supprime les mauvais élément ici
         for i in range(len(liste_valeurs_supprimer)):
            del liste[1][liste_valeurs_supprimer[i]-cptr3]
            cptr3 += 1

         print(f"{cptr} prix illisible !")
         print(f"{cptr1} prix manquant !")
         print(f"{cptr2} doublon supprimer !")



