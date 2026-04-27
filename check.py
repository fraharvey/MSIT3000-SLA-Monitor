import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://KAN.atlassian.net/rest/api/3/project"
auth = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_TOKEN"))

response = requests.get(url, auth=auth)
print("Status:", response.status_code)
if response.status_code == 200:
    for project in response.json():
        print(f"Name: {project['name']} | Key: {project['key']}")
else:
    print("Error:", response.text)