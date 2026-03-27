# Auto EDA Report Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?style=flat-square&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.19+-blueviolet?style=flat-square&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Upload any CSV and get a complete Exploratory Data Analysis report in seconds — no coding required.

---

## Business Problem

Data analysts spend hours writing repetitive EDA code for every new dataset. This tool automates that entire process — from missing value detection to correlation alerts — so you can focus on insights, not boilerplate.

---

## What You Get

| Section | Output |
|---|---|
| Overview | Rows, columns, missing values, duplicates |
| Missing Values | Bar chart + % missing per column |
| Numeric Analysis | Distributions, box plots, outlier flags |
| Correlation Matrix | Heatmap with high-correlation alerts |
| Categorical Analysis | Bar charts for top categories |
| Business Warnings | Imbalance, skewness, high-cardinality alerts |
| Export | Download summary stats as CSV |

---

## Built-in Sample Datasets

- Titanic (Classification)
- Housing Prices (Regression)
- Retail Sales (Time Series)

Or upload your own CSV.

---

## Quickstart

```bash
git clone https://github.com/deepanshu0110/auto-eda-report.git
cd auto-eda-report
pip install -r requirements.txt
streamlit run app.py
```

Open: http://localhost:8501

---

## Tech Stack

Python · Streamlit · Plotly · Pandas · NumPy

---

## Roadmap

- [ ] Excel (.xlsx) support
- [ ] PDF report export
- [ ] Time series auto-detection
- [ ] AI-powered insight generation

---

## Author

**Deepanshu Garg** — Freelance Data Analyst & Data Scientist
- GitHub: [@deepanshu0110](https://github.com/deepanshu0110)
- Hire: [freelancer.com/u/deepanshu0110](https://www.freelancer.com/u/deepanshu0110)

MIT License