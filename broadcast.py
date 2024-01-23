from pygit2.repository import Repository
from pygit2 import discover_repository, Signature
import os
import sys
from subprocess import call

args = sys.argv

if len(args) < 2:
    print("Please specify a message to broadcast!")
    os._exit(1)

message = " ".join(args[1:])

path = os.path.abspath("./")
ind = path.rfind("/")
push_path = path[:ind]

isValid = discover_repository(path)

if not isValid:
    print("Please be inside a git repo, to broadcast the message")
    os._exit(1)

f = open(".git/git-cb","r")
author = f.read().rstrip()


# author-append
call(["python3", push_path+"/pyGitScripts/author_append.py", author, message])

repo = Repository(path)

# push to remotes
for remote in repo.remotes:
    r_name = remote.name
    call(["python3",push_path+"/pyGitScripts/repo_push2.py",r_name])