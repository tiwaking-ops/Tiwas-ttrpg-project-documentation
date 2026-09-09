import os
import requests
from datetime import datetime, timezone

APP_ID = os.environ["LARK_APP_ID"]
APP_SECRET = os.environ["LARK_APP_SECRET"]

APP_TOKEN = "KlMxbfG8IaJLAMsqI7pjrHoXpvg"
TABLE_ID = "tblkcYUB9Csrxltg"

# --------------------------------------------------
# 1. Authenticate
# --------------------------------------------------

auth_url = "https://open.larksuite.com/open-apis/auth/v3/tenant_access_token/internal"

auth_response = requests.post(
    auth_url,
    json={
        "app_id": APP_ID,
        "app_secret": APP_SECRET,
    },
)

auth_data = auth_response.json()

if auth_data.get("code") != 0:
    print("Authentication failed:")
    print(auth_data)
    raise SystemExit(1)

tenant_access_token = auth_data["tenant_access_token"]

print("Authentication: SUCCESS")

# --------------------------------------------------
# 2. Create exactly ONE test record
# --------------------------------------------------

records_url = (
    f"https://open.larksuite.com/open-apis/bitable/v1/apps/"
    f"{APP_TOKEN}/tables/{TABLE_ID}/records"
)

headers = {
    "Authorization": f"Bearer {tenant_access_token}",
    "Content-Type": "application/json",
}

test_record = {
    "fields": {
        "DEC ID": "TEST-001",
        "Subject": "Lark API Integration Test",
        "Subsystem": "INTEGRATION-TEST",
        "Status": "TEST",
        "Authority Class": "TEST",
        "Decision": "TEST RECORD — NOT A CANONICAL TIWAS DECISION",
        "Source Document": "Lark API Integration Test",
        "Evidence": "Created automatically by test_lark.py to verify Lark Base write access.",
        "Date": int(datetime.now(timezone.utc).timestamp() * 1000),
        "Designer Action": "DELETE AFTER API TEST",
        "Promotion State": "TEST",
        "Last Sync": int(datetime.now(timezone.utc).timestamp() * 1000),
    }
}

response = requests.post(
    records_url,
    headers=headers,
    json=test_record,
)

print("Create record HTTP status:", response.status_code)
print("Create record response:")
print(response.text)