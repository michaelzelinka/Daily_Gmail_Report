import os
import requests
from datetime import datetime, timezone

GMAIL_API = "https://gmail.googleapis.com/gmail/v1"
CLIENT_ID = os.getenv("GMAIL_CLIENT_ID")
CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET")

ACCOUNTS = [
    {
        "name": "Account 1",
        "refresh_token": os.getenv("GMAIL_REFRESH_TOKEN_1")
    },
    {
        "name": "Account 2",
        "refresh_token": os.getenv("GMAIL_REFRESH_TOKEN_2")
    }
]

LABELS = {
    "Primary": ["INBOX"],
    "Promotions": ["CATEGORY_PROMOTIONS"],
    "Social": ["CATEGORY_SOCIAL"],
    "Updates": ["CATEGORY_UPDATES"],
    "Forums": ["CATEGORY_FORUMS"],
    "Spam": ["SPAM"]
}


def get_access_token(refresh_token):
    r = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }
    )
    r.raise_for_status()
    return r.json()["access_token"]


def count_messages(token, labels, after_date):
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "labelIds": labels,
        "q": f"after:{after_date}"
    }
    r = requests.get(f"{GMAIL_API}/users/me/messages", headers=headers, params=params)
    r.raise_for_status()
    return r.json().get("resultSizeEstimate", 0)


def build_report():
    today = datetime.now(timezone.utc).strftime("%Y/%m/%d")
    lines = []
    total_all = 0
    total_spam = 0

    for acc in ACCOUNTS:
        token = get_access_token(acc["refresh_token"])
        lines.append(f"{acc['name']}")
        account_total = 0

        for name, labels in LABELS.items():
            count = count_messages(token, labels, today)
            lines.append(f"• {name}: {count}")
            account_total += count
            if name == "Spam":
                total_spam += count

        total_all += account_total
        lines.append(f"→ Total: {account_total}\n")

    lines.append(f"Overall total emails: {total_all}")
    lines.append(f"Overall spam emails: {total_spam}")
    return "\n".join(lines)


def send_email(body):
    print(body)  # (posílání přes Gmail API nebo SMTP můžeš doplnit později)


if __name__ == "__main__":
    report = build_report()
    send_email(report)
