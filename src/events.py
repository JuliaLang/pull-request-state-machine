import github

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
    # TODO: use the commit SHA to look up the corresponding pull request number
    print(f'on_status: {state}, {event}, {action}')
    return state
