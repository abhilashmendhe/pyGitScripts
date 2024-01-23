import os, sys, pygit2
from pygit2 import discover_repository, RemoteCallbacks, Reference
from pygit2.repository import Repository, Signature

path = os.path.abspath("./")

inGitRepo = discover_repository(path)

if not inGitRepo:
    print("Please be inside a git repo to perform repo merge")
    os._exit(1)

repo = Repository(path)
for refs in repo.listall_reference_objects():
    if refs.name.startswith("refs/remotes"):
        ind = refs.name.rfind("/")
        checkHeadsStr = "refs/heads"+refs.name[ind:]
        inHeads = repo.references.get(checkHeadsStr)
        if not inHeads:
            repo.create_reference(checkHeadsStr, refs.target)
        else:
            if refs.target != inHeads.target:
                inHeads.set_target(refs.target)
                print(refs.name, checkHeadsStr)
        