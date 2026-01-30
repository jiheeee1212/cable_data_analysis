import pandas as pd


MART_DROP_COLS = [
    'updated', 'use_fl', 'ver_major', 'ver_minor', 'vod_acq_tp_cd', 'wrtr_disp',
    'svc_apy_fl', 'thmbnl_del_fl', 'thmbnl_fl', 'thmbnl_pt', 'thmbnl_rep_file_nm',
    'ttl_brief', 'studio_cd',
    'smry', 'smry_lng', 'smry_shrt',
    'sp_id', 'rvsn_id', 'prevw_prd',
    'orgnl_cntry', 'poster_del_fl', 'poster_pt',
    'img_base_dir', 'director', 'chapter',
    'is_hot_fl', 'is_new_fl', 'long_tail_fl',
     'provider', 'description',
    'studio', 'prvd_id','asset_5',"disp_rtm",'asset_id',
   'super_asset_sq','epsd_nm','series_sq','lt_inclsn_fl'
]

def drop_high_null_cols(df: pd.DataFrame, threshold: float = 90.0):
    null_rate = df.isna().mean() * 100
    drop_cols = null_rate[null_rate >= threshold].index.tolist()

    df_cleaned = df.drop(columns=drop_cols)
    return df_cleaned, drop_cols

def drop_mart_cols(df: pd.DataFrame):
    return df.drop(columns=MART_DROP_COLS, errors="ignore")

def get_column_summary(df: pd.DataFrame):
    summary = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.astype(str).values,
        "null_cnt": df.isna().sum().values,
        "null_rate": (df.isna().mean() * 100).round(2).values,
        "unique_cnt": df.nunique().values
    }).reset_index(drop=True)  

    return summary

def clean_mart(df: pd.DataFrame):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    date_cols = ["broad_ymd", "created", "crt_ymd","rlse_year"]
    flag_cols = ["lt_inclsn_fl"]
    float_cols = ["product_tp"]
    category_cols = [
        "actr_disp","asset_nm","asset_prod","category","created_by",
        "ct_cl","cts_id","eosd_no","genre","genre_of_ct_cl","publctn_rt",
        "screen_tp","studio_nm","super_asset_id","asset_5","epsd_no",
        "epsd_id","full_asset_id","super_asset_nm","ttl"
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    for col in flag_cols:
        if col in df.columns:
            df[col] = df[col].map({"Y":1,"N":0}).fillna(0).astype("Int64")

    for col in float_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").round().astype("Int64")

    for col in category_cols:
        if col in df.columns:
            df[col] = df[col].fillna("unknown").astype("category")

    return df

def clean_log(df: pd.DataFrame):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    
    float_cols = ["use_tms"]
    float_cols = [c.lower() for c in float_cols]
    for col in float_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").round().astype("Int64")
    
    category_cols = [
        "sha2_hash",
        "asset",
        "asset_nm",
        "ct_cl",
        "genre_of_ct_cl",
        "category"
    ]
    category_cols = [c.lower() for c in category_cols]
    for col in category_cols:
        if col in df.columns:
            df[col] = df[col].fillna("unknown").astype("category")

    if "disp_rtm" in df.columns:
        def disp_rtm_to_sec(x):
            try:
                m, s = map(int, x.split(":"))
                if s >= 60:
                    m += s // 60
                    s = s % 60
                return m * 60 + s
            except:
                return pd.NA
        df['disp_rtm_sec'] = df['disp_rtm'].apply(disp_rtm_to_sec).astype("Int64")
        df.drop(columns=["disp_rtm"], inplace=True)
    return df


LOG_DROP_COLS = [
   "asset_nm","CT_CL","genre_of_ct_cl","category"
]

def drop_log_cols(df: pd.DataFrame):
    return df.drop(columns=LOG_DROP_COLS, errors="ignore")

