def check_id_matching(m_ids, l_ids, dataset_type="mart_vs_log", verbose=True):
    set_m = set(m_ids)
    set_l = set(l_ids)

    common_ids = set_m & set_l
    match_rate_l = len(common_ids) / len(set_l) * 100
    match_rate_m = len(common_ids) / len(set_m) * 100
    ghost_ids = set_l - set_m

    if dataset_type == "mart_vs_log":
        m_name = "Mart"
        l_name = "Log"
    elif dataset_type == "tps_vs_log":
        m_name = "TPS"
        l_name = "Log"


    result = {
        "common_cnt": len(common_ids),
        f"{l_name}_total": len(set_l),
        f"{m_name}_total": len(set_m),
        f"match_rate_{l_name.lower()}": match_rate_l,
        f"match_rate_{m_name.lower()}": match_rate_m,
        "ghost_cnt": len(ghost_ids),
        "ghost_ids_sample": list(ghost_ids)[:5]
    }

    if verbose:
        print(f"1. 공통 ID 개수 : {result['common_cnt']:,}개")
        print(f"2. {l_name} 매칭률   : {match_rate_l:.2f}% ({l_name} 중 {m_name} 정보가 존재하는 비율)")
        print(f"3. {m_name} 매칭률  : {match_rate_m:.2f}% ({m_name} 중 {l_name} 정보가 존재하는 비율)")

        if result["ghost_cnt"] > 0:
            print(f" 경고: {l_name}에는 있으나 {m_name}에 없는 ID가 {result['ghost_cnt']:,}개 있습니다.")
            print(f"   예시: {result['ghost_ids_sample']}")
        else:
            print(f" 모든 {l_name}의 정보가 {m_name}에 존재합니다. (무결성 확보)")

    return result
