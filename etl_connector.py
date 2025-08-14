import os, requests
from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT"))
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("DB_COLLECTION")
feed_url = os.getenv("FEED_URL")

def fetch_feed(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse_feed(txt):
    lines = txt.splitlines()
    recs = []
    for line in lines:
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split()
        recs.append({
            "ip": parts[0],
            "hostname": parts[1] if len(parts) > 1 else None,
            "feed": "top_attackers",
            "ingested_at": datetime.utcnow()
        })
    return recs

def load_to_mongo(records):
    client = MongoClient(host=db_host, port=db_port)
    db = client[db_name]
    col = db[collection_name]
    if records:
        col.insert_many(records)
        print(f"Inserted {len(records)} records")
    else:
        print("No records to insert")

if __name__ == "__main__":
    try:
        txt = fetch_feed(feed_url)
        records = parse_feed(txt)
        load_to_mongo(records)
    except Exception as e:
        print(f"ETL failed: {e}")
