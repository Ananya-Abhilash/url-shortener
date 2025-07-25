# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata
from datetime import datetime

# In-memory storage
url_mapping = {}

def store_url(short_code, long_url):
    url_mapping[short_code] = {
        "url": long_url,
        "clicks": 0,
        "created_at": datetime.utcnow()
    }

def get_url(short_code):
    return url_mapping.get(short_code)

def increment_clicks(short_code):
    if short_code in url_mapping:
        url_mapping[short_code]["clicks"] += 1

def get_stats(short_code):
    return url_mapping.get(short_code)
