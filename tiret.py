import json
import requests

# Temporaire
from sys import argv

from common_keys import\
	KEY_DESC,\
	KEY_LANG,\
	KEY_NAME
from repository import Repository


_KEY_STARGAZERS = "stargazers_count"

_PATH_REPOS = "https://api.github.com/repos/"
_SLASH = "/"


def fetch_repo_info(owner, repo, username, token):
	auth_couple = (username, token)
	repo_url = _PATH_REPOS + owner + _SLASH + repo
	repo_response = requests.get(repo_url, auth=auth_couple)
	repo_data = json.loads(repo_response.content)

	name = repo_data.get(KEY_NAME)
	description = repo_data.get(KEY_DESC)
	stars = repo_data.get(_KEY_STARGAZERS)
	languages = _fetch_repo_languages(repo_url, auth_couple)
	repo = Repository(name, description, stars, languages)

	return repo


def _fetch_repo_languages(repo_url, auth_couple):
	repo_lang_url = repo_url + _SLASH + KEY_LANG
	lang_response = requests.get(repo_lang_url, auth=auth_couple)
	lang_data = json.loads(lang_response.content)
	languages = tuple(lang_data.keys())
	return languages


repo = fetch_repo_info("ClubCedille", "trema", argv[1], argv[2])
print(repo)
repo2 = eval(repr(repo))
print(repo2)
