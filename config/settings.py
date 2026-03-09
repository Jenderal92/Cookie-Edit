import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
COOKIE_FILE = os.path.join(DATA_DIR, 'cookies.json')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)