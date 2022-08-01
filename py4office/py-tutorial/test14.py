import pandas as pd
import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
data = resp.json()
# print(data)

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues)