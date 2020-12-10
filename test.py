import github 
import os

client = github.Github(os.getenv('GITHUB_TOKEN'))
repo = client.get_repo("JuliaMisc/julia-for-testing")
pr = repo.get_pull(1)
set_state(pr, "needs_changes")
