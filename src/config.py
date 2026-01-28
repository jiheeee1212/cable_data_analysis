import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
INTERIM_DIR = os.path.join(BASE_DIR, 'data', 'interim')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

MART_RAW_PATH = os.path.join(RAW_DIR, 'mart_raw.csv')
LOG_RAW_PATH = os.path.join(RAW_DIR, 'log_raw.pkl')

LOG_INT_PATH = os.path.join(INTERIM_DIR, 'log_int.pkl')
MART_INT_PATH = os.path.join(INTERIM_DIR, 'mart_int.pkl')
TPS_INT_PATH = os.path.join(INTERIM_DIR, 'tps_int.pkl')

LOG_PRC_PATH = os.path.join(PROCESSED_DIR, 'log_prc.pkl')
MART_PRC_PATH = os.path.join(PROCESSED_DIR, 'mart_prc.pkl')
TPS_PRC_PATH = os.path.join(PROCESSED_DIR, 'tps_prc.pkl')