import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




MART_COLUMNS_PATH = os.path.join(BASE_DIR, 'data', 'mart_column_selected.pkl')
TPS_YN_PATH = os.path.join(BASE_DIR, 'data', 'tps_yn_p.pkl')
VOD_LOG_SAMPLE_PATH = os.path.join(BASE_DIR, 'data', 'vod_log_sample.pkl')

FIGURES_PATH = os.path.join(BASE_DIR, 'outputs', 'figures')
TABLES_PATH = os.path.join(BASE_DIR, 'outputs', 'tables')
