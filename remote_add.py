import os, sys, pygit2
from pygit2 import discover_repository
from pygit2.repository import Repository


path = os.path.abspath("./")

args = sys.argv

if len(args) < 2:
    print("Please specify the remote process name!")
    os._exit(1)

remote_name = args[1]

if len(args) < 3:
    print("Please also specify remote url")
    os._exit(1)

remote_url = args[2]


isValidGit = discover_repository(path)

if not isValidGit:
    print(f"Please be in a valid git repo. You are currently in {path}. It does not have .git folder.")
    os._exit(1)

repo = Repository(path)

isRemotePresent = None
try:
    isRemotePresent = repo.remotes[remote_name]
except:
    pass

existsUrl = False
existsRepoWithUrl = None
for remote_repo in repo.remotes:
    if remote_repo.url  == remote_url:
        existsUrl = True
        existsRepoWithUrl = remote_repo.name
        break

sameUrl = False
if existsUrl:
    warn = f"""
    There is remote {existsRepoWithUrl} with url {remote_url}.
    Do you want to add another remote name with same url (yes/no):
    """
    inp = input(warn)
    if inp == "yes":
        repo.remotes.create(remote_name, remote_url)
        print(f"{remote_name} remote added with same url: {remote_url}")
        os._exit(1)

if not isRemotePresent:
    repo.remotes.create(remote_name, remote_url)
    print(f"{remote_name} remote added!")
else:
    print(f"{remote_name} already exists!")
