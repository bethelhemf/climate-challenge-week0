# 🌍 Ethiopia Climate Vulnerability Analysis - COP32 

This repository contains a data-driven climate analysis (2015–2026) focused on Ethiopia and its regional neighbors (Kenya, Sudan, Nigeria, and Tanzania). The project is designed to provide empirical evidence for Ethiopia's position paper at COP32, highlighting unique climate risks and the need for tailored adaptation funding.

---

## 🛠️ Phase 1: Git & Environment Setup
The project began with the initialization of a central workspace to ensure reproducibility and collaboration.
- **Environment:** A Python virtual environment was configured to isolate dependencies.
- **Branching Strategy:** A structured approach was adopted using a `setup-task` branch for initialization and specific task-based branches (e.g., `dashboard-dev`) for feature development.
- **CI/CD:** A GitHub Actions workflow (`unittests.yml`) was configured to automatically validate the environment and dependencies on every push to the main branch.
- **Git Hygiene:** Development followed Conventional Commit standards. A `.gitignore` file was implemented to exclude raw data, NASA sentinel value files, and notebook checkpoints.

## 🧹 Phase 2: Data Profiling, Cleaning & EDA
The analytical workflow involved processing diverse datasets for five countries, ensuring they were research-ready.
- **Data Standardization:** Temporal consistency was established by converting YEAR and DOY columns into a unified datetime format.
- **Quality Control:** 
    - Replaced NASA sentinel values (**-999**) with NaN.
    - Handled missing values using forward-fill techniques or logical exclusion.
- **Outlier Management:** Detected outliers using **Z-score thresholds (±3)**. Extreme values were capped or retained based on physical plausibility to preserve genuine climate signals (e.g., extreme storms).
- **Exploratory Data Analysis (EDA):** Performed seasonal trend analysis, correlation mapping, and distribution checks to identify unique climatic shifts in each region.

## 📊 Phase 3: Cross-Country Comparison & Ranking
Cleaned datasets were synthesized to identify relative vulnerability.
- **Statistical Significance:** Conducted **One-Way ANOVA**, **Kruskal-Wallis**, and **Levene’s tests**.
- **Results:** Confirmed significant regional differences (**p < 0.001**) with an **H-statistic > 15,000**, proving that Ethiopia’s climate profile is statistically distinct from its neighbors.
- **Vulnerability Index:** Ranked countries based on Heat Stress, Drought Spells (consecutive dry days), and Temperature Volatility.

## 🚀 Phase 4: Interactive Dashboard
A professional **Streamlit** dashboard was developed to translate complex data into actionable insights for policymakers.
- **Interactive Features:** Includes a Country multi-select widget, Year range slider, and Variable selector (T2M, PRECTOTCORR, RH2M).
- **Visuals:** Integrated **Plotly** line charts and precipitation boxplots.
- **Deployment:** Optimized for deployment on Streamlit Community Cloud with a robust `requirements.txt`.

---

## 🖼️ Dashboard Preview
![Dashboard Screenshot](dashboard_screenshots/dashboard_preview.png)

## 📁 Repository Structure
```text
├── app/                # Streamlit dashboard (main.py, utils.py)
├── notebooks/          # Task 2 & 3: EDA & Comparison notebooks
│   └── data/           # Cleaned CSV datasets
├── dashboard_screenshots/ # Visual previews
├── data/               # Raw datasets (Git ignored)
├── .github/workflows/  # CI/CD (GitHub Actions)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation# EAR and DOY columns into a unified datetime format.
---
