"""
This demo shows how to use function fetch_repo_info to obtain information about
a GitHub repository. The user must provide their username and one of their
personal access tokens (PATs) to authenticate the requests.
"""


from argparse import ArgumentParser
from sys import exit

from tiret import fetch_repo_info


parser = ArgumentParser(description=__doc__)
parser.add_argument("-o", "--owner",
	help="The username of the repository's owner")
parser.add_argument("-r", "--repository",
	help="The repository's name")
parser.add_argument("-u", "--username",
	help="A GitHub username")
parser.add_argument("-t", "--token",
	help="A PAT owned by user -u")
args = parser.parse_args()

try:
	repo = fetch_repo_info(
		args.owner, args.repository, args.username, args.token)
except RuntimeError as rte:
	print(rte)
	exit()

print("Representation")
print(repo)

print("\nDictionary")
print(repo.as_dict())
