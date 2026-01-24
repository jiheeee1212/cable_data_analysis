import pandas as pd
import src.config as config

def load_csv(path, nrows=None):
    return pd.read_csv(
        path,
        sep=",",
        encoding="utf-8",
        engine="python",
        on_bad_lines="skip",
        nrows=nrows
    )

def load_pickle(path):
    try:
        return pd.read_pickle(path)
    except Exception as e:
        print(f"pd.read_pickle 실패: {e}, 일반 pickle로 시도합니다.")
        with open(path, "rb") as f:
            data = pickle.load(f)
        return pd.DataFrame(data)

def load_interim_file(path=None, file_type="log"):
    if path is None:
        if file_type == "log":
            path = config.INTERIM_LOG_PATH
        elif file_type == "mart":
            path = config.INTERIM_MART_PATH
        else:
            raise ValueError("file_type은 'log' 또는 'mart'여야 합니다.")
    return pd.read_pickle(path)



