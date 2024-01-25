import os, sys, pygit2
from pygit2 import discover_repository, RemoteCallbacks, Reference
from pygit2.repository import Repository, Signature

path = os.path.abspath("./")

inGitRepo = discover_repository(path)

if not inGitRepo:
    print("Please be inside a git repo to perform repo delivery")
    os._exit(1)

repo = Repository(path)
deliverd_msg = []
for refs in repo.listall_reference_objects():
    # print(refs.name, refs.target)
    if refs.name.startswith("refs/heads"):
        ind = refs.name.rfind("/")
        checkHeadsStr = "refs/delivered"+refs.name[ind:]
        inHeads = repo.references.get(checkHeadsStr)
        print(inHeads)
        if not inHeads:
            deliverd_msg.append((refs.target, checkHeadsStr))
            repo.create_reference(checkHeadsStr, refs.target)
        else:
            if refs.target != inHeads.target:
                inHeads.set_target(refs.target)
                deliverd_msg.append((refs.target, checkHeadsStr))
        
for dmsg in deliverd_msg[::-1]:
    print(dmsg)