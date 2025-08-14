# 📡 DShield Top Attackers ETL Connector

## Overview
This project implements a custom **ETL (Extract → Transform → Load)** pipeline in Python to ingest the **Top Attackers** data from the [DShield Internet Storm Center](https://www.dshield.org) feed into MongoDB.

**Connector Details:**
- **Name:** DShield Top Attackers
- **Base URL:** https://feeds.dshield.org
- **Endpoint:** /feeds/top10.txt
- **Format:** TXT
- **Authentication:** None (public feed)

---

## 📂 Project Structure
/etl_connector.py # Main ETL script
/.env # Local credentials and config (ignored in Git)
/ENV_TEMPLATE # Placeholder environment variables
/requirements.txt # Python dependencies
/README.md # Documentation
/.gitignore # Files/folders to ignore


## ⚙️ Environment Setup

### 1. Clone the repository
git clone <repo-url>
cd <repo-folder>

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt


🔑 Environment Variables
For reference, ENV_TEMPLATE contains placeholders only (no real keys).

▶️ Running the ETL Script: python etl_connector.py

Inserted 89 records


📊 Sample MongoDB Output
After running the ETL, check MongoDB:
mongosh
use etl_db
db.dshield_top_raw.find().pretty()

Example document:
{
 "_id": { "$oid": "64f8b7f52eaf8f14b0c8d123" },
 "ip": "45.133.1.23",
 "reports": 1200,
 "attacks": 4500,
 "country": "CN",
 "network": "45.133.1.0/24",
 "ingested_at": { "$date": "2025-08-13T14:30:45Z" }
}
