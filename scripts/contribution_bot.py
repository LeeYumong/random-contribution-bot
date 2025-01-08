import os
import random
import datetime

# Generate a random number of contributions for the day
NUM_COMMITS = random.randint(1, 3)  # Random 1-3 commits per day

# Simulate commits on random past dates
for i in range(NUM_COMMITS):
    date = (datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))).date()
    commit_message = f"Random contribution on {date}"
    filename = f"contribution-{date}.txt"

    # Create a file to represent the contribution
    with open(filename, 'w') as file:
        file.write(commit_message)
    
    # Add and commit the file with a fake commit date
    os.system(f'git add {filename}')
    os.system(f'git commit --date="{date}T12:00:00" -m "{commit_message}"')

# Push changes
os.system('git push')
