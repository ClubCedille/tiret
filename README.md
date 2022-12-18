# tiret

Cette bibliothèque aide à obtenir les données d'un dépôt GitHub au moyen de
l'API de GitHub.

La classe `Repository` contient plusieurs données sur un dépôt:
* son nom
* sa description
* son nombre d'étoiles
* le nom de ses contributeurs
* son nombre de commits
* les langages informatiques utilisés

La fonction `fetch_repo_info` se connecte à l'API de GitHub pour obtenir des
informations sur le dépôt spécifié. L'appelant doit s'authentifier en donnant
son nom d'utilisateur et un jeton d'authentification (PAT). `fetch_repo_info`
renvoie un objet `Repository`.

Pour connaître les paramètres de la démo, entrez la commande suivante.
```
python demo.py -h
```
