import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
RAW_MART_PATH = os.path.join(RAW_DIR, 'mart.csv')
RAW_LOG_PATH = os.path.join(RAW_DIR, 'log.pkl')

INTERIM_DIR = os.path.join(BASE_DIR, 'data', 'interim')
INTERIM_LOG_PATH = os.path.join(INTERIM_DIR, 'interim_log.pkl')
INTERIM_MART_PATH = os.path.join(INTERIM_DIR, 'interim_mart.pkl')

