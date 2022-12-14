class Repository:
	"""
	This class gathers data about one GitHub repository.
	"""

	def __init__(self, name, description, stars, languages):
		"""
		The constructor requires all the data that the class is meant to
		contain.

		Args:
			name (str): the repository's name
			description (str): the repository's description
			stars (int): the repository's number of stars
			languages: a list, set or tuple of the computer languages (str)
				used in the repository
		"""
		self._name = name
		self._description = description
		self._stars = stars

		if isinstance(languages, tuple):
			self._languages = languages
		else:
			self._languages = tuple(languages)

	def __repr__(self):
		return self.__class__.__name__\
			+ f"(\"{self._name}\", \"{self._description}\", "\
			+ f"{self._stars}, {self._languages})"

	@property
	def description(self):
		return self._description

	@property
	def languages(self):
		return self._languages

	@property
	def name(self):
		return self._name

	@property
	def stars(self):
		return self.stars
