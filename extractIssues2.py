from github import Github, RateLimitExceededException
from tqdm import tqdm
from datetime import datetime, timedelta
import time

# Authenticate with GitHub API using personal access token
g = Github("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")

start_date = datetime(2020, 3, 1, 0, 0)
#end_date = datetime(2023, 4, 1, 0, 0)

# since이후로 데이터를 모음
while True:
    try:
        # Get the VS Code repository object
        repo = g.get_repo("microsoft/vscode")
        issues = repo.get_issues(state="all", since=start_date)#, direction="asc")
        break
    except RateLimitExceededException:
        print("GitHUB API Rate limiting exceeded")
        print("Please wait 1 hour")
        time.sleep(3650)

print(issues.totalCount)
    
############### WRITE DATA #######################################################
import csv


# Iterate through the issues and print their titles

with open("data2.csv", "w", newline="", encoding='utf-8') as file:
    for i, issue in tqdm(enumerate(issues), total=issues.totalCount):
        if i == 40503:
            break
        try:
            line = []
            line.append(str(issue.id))

            text = issue.title
            comments = issue.get_comments()
            for comment in comments:
                if start_date <= comment.created_at:
                    text += '\n' + comment.body
            
        except RateLimitExceededException:
            print("GitHUB API Rate limiting exceeded")
            print("Please wait 1 hour")
            time.sleep(3650)

            line = []
            line.append(str(issue.id))

            text = issue.title
            comments = issue.get_comments()
            for comment in comments:
                if start_date <= comment.created_at:
                    text += '\n' + comment.body
        
        

        line.append(text)
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='',escapechar='\\')
        # Write the data to the CSV file
        writer.writerow(line)


            

# Define the data to write to the CSV file
#data = ["John Smith", "john@example.com", "New York"]