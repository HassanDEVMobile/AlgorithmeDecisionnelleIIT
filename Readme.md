# Analyse comparative de prix (projet Python)
 
Projet réalisé en **L2** à l'**Institut Ivoirien de Technologie (IIT)**, dans le cadre du module Python (séance 3).
 
> **Le projet n'est pas terminé.** Je suis encore en train d'apprendre et de coder. Ce README explique ce que j'ai déjà fait et ce qu'il me reste à faire.
 
---
 
## C'est quoi ce projet ?
 
Trois boutiques en ligne vendent à peu près les mêmes produits (téléphones, ordinateurs, clés USB, etc.), mais chacune écrit ses données à sa façon :
 
| Boutique | Format du fichier |
|---|---|
| Marché Lagune | CSV |
| Baobab Shop | JSON |
| Comptoir Ivoire | Excel |
 
Il y a aussi un **catalogue de référence** (30 produits, de P01 à P30) qui sert de liste officielle.
 
Le but du programme est de :
 
1. lire les trois fichiers,
2. nettoyer les données (elles ne sont pas propres),
3. retrouver quel produit du catalogue correspond à chaque article de chaque boutique (le **rapprochement**),
4. comparer les prix et dire où acheter.
---
 
## Ce que j'ai déjà fait
 
- [x] **Lecture des fichiers** : Excel, CSV, JSON et catalogue de référence (`LireFichier.py`).
- [x] **Début du nettoyage des prix** (`Nettoyage.py`) :
  - Marché Lagune : transformer un prix écrit en texte (« 102 900 FCFA ») en nombre, et repérer les prix illisibles ou manquants. Le programme affiche le nombre de problèmes trouvés.
  - Comptoir Ivoire : transformer les prix écrits en texte en nombres.
- [x] Un fichier `config.py` qui contient les noms des fichiers de données.
## Ce qui est en cours
 
- [ ] **Nettoyage** : la partie qui supprime les doublons n'est pas finie (je l'ai noté dans le code). Il y a aussi des choses à vérifier dans ma façon de repérer les prix manquants.
- [ ] **Rapprochement** (`Rapprochement.py`) : j'ai commencé avec l'idée de comparer les mots du nom d'un article avec ceux du nom du catalogue. Ce n'est pas terminé et ça ne donne pas encore de résultat.
## Ce qu'il me reste à faire
 
- [ ] Nettoyer les données de Baobab Shop (prix et frais de livraison).
- [ ] Gérer la remise de Comptoir Ivoire dans le prix.
- [ ] Terminer le rapprochement des produits avec le catalogue.
- [ ] Faire le **comparatif** des prix et l'exporter en fichier CSV.
- [ ] Faire la **synthèse** (quelle boutique est la moins chère, où l'écart est le plus grand).
- [ ] Calculer le **panier** de rentrée dans chaque boutique.
- [ ] Étudier l'**historique** des prix et regarder si le Black Friday est vraiment une bonne affaire.
- [ ] Mesurer le **temps d'exécution** et expliquer mes choix de structures de données.
- [ ] Écrire le **journal** des problèmes trouvés dans les données.
- [ ] Remplir `main.py` pour que le programme se lance en une seule fois.
---
 
## Les fichiers du projet
 
| Fichier | À quoi il sert |
|---|---|
| `main.py` | Point de départ du programme. Pour l'instant, il contient seulement mes tests (en commentaire). |
| `config.py` | Les chemins vers les fichiers de données. |
| `LireFichier.py` | Lire les trois fichiers de boutiques et le catalogue. |
| `Nettoyage.py` | Nettoyer les prix. |
| `Rapprochement.py` | Relier les articles des boutiques au catalogue (pas fini). |
| `marche_lagune.csv` | Données de Marché Lagune. |
| `baobab_shop.json` | Données de Baobab Shop. |
| `comptoir_ivoire.xlsx` | Données de Comptoir Ivoire. |
| `catalogue_reference.csv` | Les 30 produits de référence. |
| `historique_prix.csv` | Historique des prix sur un an (pas encore utilisé). |
| `requirement.txt` | La bibliothèque à installer. |
 
---
 
## Ce qu'il faut pour le lancer
 
- Python 3
- La bibliothèque `openpyxl` pour lire le fichier Excel :
```
pip install -r requirement.txt
```
 
Le reste utilise seulement ce qui est déjà dans Python (`csv`, `json`).
 
> Pour l'instant, le programme complet ne se lance pas encore : `main.py` n'est pas terminé. Seules les parties « lecture » et « nettoyage » existent.
 
---
 
## Ce que j'apprends avec ce projet
 
- Lire des fichiers de formats différents (CSV, JSON, Excel).
- Nettoyer des données réelles qui ne sont jamais parfaites.
- Utiliser des listes et des dictionnaires.
- Réfléchir à une méthode avant de coder.
---
 
## Auteur
 
Diabagate Hassane Ilias, étudiant en L2, IIT.
 