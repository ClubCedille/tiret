"""
This demo shows how to use function fetch_repo_info to obtain information about
a GitHub repository. The user must provide the username of the repository's
owner, the repository's name, their own username and one of their personal
access tokens (PATs).
"""


from argparse import ArgumentParser
from sys import argv

from tiret import fetch_repo_info


parser = ArgumentParser(description=__doc__)
parser.add_argument("-o", "--owner",
	help="The username of the repository's owner")
parser.add_argument("-r", "--repository",
	help="The repository's name")
parser.add_argument("-t", "--token",
	help="A PAT owned by user -u")
args = parser.parse_args()

repo = fetch_repo_info(args.owner, args.repository, args.token)

print("Representation")
print(repo)

print("\nDictionary")
print(repo.as_dict())
