import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv('JIRA_URL')
JIRA_EMAIL = os.getenv('JIRA_EMAIL')
JIRA_TOKEN = os.getenv('JIRA_TOKEN')

jql_query = 'project=KAN'

auth = (JIRA_EMAIL, JIRA_TOKEN)

url = f"{JIRA_URL}/rest/api/3/search/jql"

params = {
    'jql': jql_query,
    'fields': 'summary,created,status',
    'maxResults': 50
}

print(f"Connecting to: {JIRA_URL}")
print(f"Using API: {url}")
print(f"JQL: {jql_query}")

response = requests.get(url, auth=auth, params=params)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    tickets = data.get('issues', [])
    print(f"\nFound {len(tickets)} tickets:\n")
    
    for ticket in tickets:
        key = ticket['key']
        summary = ticket['fields']['summary']
        created_str = ticket['fields']['created']
        
        # Calculate hours since ticket was created
        created_time = datetime.fromisoformat(created_str.replace('Z', '+00:00'))
        current_time = datetime.now().astimezone()
        hours_old = (current_time - created_time).total_seconds() / 3600
        
        # SLA check: 48 hours threshold
        if hours_old > 48:
            print(f" ⚠️ OVERDUE: {key} - {summary} ({hours_old:.0f} hours old)")
        else:
            print(f" ✅ On-time: {key} - {summary} ({hours_old:.0f} hours old)")
else:
    print(f"Error: {response.text}")