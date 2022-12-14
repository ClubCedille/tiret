from common_keys import *


_KEY_STARS = "stars"


class Repository:
	"""
	This class gathers data about one GitHub repository.
	"""

	def __init__(self, name, description, stars, contributors, languages):
		"""
		The constructor requires all the data that the class is meant to
		contain.

		Args:
			name (str): the repository's name
			description (str): the repository's description
			stars (int): the repository's number of stars
			contributors: a list, set or tuple containing the username (str) of
				the repository's contributors
			languages: a list, set or tuple of the computer languages (str)
				used in the repository
		"""
		self._name = name
		self._description = description
		self._stars = stars
		self._contributors = _ensure_is_tuple(contributors)
		self._languages = _ensure_is_tuple(languages)

	def __repr__(self):
		return self.__class__.__name__\
			+ f"(\"{self._name}\", \"{self._description}\", "\
			+ f"{self._stars}, {self._contributors}, {self._languages})"

	@property
	def contributors(self):
		"""
		tuple: the username (str) of this repository's contributors
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
		Creates a dictionary that maps attribute names (strings) to this
		object's attributes.

		Returns:
			dict: It maps the attributes' name to their value.
		"""
		return {
			KEY_NAME: self._name,
			KEY_DESC: self._description,
			_KEY_STARS: self._stars,
			KEY_CONTRIBUTORS: self._contributors,
			KEY_LANG: self._languages
		}


def _ensure_is_tuple(obj):
	if isinstance(obj, tuple):
		return obj

	else:
		return obj
