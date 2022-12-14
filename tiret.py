import json
import requests

# Temporaire
from sys import argv


_KEY_DESC =  "description"
_KEY_LANG = "languages"
_KEY_NAME = "name"
_KEY_STARS = "stargazers_count"

_PATH_REPOS = "https://api.github.com/repos/"
_SLASH = "/"


def fetch_repo_info(owner, repo, username, token):
	repo_url = _PATH_REPOS + owner + _SLASH + repo
	repo_response = requests.get(repo_url, auth=(username, token))
	repo_data = json.loads(repo_response.content)
	repo = _repo_from_api_data(repo_data)


def _repo_from_api_data(repo_data):
	name = repo_data.get(_KEY_NAME)
	description = repo_data.get(_KEY_DESC)
	stars = repo_data.get(_KEY_STARS)
	languages = repo_data.get(_KEY_LANG)
	print(name)
	print(description)
	print(stars)
	print(languages)


fetch_repo_info("ClubCedille", "tiret", argv[1], argv[2])
