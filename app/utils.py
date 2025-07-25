# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need
import string, random
from urllib.parse import urlparse

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
