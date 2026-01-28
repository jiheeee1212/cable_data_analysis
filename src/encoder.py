import pandas as pd
from src.schema import ASSET_PROD_MAP,SCREEN_TP_MAP,PUBLCTN_MAP

def encode_asset_prod(df: pd.DataFrame):
    df_out = df.copy()
    df_out['asset_prod'] = (
        df_out['asset_prod']
        .map(ASSET_PROD_MAP)
        .fillna(-1)
        .astype("int8")
    )
    return df_out

def encode_screen_tp(df: pd.DataFrame):
    df_out = df.copy()
    df_out["screen_tp"] = (
        df_out["screen_tp"]
        .map(SCREEN_TP_MAP)
        .fillna(-1)
        .astype("int8")
    )
    return df_out

def get_bitmask(value: str):
    if not isinstance(value, str):
        return 0

    bitmask = 0
    parts = {x.strip() for x in value.split(",")}

    for p in parts:
        bit = PUBLCTN_MAP.get(p)
        if bit is not None:
            bitmask |= bit
    return bitmask

def encode_publctn_bit(df: pd.DataFrame):
    df_out = df.copy()
    df_out["publctn_rt"] = df_out["publctn_rt"].apply(get_bitmask)
    return df_out