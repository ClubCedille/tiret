import json
import requests

# Temporaire
from sys import argv

from repo_keys import *
from repository import Repository


_KEY_LOGIN = "login"
_KEY_STARGAZERS = "stargazers_count"

_PARAM_PAGE = "?page="
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
	contributors = _fetch_repo_contributors(repo_url, auth_couple)
	commits = _fetch_repo_num_commits(repo_url, auth_couple)
	languages = _fetch_repo_languages(repo_url, auth_couple)
	repo = Repository(
		name, description, stars, contributors, commits, languages)

	return repo


def _fetch_repo_contributors(repo_url, auth_couple):
	contributor_url = repo_url + _SLASH + KEY_CONTRIBUTORS
	contributor_response = requests.get(contributor_url, auth=auth_couple)
	contributor_data = json.loads(contributor_response.content)
	contributors = *(c[_KEY_LOGIN] for c in contributor_data),
	return contributors


def _fetch_repo_languages(repo_url, auth_couple):
	repo_lang_url = repo_url + _SLASH + KEY_LANG
	lang_response = requests.get(repo_lang_url, auth=auth_couple)
	lang_data = json.loads(lang_response.content)
	languages = tuple(lang_data.keys())
	return languages


def _fetch_repo_num_commits(repo_url, auth_couple):
	repo_commit_url = repo_url + _SLASH + KEY_COMMITS + _PARAM_PAGE
	page_num = 1
	num_commits = 0

	while True:
		commit_response = requests.get(
			repo_commit_url+str(page_num), auth=auth_couple)
		commit_data = json.loads(commit_response.content)

		num_commits_page = len(commit_data)
		if num_commits_page < 1:
			break
		num_commits += num_commits_page
		page_num += 1

	return num_commits


repo = fetch_repo_info("ClubCedille", "trema", argv[1], argv[2])

print("Representation")
print(repo)

print("\nDictionary")
print(repo.as_dict())
