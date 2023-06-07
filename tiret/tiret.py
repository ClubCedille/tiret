import json
from pathlib import Path
import requests
from yaml import dump

from .repo_keys import *
from .repository import Repository


_ENCODING_UTF8 = "utf-8"
_MODE_W = "w"

_KEY_LOGIN = "login"

_PARAM_PAGE = "?page="
_PATH_REPOS = "https://api.github.com/repos/"
_SLASH = "/"


def _count_items_in_pages(url, authentication):
	url += _PARAM_PAGE
	page_num = 1
	num_items = 0

	while True:
		url_to_page = url+str(page_num)
		response = requests.get(url_to_page, auth=authentication)
		_raise_request_exception(url_to_page, response.status_code)
		item_data = json.loads(response.content)

		num_items_on_page = len(item_data)
		if num_items_on_page < 1:
			break
		num_items += num_items_on_page
		page_num += 1

	return num_items


def _ensure_is_path(obj):
	if isinstance(obj, Path):
		return obj

	else:
		return Path(obj)


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
	_raise_request_exception(repo_url, repo_response.status_code)

	repo_data = json.loads(repo_response.content)
	name = repo_data.get(KEY_NAME)
	description = repo_data.get(KEY_DESC)
	forks = repo_data.get(KEY_FORKS)
	stargazers = repo_data.get(KEY_STARGAZERS)

	contributors = _fetch_repo_contributors(repo_url, authentication)
	pulls_url = repo_url + _SLASH + KEY_PULLS
	open_prs = _count_items_in_pages(pulls_url, authentication)
	open_issues = repo_data.get(KEY_OPEN_ISSUES) - open_prs
	commits_url = repo_url + _SLASH + KEY_COMMITS
	commits = _count_items_in_pages(commits_url, authentication)
	languages = _fetch_repo_languages(repo_url, authentication)

	repo = Repository(
		name,
		description,
		open_issues,
		open_prs,
		forks,
		stargazers,
		contributors,
		commits,
		languages)

	return repo


def _fetch_repo_contributors(repo_url, authentication):
	contributor_url = repo_url + _SLASH + KEY_CONTRIBUTORS
	contributor_response = requests.get(contributor_url, auth=authentication)
	_raise_request_exception(contributor_url, contributor_response.status_code)
	contributor_data = json.loads(contributor_response.content)
	contributors = *(c[_KEY_LOGIN] for c in contributor_data),
	return contributors


def _fetch_repo_languages(repo_url, authentication):
	repo_lang_url = repo_url + _SLASH + KEY_LANG
	lang_response = requests.get(repo_lang_url, auth=authentication)
	_raise_request_exception(repo_lang_url, lang_response.status_code)
	lang_data = json.loads(lang_response.content)
	languages = tuple(lang_data.keys())
	return languages


def _raise_request_exception(url, status_code):
	if status_code != 200:
		raise RuntimeError(
			f"Request {url} failed with status code {status_code}.")


def write_repo_info(owner, repo, username, token, o_file):
	"""
	This function obtains information about a GitHub repository from the GitHub
	API and writes the information in YAML in a file. The function requires a
	GitHub username and a personal access token (PAT) to authenticate the
	requests.

	Args:
		owner (str): the name of the repository's owner
		repo (str): the repository's name
		username (str): the name of a GitHub user
		token (str): the user's PAT
		o_file (str or pathlib.Path): the path to the YAML file where the
			repository's information will be written

	Raises:
		RuntimeError: if a request to the GitHub API fails. Status code 401
			can be due to an incorrect username or PAT.
	"""
	o_file = _ensure_is_path(o_file)
	repository = fetch_repo_info(owner, repo, username, token)
	repo_dict = repository.as_dict()

	# Unwanted text added if tuples are recorded
	for key, value in repo_dict.items():
		if isinstance(value, tuple):
			repo_dict[key] = list(value)

	with o_file.open(encoding=_ENCODING_UTF8, mode=_MODE_W) as o_stream:
		dump(repo_dict, o_stream, allow_unicode=True)
