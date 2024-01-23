# Doesn't work - no push support for non-bare repos
import os, sys, pygit2
from pygit2 import discover_repository, RemoteCallbacks, Reference,reference_is_valid_name
from pygit2.repository import Repository,Signature
from pygit2.refspec import Refspec

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

# print(reference_is_valid_name("+refs/heads/*"))
# print(reference_is_valid_name("+refs/heads/alice"))
# print(reference_is_valid_name("refs/remotes/bob/"))

repo = Repository(path)
try:
    remote = repo.remotes[origin]
    refspec = remote.get_refspec(0)
    print(type(refspec))
    print(refspec.direction)
    print(refspec.dst)
    print(refspec.string)
    specs = [f"refs/heads/alice"]
    # callbacks = RemoteCallbacks()
    # callbacks.push_update_reference(refspec.dst,"")
    remote.push(specs)
except Exception as e:
    print(e)
    print(f"remote {origin} does not exists!")  

# For broadcast loop through
# for remotes in repo.remotes:
#     print(remotes.name, remotes.push_url, remotes.url, remotes.fetch_refspecs, remotes.push_refspecs)
