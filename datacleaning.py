import pandas as pd
import requests
import os

# Download files if they don't exist
urls = {
    'Outcomes-a.txt': 'https://physionet.org/files/challenge-2012/1.0.0/Outcomes-a.txt',
    'Outcomes-b.txt': 'https://physionet.org/files/challenge-2012/1.0.0/Outcomes-b.txt'
}

for filename, url in urls.items():
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            f.write(requests.get(url).content)

# Read files separately
outcomes_a = pd.read_csv('Outcomes-a.txt')
outcomes_b = pd.read_csv('Outcomes-b.txt')

print("Outcomes A shape:", outcomes_a.shape)
print("Outcomes B shape:", outcomes_b.shape)
print("\nMissing values in Outcomes A:\n", outcomes_a.isnull().sum())
print("\nMissing values in Outcomes B:\n", outcomes_b.isnull().sum())
