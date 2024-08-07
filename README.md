# GitHub Issue Cloning Tool

## Overview
This tool is designed to clone GitHub issues from one repository to another. It copies issues along with their comments and other details, allowing you to replicate issue tracking between repositories.

## Features
- Clone issues from one repository to another
- Copy issue comments and labels
- Supports both open and closed issues

## Prerequisites
Before you begin, ensure you have the following:

- Python 3.x installed
- `requests` library installed (`pip3 install requests`)
- `dotenv` library installed (`pip3 install python-dotenv`)
- A GitHub personal access token with the `repo` scope

## How to Use this Tool
1. **Install and Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/issue-cloning-tool.git
   cd issue-cloning-tool
2. **Create PAT**
    Create a github personal access token by going to profile > settings > developer settings > tokens > create
    create an .env file with ```bash touch .env
    ```bash
    GITHUB_TOKEN=your_personal_access_token
3. **Enter Repo Names**
    Add source and destination repos to the .env file
    ```bash
    SOURCE_REPO=owner_name/your_source_repo
    DEST_REPO=owner_name/your_destination_repo
4. **Run the Script**
    Run with python3 cloner.py
