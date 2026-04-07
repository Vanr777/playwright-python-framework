import os
from dotenv import load_dotenv

# Load file .env
load_dotenv()

# Ambil data dari .env
BASE_URL = os.getenv('BASE_URL')
USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('USER_PASSWORD')