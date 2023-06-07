# Tiret

Cette bibliothèque aide à obtenir les données d'un dépôt GitHub au moyen de
l'API de GitHub.

### Installation

Avant tout, installez les dépendances.
```
pip install -r requirements.txt
```

### Contenu

La classe `Repository` contient plusieurs données sur un dépôt:
* son propriétaire
* son nom
* sa description
* son nombre de problèmes (*issues*) ouverts
* son nombre de duplications (*forks*)
* son nombre de demandes de tirage (*pull requests*) ouvertes
* son nombre d'étoiles
* le nom de ses contributeurs
* son nombre de commits
* la proportion des langages informatiques utilisés

La méthode `as_dict` de `Repository` crée un dictionnaire associant un nom aux
attributs d'un dépôt. Le module `repo_keys` de cette bibliothèque contient les
clés de ce dictionnaire (noms d'attribut) dans les constantes suivantes.
* `KEY_COMMITS`
* `KEY_CONTRIBUTORS`
* `KEY_DESC`
* `KEY_FORKS`
* `KEY_LANG`
* `KEY_NAME`
* `KEY_OPEN_ISSUES`
* `KEY_OWNER`
* `KEY_PULLS`
* `KEY_STARGAZERS`

La fonction `fetch_repo_info` se connecte à l'API de GitHub pour obtenir des
informations sur le dépôt spécifié. L'appelant doit s'authentifier en donnant
son nom d'utilisateur et un jeton d'authentification. `fetch_repo_info` renvoie
un objet `Repository`.

La démo `demo_fetch_repo_info.py` montre comment utiliser `fetch_repo_info`.
Pour afficher ses paramètres, entrez la commande suivante.
```
python demo_fetch_repo_info.py -h
```

La fonction `write_repo_info` appelle `fetch_repo_info` puis enregistre les
données du dépôt en YAML dans un fichier texte. Elle aussi requiert les
informations d'authentification d'un utilisateur de GitHub.

Le script `write_repository.py` permet d'exécuter `write_repo_info` sans
l'importer de cette bibliothèque. Pour afficher ses paramètres, entrez la
commande suivante.
```
python write_repository.py -h
```

### Importation
Pour utiliser cette bibliothèque, téléchargez ce dépôt dans le dossier du code
appelant. Vous pourrez importer les éléments suivants.
* `fetch_repo_info`
* `Repository`
* `repo_keys`
* `write_repo_info`

Exemple:
```
from tiret import\
	fetch_repo_info,\
	repo_keys as rk


repository = fetch_repo_info(...)
repo_dict = repository.as_dict()
repo_name = repo_dict[rk.KEY_NAME]
print(repo_name)
```
