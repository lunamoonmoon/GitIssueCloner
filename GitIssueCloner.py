import requests
from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
BASE_URL = 'https://api.github.com'

# Source and destination repositories
SOURCE_REPO = 'owner/source-repo'
DEST_REPO = 'owner/destination-repo'

# Headers for GitHub API requests
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_issues(repo):
    url = f'{BASE_URL}/repos/{repo}/issues'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_comments(repo, issue_number):
    url = f'{BASE_URL}/repos/{repo}/issues/{issue_number}/comments'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def create_issue(repo, title, body, labels, assignees):
    url = f'{BASE_URL}/repos/{repo}/issues'
    data = {'title': title, 'body': body, 'labels': labels, 'assignees': assignees}
    response = requests.post(url, json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def create_comment(repo, issue_number, body):
    url = f'{BASE_URL}/repos/{repo}/issues/{issue_number}/comments'
    data = {'body': body}
    response = requests.post(url, json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def clone_issues():
    issues = get_issues(SOURCE_REPO)
    for issue in issues:
        if 'pull_request' in issue:
            continue  # Skip pull requests
        title = issue['title']
        body = issue['body']
        labels = [label['name'] for label in issue.get('labels', [])]
        assignees = [assignee['login'] for assignee in issue.get('assignees', [])]
        # Create issue in destination repo
        new_issue = create_issue(DEST_REPO, title, body, labels, assignees)
        # Copy comments
        comments = get_comments(SOURCE_REPO, issue['number'])
        for comment in comments:
            create_comment(DEST_REPO, new_issue['number'], comment['body'])

if __name__ == '__main__':
    clone_issues()
