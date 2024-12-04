import os
from github import Github
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")

REPO_NAME = 'Elnasharr/SW_PRO'

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

milestone_name = "Sprint 1"  # Change as needed
milestone = None
for m in repo.get_milestones(state="open"):
    if m.title == milestone_name:
        milestone = m
        break

if not milestone:
    raise ValueError(f"Milestone '{milestone_name}' not found.")

issues = repo.get_issues(state="closed", milestone=milestone)
issue_dates = [issue.closed_at for issue in issues if issue.closed_at]

df = pd.DataFrame(issue_dates, columns=['Closed At'])
df['Closed At'] = pd.to_datetime(df['Closed At'])
df = df.sort_values(by='Closed At')
df['Date'] = df['Closed At'].dt.date
issue_counts = df['Date'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.plot(issue_counts.index, issue_counts.values, marker='o', linestyle='-')
plt.title('Burndown Chart for Sprint')
plt.xlabel('Date')
plt.ylabel('Number of Issues Closed')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as a PNG file
plt.savefig('burndown_chart.png')