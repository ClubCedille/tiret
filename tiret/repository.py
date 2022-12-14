from .repo_keys import *


class Repository:
	"""
	This class contains data about a GitHub repository.
	"""

	def __init__(self, name, description, stars, contributors, commits, languages):
		"""
		The constructor requires all the data that the class is meant to
		contain.

		Args:
			name (str): the repository's name
			description (str): the repository's description
			stars (int): the repository's number of stars
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
		self._stars = stars
		self._contributors = _ensure_is_tuple(KEY_CONTRIBUTORS, contributors)
		self._commits = commits
		self._languages = _ensure_is_tuple(KEY_LANG, languages)

	def __repr__(self):
		return self.__class__.__name__\
			+ f"(\"{self._name}\", \"{self._description}\", {self._stars}, "\
			+ f"{self._contributors}, {self._commits}, {self._languages})"

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
	def stars(self):
		"""
		int: the repository's number of stars
		"""
		return self._stars

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
			KEY_STARS: self._stars,
			KEY_CONTRIBUTORS: self._contributors,
			KEY_COMMITS: self._commits,
			KEY_LANG: self._languages
		}


def _ensure_is_tuple(arg_name, obj):
	if isinstance(obj, tuple):
		return obj

	elif isinstance(obj, (list, set)):
		return tuple(obj)

	else:
		raise TypeError(f"Repository: argument {arg_name} "\
			+ "must be a list, a set or a tuple.")
