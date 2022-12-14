from sys import argv

from tiret import fetch_repo_info


repo = fetch_repo_info("ClubCedille", "trema", argv[1], argv[2])

print("Representation")
print(repo)

print("\nDictionary")
print(repo.as_dict())
