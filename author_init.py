from pygit2.repository import Repository
from pygit2 import discover_repository, Signature
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_SORT_NONE
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
    msg = f"""    You are not inside the git repo.
    you are currently in dir - {path}.
    Run `repo_init.py 'name'` to create a repository.
    Then change to that directory. Then run
    `author_init.py 'name'`
    """
    print(msg)
    os._exit(1)

repo = Repository(path)
isBranch = repo.branches.get(repo_name)

if isBranch:
    print(f"Branch {repo_name} already exists!")
    os._exit(1)

pInit = ""
if len(args) >= 3:
    pInit = " "+args[2]

with open(path+"/.git/git-cb","r") as f:
    hash = f.read().split("\n")[-1]

    if hash != "":
        commit = repo.revparse_single(hash)
        # print(commit.message)
        if commit.message.endswith("process-init"):
            print("Can't add author because it's a single process")
            os._exit(1)

email = f"{repo_name}@email.com"
msg = f"Author '{repo_name}' initialized."+pInit
tree = repo.get("4b825dc642cb6eb9a060e54bf8d69288fbee4904").id
author   = Signature(repo_name, email)
commiiter = Signature(repo_name, email)
refsHeads = f"refs/heads/{repo_name}"

firstHash = repo.create_commit(refsHeads, 
                   author, 
                   commiiter, 
                   msg,
                   tree, 
                   [])

newmsg = msg+" in repo "+path

with open(path+"/.git/git-cb","+a") as f:
    # print(f.read())
    hash = f.read().split("\n")[-1]
    # print(hash)
    if hash != "":
        f.write(str(firstHash))
    else:
        pass
        # print("not able to write")

print(repo_name)
print(firstHash)
print(newmsg)
