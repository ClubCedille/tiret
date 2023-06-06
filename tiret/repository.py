from .repo_keys import *


class Repository:
	"""
	This class contains data about a GitHub repository.
	"""

	def __init__(self,
	    name,
		description,
		open_issues,
		forks,
		stargazers,
		contributors,
		commits,
		languages):
		"""
		The constructor requires all the data that the class is meant to
		contain.

		Args:
			name (str): the repository's name
			description (str): the repository's description
			open_issues (int): the repository's number of open issues
			forks (int): the repository's number of forks
			stargazers (int): the repository's number of stargazers
			contributors: a list, set or tuple containing the username (str) of
				the repository's contributors
			commits (int): the repository's number of commits
			languages: a list, set or tuple containing the name (str) of the
				computer languages used in the repository

		Raises:
			TypeError: if argument contributors or languages is of a wrong type
		"""
		self._name = name
		self._description = description
		self._open_issues = open_issues
		self._forks = forks
		self._stargazers = stargazers
		self._contributors = _ensure_is_tuple(KEY_CONTRIBUTORS, contributors)
		self._commits = commits
		self._languages = _ensure_is_tuple(KEY_LANG, languages)

	def __repr__(self):
		return self.__class__.__name__\
			+ f"('{self._name}', "\
			+ f"'{self._description}', "\
			+ f"{self._open_issues}, "\
			+ f"{self._forks}, "\
			+ f"{self._stargazers}, "\
			+ f"{self._contributors}, "\
			+ f"{self._commits}, "\
			+ f"{self._languages})"

	@property
	def commits(self):
		"""
		int: the repository's number of commits
		"""
		return self._commits

	@property
	def contributors(self):
		"""
		tuple: the username (str) of the repository's contributors
		"""
		return self._contributors

	@property
	def description(self):
		"""
		str: the repository's description
		"""
		return self._description

	@property
	def forks(self):
		"""
		int: the repository's number of forks
		"""
		return self._forks

	@property
	def languages(self):
		"""
		tuple: the name (str) of the computer languages used in the repository
		"""
		return self._languages

	@property
	def name(self):
		"""
		str: the repository's name
		"""
		return self._name

	@property
	def open_issues(self):
		"""
		int: the repository's number of open issues
		"""
		return self._open_issues

	@property
	def stargazers(self):
		"""
		int: the repository's number of stargazers
		"""
		return self._stargazers

	def as_dict(self):
		"""
		Creates a dictionary that maps attribute names (str) to the
		repository's attributes.

		Returns:
			dict: It maps the attributes' name to their value.
		"""
		return {
			KEY_NAME: self._name,
			KEY_DESC: self._description,
			KEY_OPEN_ISSUES: self._open_issues,
			KEY_FORKS: self._forks,
			KEY_STARGAZERS: self._stargazers,
			KEY_CONTRIBUTORS: self._contributors,
			KEY_COMMITS: self._commits,
			KEY_LANG: self._languages}


def _ensure_is_tuple(arg_name, obj):
	if isinstance(obj, tuple):
		return obj

	elif isinstance(obj, (list, set)):
		return tuple(obj)

	else:
		raise TypeError(f"Repository: argument {arg_name} "\
			+ "must be a list, a set or a tuple.")
