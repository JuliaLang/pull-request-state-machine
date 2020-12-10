LABEL_PREFIX = "state:"

LABELS = {
    "abandoned":     LABEL_PREFIX + "abandoned",
    "accepted":      LABEL_PREFIX + "accepted",
    "ci_failed":     LABEL_PREFIX + "ci-failed",
    "ci_passed":     LABEL_PREFIX + "ci-passed",
    "initial_state": LABEL_PREFIX + "initial-state",
    "done":          LABEL_PREFIX + "done",
    "needs_changes": LABEL_PREFIX + "needs-changes",
    "needs_review":  LABEL_PREFIX + "needs-review",
    "rejected":      LABEL_PREFIX + "rejected"
}

def set_state(new_state):
    new_label = LABELS[new_state]
    print(f'The new state is: {state}')
    print(f'The new labels is: {new_label}')
    return state

def on_pr_closed(state, event, action, payload):
    print(f'on_pr_closed: {state}, {event}, {action}')
    return state

def on_pr_comment(state, event, action, payload):
    print(f'on_pr_comment: {state}, {event}, {action}')
    return state

def on_pr_opened(state, event, action, payload):
    print(f'on_pr_opened: {state}, {event}, {action}')
    return state

def on_pr_reopened(state, event, action, payload):
    print(f'on_pr_reopened: {state}, {event}, {action}')
    return state

def on_pr_review_dismissed(state, event, action, payload):
    print(f'on_pr_review_dismissed: {state}, {event}, {action}')
    return state

def on_pr_review_submitted(state, event, action, payload):
    print(f'on_pr_review_submitted: {state}, {event}, {action}')
    return state

def on_pr_synchronize(state, event, action, payload):
    print(f'on_pr_synchronize: {state}, {event}, {action}')
    return state

def on_status(state, event, action, payload):
    print(f'on_status: {state}, {event}, {action}')
    return state

def state_unchanged(state, event, action, payload):
    print(f'state_unchanged: {state}, {event}, {action}')
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
            print(f'Warning: unsupported action. state={state}, event={event}, action={action}.')
            return state_unchanged
    elif event == "pull_request_review":
        if action == "submitted":
            return on_pr_review_submitted
        elif action == "dismissed":
            return on_pr_review_dismissed
        else:
            print(f'Warning: unsupported action. state={state}, event={event}, action={action}.')
            return state_unchanged
    elif event == "issue_comment":
        if action == "created":
            if True: # TODO: check the payload, and only return on_pr_comment if the issue is a pull request
                return on_pr_comment
            else:
                return stay_in_same_state
        else:
            print(f'Warning: unsupported action. state={state}, event={event}, action={action}.')
            return state_unchanged
    elif event == "status":
        return on_status
    else:
        print(f'Warning: unsupported event. state={state}, event={event}, action={action}.')
        return state_unchanged

def main():
    f = transition_function(state, event, action, payload)
    new_state = f(state, event, action, payload)
    if state != new_state:
        set_state(new_state)
    return None

if __name__ == "__main__":
    # main()
    pass
