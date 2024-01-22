from pygit2.repository import Repository
from pygit2 import discover_repository
import os
import sys

args = sys.argv

if len(args) < 2:
    print("Please specify the name of repo!")
    os._exit(1)

path = os.path.abspath("./") + "/" + args[1]

isPresent = discover_repository(path)

if not isPresent:
    print("Respository not present. Run repo_init.py {name} to create a repository")
    os._exit(1)
