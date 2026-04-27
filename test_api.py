import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")

# Use older API endpoint (rest/api/2 instead of /3)
url = f"{JIRA_URL}/rest/api/2/search"

auth = (JIRA_EMAIL, JIRA_TOKEN)

# Simple query to get all issues
query = {
    "jql": "project = ITRT",
    "maxResults": 10
}

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Connecting to Jira...")

try:
    response = requests.get(url, auth=auth, params=query, timeout=30)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"[SUCCESS] Found {len(data.get('issues', []))} issues")
        for issue in data.get('issues', []):
            print(f"  - {issue['key']}: {issue['fields']['summary']}")
    else:
        print(f"[ERROR] {response.text[:200]}")
        
except Exception as e:
    print(f"[ERROR] {e}")