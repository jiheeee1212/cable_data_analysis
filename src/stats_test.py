import pandas as pd
import scipy.stats as stats
from typing import Union, List, Dict, Optional, Tuple

def one_sample_ttest(df: pd.DataFrame, target_col: str, popmean: float) -> Dict[str, float]:
    """
    1집단 평균 비교 (One-sample t-test)
    """
    data = df[target_col].dropna()
    statistic, pvalue = stats.ttest_1samp(data, popmean)
    return {'statistic': statistic, 'p_value': pvalue, 'mean': data.mean()}

def compare_two_groups(df: pd.DataFrame, target_col: str, group_col: str, 
                      group1: Union[str, int], group2: Union[str, int],
                      test_type: str = 't-test') -> Dict[str, float]:
    """
    2집단 평균 비교
    test_type: 't-test' (equal variance), 'welch' (unequal variance), 'mann-whitney' (non-parametric)
    """
    g1_data = df[df[group_col] == group1][target_col].dropna()
    g2_data = df[df[group_col] == group2][target_col].dropna()
    
    if test_type == 'mann-whitney':
        statistic, pvalue = stats.mannwhitneyu(g1_data, g2_data)
    elif test_type == 'welch':
        statistic, pvalue = stats.ttest_ind(g1_data, g2_data, equal_var=False)
    else: # t-test (assuming equal variance)
        statistic, pvalue = stats.ttest_ind(g1_data, g2_data, equal_var=True)
        
    return {'statistic': statistic, 'p_value': pvalue, 
            'mean_1': g1_data.mean(), 'mean_2': g2_data.mean()}

def compare_multiple_groups(df: pd.DataFrame, target_col: str, group_col: str, 
                          test_type: str = 'anova') -> Dict[str, float]:
    """
    3집단 이상 평균 비교
    test_type: 'anova' (parametric), 'kruskal' (non-parametric)
    """
    groups = df[group_col].dropna().unique()
    data_by_group = [df[df[group_col] == g][target_col].dropna() for g in groups]
    
    if test_type == 'kruskal':
        statistic, pvalue = stats.kruskal(*data_by_group)
    else: # anova
        statistic, pvalue = stats.f_oneway(*data_by_group)
        
    return {'statistic': statistic, 'p_value': pvalue}

def chisquare_test(df: pd.DataFrame, col1: str, col2: str) -> Dict[str, float]:
    """
    범주형 변수 간 독립성 검정 (Chi-square test)
    """
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    return {'statistic': chi2, 'p_value': p, 'dof': dof}

def fit_regression(df: pd.DataFrame, formula: str, model_type: str = 'ols') -> object:
    """
    회귀분석
    model_type: 'ols' (Linear Regression), 'logit' (Logistic Regression)
    formula: Patsy formula string e.g. 'y ~ x1 + x2'
    """
    data = df.dropna()
    if model_type == 'logit':
        model = smf.logit(formula=formula, data=data).fit(disp=0)
    else:
        model = smf.ols(formula=formula, data=data).fit()
    return model

def calculate_correlation(df: pd.DataFrame, col1: str, col2: str, method: str = 'pearson') -> Dict[str, float]:
    """
    상관관계 분석
    method: 'pearson', 'spearman', 'kendall'
    """
    data = df[[col1, col2]].dropna()
    corr, pvalue = getattr(stats, f'{method}r')(data[col1], data[col2]) 
    if method == 'kendall': # scipy kendalltau returns different name
         corr, pvalue = stats.kendalltau(data[col1], data[col2])
    
    return {'correlation': corr, 'p_value': pvalue}
