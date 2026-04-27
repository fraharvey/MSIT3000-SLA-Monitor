# IT Request Tracker - SLA Monitor Runbook

## Purpose
Automated monitoring of Jira tickets to flag tickets older than 48 hours.

## Requirements
- Python 3.14 (or any Python 3.x)
- Internet access to Jira Cloud (port 443)
- Valid Jira API token

## Verify Python Version
```bash
python --version
# Should show: Python 3.14.0