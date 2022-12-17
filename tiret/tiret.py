import json
import requests

from .repo_keys import *
from .repository import Repository


_KEY_LOGIN = "login"
_KEY_STARGAZERS = "stargazers_count"

_PARAM_PAGE = "?page="
_PATH_REPOS = "https://api.github.com/repos/"
_SLASH = "/"


def fetch_repo_info(owner, repo, username, token):
	"""
	This function obtains information about a GitHub repository from the GitHub
	API. It requires a GitHub username and a personal access token (PAT) to
	authenticate the requests.

	Args:
		owner (str): the name of the repository's owner
		repo (str): the repository's name
		username (str): the name of a GitHub user
		token (str): the user's PAT

	Returns:
		Repository: an object containing information about the specified
			repository

	Raises:
		RuntimeError: if a request to the GitHub API fails. Status code 401
			can be due to an incorrect username or PAT.
	"""
	authentication = (username, token)
	repo_url = _PATH_REPOS + owner + _SLASH + repo
	repo_response = requests.get(repo_url, auth=authentication)
	_raise_request_exception(repo_response.status_code)

	repo_data = json.loads(repo_response.content)
	name = repo_data.get(KEY_NAME)
	description = repo_data.get(KEY_DESC)
	stars = repo_data.get(_KEY_STARGAZERS)
	contributors = _fetch_repo_contributors(repo_url, authentication)
	commits = _fetch_repo_num_commits(repo_url, authentication)
	languages = _fetch_repo_languages(repo_url, authentication)
	repo = Repository(
		name, description, stars, contributors, commits, languages)

	return repo


def _fetch_repo_contributors(repo_url, authentication):
	contributor_url = repo_url + _SLASH + KEY_CONTRIBUTORS
	contributor_response = requests.get(contributor_url, auth=authentication)
	_raise_request_exception(contributor_response.status_code)
	contributor_data = json.loads(contributor_response.content)
	contributors = *(c[_KEY_LOGIN] for c in contributor_data),
	return contributors


def _fetch_repo_languages(repo_url, authentication):
	repo_lang_url = repo_url + _SLASH + KEY_LANG
	lang_response = requests.get(repo_lang_url, auth=authentication)
	_raise_request_exception(lang_response.status_code)
	lang_data = json.loads(lang_response.content)
	languages = tuple(lang_data.keys())
	return languages


def _fetch_repo_num_commits(repo_url, authentication):
	repo_commit_url = repo_url + _SLASH + KEY_COMMITS + _PARAM_PAGE
	page_num = 1
	num_commits = 0

	while True:
		commit_response = requests.get(
			repo_commit_url+str(page_num), auth=authentication)
		_raise_request_exception(commit_response.status_code)
		commit_data = json.loads(commit_response.content)

		num_commits_page = len(commit_data)
		if num_commits_page < 1:
			break
		num_commits += num_commits_page
		page_num += 1

	return num_commits


def _raise_request_exception(status_code):
	if status_code != 200:
		raise RuntimeError(
			f"Request to the GitHub API fialed. Status: {status_code}.")
