import none


class Nettoyage:

   def nettoyage_prix_comptoir_ivoire(self,liste:list):
       cptr = 0
       for i in range(len(liste[0])-1):
           if "\u202f" in str(liste[0][i]["Prix catalogue (FCFA)"]):
               del liste[0][i]
               cptr += 1
               print(f"Nombre de ligne supprimer : {cptr} , prix impossible à lire")


   def nettoyer_prix_marche_lagune(self,liste:list):
         cptr = 0
         cptr1 = 0
         cptr2 = 0
         indice = 0
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
                indice = i

         for i in range(len(liste_valeurs_supprimer)):
             del liste[1][liste_valeurs_supprimer[cptr2-i]]
             print(liste_valeurs_supprimer[cptr2])
             cptr2 -= 1
         print(cptr,cptr1,indice)
