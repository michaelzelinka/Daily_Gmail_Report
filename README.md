# Daily_Gmail_Report


Overview
--------

Daily Gmail Category Report is an automated project that generates a daily summary of incoming emails across two Gmail accounts. The report breaks messages down using Gmail’s native categories such as Primary, Promotions, Social, Updates, Forums, and Spam.

The report is delivered automatically once per day and is designed to provide objective insight into email volume without changing or manipulating any messages.

Key Features
------------

- Daily automated execution using GitHub Actions (cron based)
- Supports two independent Gmail accounts
- Uses official Gmail API (no scraping, no IMAP)
- Categorizes emails using Gmail labels
- Generates a simple and readable daily report
- Security-first design (OAuth refresh tokens, secrets stored safely)

Categorized Metrics
-------------------

The report includes counts for the following Gmail categories:

- Primary
- Promotions
- Social
- Updates
- Forums
- Spam

Each account is listed separately, followed by an overall daily total.

Technology Stack
----------------

- Python 3
- Gmail API
- OAuth 2.0 (Desktop App flow)
- GitHub Actions

Architecture
------------

1. GitHub Actions triggers the workflow once per day
2. Python script refreshes Gmail API access tokens
3. Gmail API is queried for message counts by label
4. Daily report is generated
5. Report is sent via email

Security Model
--------------

- OAuth Desktop App client
- Long-lived refresh tokens
- No passwords stored
- Secrets kept in GitHub Actions secrets
- No local credentials committed to the repository

Deployment
----------

The solution is intended to run fully serverless via GitHub Actions. No persistent infrastructure is required.

Customization Options
---------------------

Possible future extensions include:

- Weekly or monthly trend analysis
- Threshold alerts for spam volume
- Per-category percentage comparisons
- Integration with additional inboxes

License
-------

MIT License

This project is intended as a practical personal automation tool and a reference implementation for Gmail API integrations.
