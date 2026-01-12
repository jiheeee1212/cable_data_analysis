# 📊 LG HelloVision Customer Analysis

## 1. Project Overview
본 프로젝트는 LG HelloVision 고객 데이터를 활용하여  
고객 특성과 서비스 이용 행태 간의 관계를 탐색하고,  
각 변수 간 통계적 특성을 분석하는 것을 목표로 한다.  


⚠️ 실제 데이터는 내부 전용이며, 깃허브에는 포함되지 않습니다.  


## 2. Project Structure
lg_hellovision_customer_analysis/
├─ data/                   # 내부용 데이터 폴더 (깃허브에는 업로드 X, .gitignore 처리)
│   ├─ user_data.pkl
│   └─ vod_data.pkl
├─ notebooks/               
│   ├─ 01_eda.ipynb       
│   └─ 02_statistical_test.ipynb  
├─ outputs/                  
│   ├─ figures/              
│   └─ tables/               
├─ src/                      
│   ├─ config.py              
│   └─ stats_test.py         
├─ .gitignore               
└─ README.md                 
---

## 3. Analysis Process

### 3.1 Exploratory Data Analysis (EDA)
- 데이터 구조 확인 및 변수 타입 점검  
- 결측치 및 이상치 탐색  
- 변수 분포 확인 (히스토그램, 박스플롯 등)  
- 변수 간 관계 시각화 (scatter, heatmap 등)  

### 3.2 Statistical Testing
- **범주형 변수 간 관계:**  
  - Chi-square test / 교차분석 → 범주형 변수끼리 독립성 확인
- **수치형 변수 집단 비교:**  
  - t-test / ANOVA / F-test → 집단별 평균 차이 확인
  - 비정규 수치형 → Mann–Whitney, Kruskal–Wallis  
- 유의수준 α = 0.05 기준으로 변수 간 통계적 관계 검정  

---

## 4. Tech Stack
- **언어:** Python  
- **라이브러리:** Pandas, NumPy, Matplotlib, Seaborn, SciPy, Statsmodels  
