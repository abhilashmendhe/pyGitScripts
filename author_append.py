import os, sys, pygit2
from pygit2 import discover_repository
from pygit2.repository import Repository,Signature


path = os.path.abspath("./")

args = sys.argv

if len(args) < 2:
    print("Please specify the process name!")
    os._exit(1)

p_name = args[1]

if len(args) < 3:
    print("Please specify the message!")
    os._exit(1)

msg = " ".join(args[2:])

inGitRepo = discover_repository(path)

if not inGitRepo:
    print("Please be inside a git repo.")
    os._exit(1)

repo = Repository(path)

parents = []

# for refs in repo.
for objs in repo.listall_reference_objects():
    if p_name == objs.resolve().shorthand:
        parents.insert(0, objs.target)
    else:
        parents.append(objs.target)


email = f"{p_name}@email.com"
author   = Signature(p_name, email)
commiiter = Signature(p_name, email)
refsHeads = f"refs/heads/{p_name}"
tree = repo.TreeBuilder().write()

hashhead = repo.create_commit(refsHeads, 
                   author, 
                   commiiter, 
                   msg,
                   tree, 
                   parents)

print(f"{p_name} HEAD {hashhead}")

