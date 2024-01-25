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

branchP = repo.branches.get(p_name)
if not branchP:
    print(f"{p_name} branch is not present. Please run authon_init.py inside git repo.")
    os._exit(1)

headsPname = "refs/heads/"+p_name

ps = set()
parents = []

for refs in repo.listall_reference_objects():
    if refs.name.startswith("refs/heads"):
        if refs.name == headsPname:
            parents.insert(0, refs.target)
        else:
            parents.append(refs.target)
# print(parents)

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

