import csv
import json

from openpyxl import load_workbook

class LireFichier:

   liste_donner = []

   chemin_csv = "chemin.csv"
   def lire_fichier(self,chemin_openpyxl,chemin_csv,chemin_json):
      liste1 = []
      wb = load_workbook(chemin_openpyxl)
      wk = wb.active
      lignes = wk.iter_rows(min_row=3,values_only=True)
      entete = next(lignes)
      for row in lignes:
         liste1.append(dict(zip(entete,row)))
      self.liste_donner.append(liste1)

      with open(chemin_csv,'r',encoding="utf-8") as csvfile:
         liste2 = []
         dict_reader = csv.DictReader(csvfile,delimiter=";")
         for ligne_dict in dict_reader:
            liste2.append(ligne_dict)
         self.liste_donner.append(liste2)


      with open(chemin_json,'r',encoding="utf-8") as jsonfile:
         liste3 = []
         json_values = json.load(jsonfile)
         for json_items in json_values["items"]:
                liste3.append(json_items)
         self.liste_donner.append(liste3)