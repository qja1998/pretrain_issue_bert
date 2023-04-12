from github import Github
from tqdm import tqdm

# Authenticate with GitHub API using personal access token
g = Github("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")

# Get the VS Code repository object
repo = g.get_repo("microsoft/vscode")

# Get all the issues in the repository
issues = repo.get_issues(state="all")
print(issues.totalCount)
############### WRITE DATA #######################################################
import csv

# Iterate through the issues and print their titles

with open("data.csv", "w", newline="", encoding='utf-8') as file:
    for i, issue in tqdm(enumerate(issues), total=issues.totalCount):
        if (i == 5000):
            break

        # line = str(issue.id) + ", " + issue.title
        line = []
        line.append(str(issue.id))

        text = issue.title
        comments = issue.get_comments()
        if comments.totalCount > 0:
            for comment in comments:
                text += '\n' + comment.body
        
        line.append(text)
        writer = csv.writer(file)
        # Write the data to the CSV file
        writer.writerow(line)

# Define the data to write to the CSV file
#data = ["John Smith", "john@example.com", "New York"]