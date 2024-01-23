import os, sys, pygit2
from pygit2 import discover_repository, RemoteCallbacks
# from pygit2.repository import Repository,Signature
from pygit2.refspec import Refspec
from git import Repo
path = os.path.abspath("./")

args = sys.argv

if len(args) < 2:
    print("Please specify the origin")
    os._exit(1)

origin = args[1]

inGitRepo = discover_repository(path)

if not inGitRepo:
    print("Please be inside a git repo.")
    os._exit(1)

f = open(path+"/.git/git-cb","r")
lbranch = f.read().strip()
f.close()

repo = Repo(path)
try:
    remote = repo.remote(origin)
    name = f"refs/heads/*:refs/remotes/{lbranch}/*"
    remote.push(name)
except Exception as e:
    print(e)

# For broadcast loop through
# for remotes in repo.remotes:
#     print(remotes.name, remotes.push_url, remotes.url, remotes.fetch_refspecs, remotes.push_refspecs)
