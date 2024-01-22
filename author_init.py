from pygit2.repository import Repository
from pygit2 import discover_repository, Signature
import os
import sys

args = sys.argv
repo_name = args[1]
path = os.path.abspath("./")

if len(args) < 2:
    print("Please specify the name of author!")
    os._exit(1)

isPresent = discover_repository(path)

if not isPresent:
    msg = """    Respository not present.
    Run repo_init.py {name} to create a repository.
    Then change to that directory.
    """
    print(msg)
    os._exit(1)

repo = Repository(path)
isBranch = repo.branches.get(repo_name)

if isBranch:
    print(f"Branch {repo_name} already exists!")
    os._exit(1)

email = f"{repo_name}@email.com"
msg = f"Author {repo_name} initialized"
tree = repo.get("4b825dc642cb6eb9a060e54bf8d69288fbee4904").id
author   = Signature(repo_name, email)
commiiter = Signature(repo_name, email)
refsHeads = f"refs/heads/{repo_name}"

repo.create_commit(refsHeads, 
                   author, 
                   commiiter, 
                   msg,
                   tree, 
                   [])