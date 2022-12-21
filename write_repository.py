"""
This script obtains information about a GitHub repository from the GitHub API
and writes the information in YAML in a file. The user must provide their
username and one of their personal access tokens (PATs) to authenticate the
requests.
"""


from argparse import ArgumentParser
from sys import exit

from tiret import write_repo_info


parser = ArgumentParser(description=__doc__)
parser.add_argument("-o", "--owner", required=True,
	help="The username of the repository's owner")
parser.add_argument("-r", "--repository", required=True,
	help="The repository's name")
parser.add_argument("-u", "--username", required=True,
	help="A GitHub username")
parser.add_argument("-t", "--token", required=True,
	help="A PAT owned by user -u")
parser.add_argument("-y", "--yaml-output", required=True,
	help="The path to the YAML file where to write the information from -r")
args = parser.parse_args()

try:
	write_repo_info(
		args.owner,
		args.repository,
		args.username,
		args.token,
		args.yaml_output)

except RuntimeError as rte:
	print(rte)
	exit()
