import json
import os

import github

from .events import *

class StateMachineException(Exception):
    pass

LABEL_PREFIX = "state: "

LABELS = {
    "abandoned":     LABEL_PREFIX + "abandoned",
    "accepted":      LABEL_PREFIX + "accepted",
    "ci_failed":     LABEL_PREFIX + "ci failed",
    "ci_passed":     LABEL_PREFIX + "ci passed",
    "initial_state": LABEL_PREFIX + "initial state",
    "done":          LABEL_PREFIX + "done",
    "needs_changes": LABEL_PREFIX + "needs changes",
    "needs_review":  LABEL_PREFIX + "needs review",
    "rejected":      LABEL_PREFIX + "rejected"
}

def state_unchanged(state, event, action, payload):
    return state

def transition_function(state, event, action, payload):
    if event == "pull_request":
        if action == "opened":
            return on_pr_opened
        elif action == "reopened":
            return on_pr_reopened
        elif action == "closed":
            return on_pr_closed
        elif action == "synchronize":
            return on_pr_synchronize
        else:
            print(f'Warning: unsupported action; state={state}, event={event}, action={action}.')
            return state_unchanged
    elif event == "pull_request_review":
        if action == "submitted":
            return on_pr_review_submitted
        elif action == "dismissed":
            return on_pr_review_dismissed
        else:
            print(f'Warning: unsupported action; state={state}, event={event}, action={action}.')
            return state_unchanged
    elif event == "issue_comment":
        if action == "created":
            if false: # TODO: check the payload, and only return `on_pr_comment` if the issue is a pull request
                return on_pr_comment
            else:
                return stay_in_same_state
        else:
            print(f'Warning: unsupported action; state={state}, event={event}, action={action}.')
            return state_unchanged
    elif event == "status":
        return on_status
    else:
        print(f'Warning: unsupported event; state={state}, event={event}, action={action}.')
        return state_unchanged

def commit_to_pull_request(commit):
    prs = list(commit.get_pulls())
    print("commit")
    print(commit)
    print("prs for this commit")
    print(prs)
    if len(prs) == 1:
        return prs[0]
    else:
        raise StateMachineException('Could not identify the PR for this commit')

def get_pull_request(payload):
    if "pull_request" in payload:
        return repo.get_pull(payload["pull_request"]["number"])
    elif:
        commit = repo.get_commit(payload["sha"])
        return commit_to_pull_request(commit)
    else:
        raise StateMachineException('Payload has neither pull_request nor sha')

def determine_new_labels(old_labels, new_state):
    new_state_label = LABELS[new_state]
    current
    "foo".startswith("fo")

def get_state(pull_request):
    pass

def set_state(pull_request, new_state):
    new_state_label = LABELS[new_state]
    print(f'The new state is: {new_state}')
    print(f'The new state label is: {new_state_label}')
    pull_request.add_to_labels(new_state_label)
    current_labels = [x.name for x in pull_request.get_labels()]
    for current_label in current_labels:
        if current_label != new_state_label:
            if current_label.startswith(LABEL_PREFIX):
                try:
                    pull_request.remove_from_label(current_label)
                except Exception as e:
                    print(f'Ignoring exception: {e}')
    return new_state

def machine(client, event, payload):
    repo = client.get_repo(payload["repository"]["full_name"])
    pr = determine_pull_request(payload):
    f = transition_function(state, event, action, payload)
    new_state = f(state, event, action, payload)
    if state != new_state:
        set_state(new_state)
    return 200
