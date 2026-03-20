# Auto EDA Report Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?style=flat-square&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.19+-blueviolet?style=flat-square&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Upload **any CSV file** and get a complete Exploratory Data Analysis report in seconds — no coding required.

---

## Features

| Section | What you get |
|---|---|
| **Overview** | Rows, columns, missing values, duplicates at a glance |
| **Data Preview** | First 10 rows + full column type summary |
| **Missing Values** | Bar chart + % missing per column |
| **Numeric Analysis** | Distributions, box plots, outlier detection |
| **Correlation Matrix** | Heatmap with high-correlation alerts |
| **Categorical Analysis** | Bar charts for top categories per column |
| **Business Insights** | Auto-generated warnings (imbalance, skewness, cardinality) |
| **Export** | Download summary stats as CSV |

---

## Built-in Sample Datasets

- Titanic (Binary Classification)
- Housing Prices (Regression)
- Retail Sales (Time Series)

Or upload your own CSV!

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

## Project Structure

```
auto-eda-report/
├── app.py                  # Main Streamlit app (346 lines)
├── requirements.txt        # Pinned dependencies
├── .streamlit/
│   └── config.toml         # Dark purple theme
├── .gitignore
├── LICENSE
└── README.md
```

---

## Roadmap

- [ ] Excel (.xlsx) file support
- [ ] PDF report export
- [ ] Time series auto-detection
- [ ] Target column analysis
- [ ] AI-powered insight generation
- [ ] Multi-file comparison mode

---

## Tech Stack

Python · Streamlit · Plotly · Pandas · NumPy

---

## Author

**Deepanshu Garg** — Freelance Data Analyst & Data Scientist

[![GitHub](https://img.shields.io/badge/GitHub-deepanshu0110-black?style=flat-square&logo=github)](https://github.com/deepanshu0110)
[![Freelancer](https://img.shields.io/badge/Hire%20Me-Freelancer.com-brightgreen?style=flat-square)](https://www.freelancer.com/u/deepanshu0110)

---

## License

MIT License — see [LICENSE](LICENSE) for details.
