# tiret

Cette bibliothèque aide à obtenir les données d'un dépôt GitHub au moyen de
l'API de GitHub.

### Installation

Avant tout, installez les dépendances.
```
pip install -r requirements.txt
```

### Contenu

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

Une démo montre comment utiliser `fetch_repo_info`. Pour afficher ses
paramètres, entrez la commande suivante.
```
python demo_fetch_repo_info.py -h
```

La fonction `write_repo_info` appelle `fetch_repo_info` puis enregistre les
données du dépôt dans un fichier YAML. Elle aussi requiert les informations
d'authentification d'un utilisateur de GitHub.

Un script permet d'exécuter `write_repo_info` sans l'importer de cette
bibliothèque. Pour afficher ses paramètres, entrez la commande suivante.
```
python write_repo.py -h
```
