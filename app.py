"""
Auto EDA Report Generator
Author: Deepanshu Garg
Description: Upload any CSV — get a full Exploratory Data Analysis report instantly.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Auto EDA Report Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem; border-radius: 10px; color: white;
        text-align: center; margin: 0.3rem 0;
    }
    .metric-value { font-size: 2rem; font-weight: 700; }
    .metric-label { font-size: 0.85rem; opacity: 0.85; }
    .section-header {
        background: #f0f2f6; padding: 0.5rem 1rem;
        border-left: 4px solid #667eea; border-radius: 4px;
        margin: 1.5rem 0 1rem 0; font-weight: 600; font-size: 1.1rem;
    }
    .warning-box {
        background: #fff3cd; border: 1px solid #ffc107;
        padding: 0.75rem; border-radius: 6px; margin: 0.5rem 0;
    }
    .good-box {
        background: #d4edda; border: 1px solid #28a745;
        padding: 0.75rem; border-radius: 6px; margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.shields.io/badge/Auto%20EDA-Report%20Generator-blueviolet?style=for-the-badge", use_container_width=True)
    st.markdown("### ⚙️ Settings")

    sample_datasets = {
        "📦 None (upload your own)": None,
        "🚢 Titanic (Classification)": "titanic",
        "🏠 Housing Prices (Regression)": "housing",
        "🛒 Retail Sales (Time Series)": "retail",
    }
    selected_sample = st.selectbox("Use sample dataset", list(sample_datasets.keys()))
    uploaded_file  = st.file_uploader("Or upload CSV", type=["csv"])

    st.markdown("---")
    st.markdown("### 🎨 Chart Theme")
    theme = st.selectbox("Color theme", ["plotly_dark", "plotly", "ggplot2", "seaborn"])

    st.markdown("---")
    st.markdown("**Built by [Deepanshu Garg](https://github.com/deepanshu0110)**")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-deepanshu0110-black?logo=github)](https://github.com/deepanshu0110)")


# ─── Sample Data Generators ──────────────────────────────────────────────────
def load_sample(name):
    np.random.seed(42)
    n = 500
    if name == "titanic":
        return pd.DataFrame({
            "Survived":  np.random.randint(0, 2, n),
            "Pclass":    np.random.choice([1, 2, 3], n, p=[0.2, 0.3, 0.5]),
            "Sex":       np.random.choice(["male","female"], n, p=[0.65, 0.35]),
            "Age":       np.random.normal(30, 14, n).clip(1, 80).round(1),
            "Fare":      np.random.exponential(33, n).round(2),
            "Embarked":  np.random.choice(["S","C","Q"], n, p=[0.7, 0.2, 0.1]),
            "SibSp":     np.random.randint(0, 5, n),
            "Parch":     np.random.randint(0, 4, n),
        })
    elif name == "housing":
        sqft = np.random.normal(1800, 500, n).clip(500, 5000).round(0)
        return pd.DataFrame({
            "Price":       (sqft * 150 + np.random.normal(0, 20000, n)).clip(50000).round(-2),
            "SqFt":        sqft,
            "Bedrooms":    np.random.randint(1, 6, n),
            "Bathrooms":   np.random.choice([1,1.5,2,2.5,3], n),
            "YearBuilt":   np.random.randint(1970, 2023, n),
            "Neighborhood":np.random.choice(["Downtown","Suburb","Rural","Urban"], n),
            "GarageType":  np.random.choice(["Attached","Detached","None"], n, p=[0.5,0.3,0.2]),
            "Condition":   np.random.choice(["Excellent","Good","Fair","Poor"], n, p=[0.2,0.5,0.2,0.1]),
        })
    else:  # retail
        dates = pd.date_range("2023-01-01", periods=n, freq="D")
        return pd.DataFrame({
            "Date":     dates.astype(str),
            "Sales":    (np.random.normal(5000, 1500, n) + np.sin(np.arange(n)/30)*1000).clip(500).round(2),
            "Quantity": np.random.randint(10, 200, n),
            "Category": np.random.choice(["Electronics","Clothing","Food","Home"], n),
            "Region":   np.random.choice(["North","South","East","West"], n),
            "Discount": np.random.choice([0, 5, 10, 15, 20], n),
            "Returns":  np.random.randint(0, 20, n),
        })


# ─── Load Data ───────────────────────────────────────────────────────────────
df = None
data_name = "Dataset"

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    data_name = uploaded_file.name
elif sample_datasets[selected_sample]:
    df = load_sample(sample_datasets[selected_sample])
    data_name = selected_sample.split(" ", 1)[1]


# ─── Main App ─────────────────────────────────────────────────────────────────
st.title("📊 Auto EDA Report Generator")
st.markdown("Upload any CSV — get a complete Exploratory Data Analysis report in seconds.")

if df is None:
    st.info("👈 Select a sample dataset or upload your own CSV to get started.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🔍 What you get")
        st.markdown("- Dataset overview & shape\n- Missing value analysis\n- Distribution plots\n- Correlation heatmap\n- Outlier detection\n- Category analysis")
    with col2:
        st.markdown("#### 🎯 Best for")
        st.markdown("- Quick data exploration\n- Client presentations\n- Finding data issues\n- Feature understanding\n- Business insights")
    with col3:
        st.markdown("#### 📁 Supported")
        st.markdown("- Any CSV file\n- Up to 100K rows\n- Numeric columns\n- Categorical columns\n- Date columns\n- Mixed types")
    st.stop()


# ─── 1. OVERVIEW ─────────────────────────────────────────────────────────────
st.markdown(f"## 📋 Report: `{data_name}`")

num_cols  = df.select_dtypes(include=np.number).columns.tolist()
cat_cols  = df.select_dtypes(include="object").columns.tolist()
missing   = df.isnull().sum().sum()
dup_rows  = df.duplicated().sum()
mem_mb    = df.memory_usage(deep=True).sum() / 1024**2

c1, c2, c3, c4, c5, c6 = st.columns(6)
metrics = [
    (c1, str(df.shape[0]),  "Rows"),
    (c2, str(df.shape[1]),  "Columns"),
    (c3, str(len(num_cols)),"Numeric"),
    (c4, str(len(cat_cols)),"Categorical"),
    (c5, str(missing),      "Missing Values"),
    (c6, str(dup_rows),     "Duplicate Rows"),
]
for col, val, lbl in metrics:
    with col:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{val}</div>
            <div class="metric-label">{lbl}</div>
        </div>""", unsafe_allow_html=True)


# ─── 2. DATA PREVIEW + DTYPES ────────────────────────────────────────────────
st.markdown('<div class="section-header">🗂️ Data Preview & Column Types</div>', unsafe_allow_html=True)
tab1, tab2 = st.tabs(["📄 First 10 Rows", "📊 Column Summary"])
with tab1:
    st.dataframe(df.head(10), use_container_width=True)
with tab2:
    summary = pd.DataFrame({
        "Column":    df.columns,
        "Type":      df.dtypes.values,
        "Non-Null":  df.notnull().sum().values,
        "Null":      df.isnull().sum().values,
        "Null %":    (df.isnull().mean() * 100).round(1).values,
        "Unique":    df.nunique().values,
        "Sample":    [str(df[c].dropna().iloc[0]) if df[c].notnull().any() else "N/A" for c in df.columns],
    })
    st.dataframe(summary, use_container_width=True)


# ─── 3. MISSING VALUES ───────────────────────────────────────────────────────
st.markdown('<div class="section-header">❓ Missing Value Analysis</div>', unsafe_allow_html=True)
miss_df = df.isnull().sum().reset_index()
miss_df.columns = ["Column", "Missing"]
miss_df["Pct"] = (miss_df["Missing"] / len(df) * 100).round(2)
miss_df = miss_df[miss_df["Missing"] > 0].sort_values("Missing", ascending=False)

if miss_df.empty:
    st.markdown('<div class="good-box">✅ No missing values found — dataset is complete!</div>', unsafe_allow_html=True)
else:
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.dataframe(miss_df, use_container_width=True)
    with col_b:
        fig = px.bar(miss_df, x="Column", y="Pct", title="Missing Value % by Column",
                     color="Pct", color_continuous_scale="Reds", template=theme)
        fig.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig, use_container_width=True)


# ─── 4. NUMERIC ANALYSIS ─────────────────────────────────────────────────────
if num_cols:
    st.markdown('<div class="section-header">🔢 Numeric Column Analysis</div>', unsafe_allow_html=True)

    # Descriptive stats
    desc = df[num_cols].describe().T.round(3)
    desc["skew"]     = df[num_cols].skew().round(3)
    desc["kurtosis"] = df[num_cols].kurtosis().round(3)
    st.dataframe(desc, use_container_width=True)

    # Distribution plots
    st.markdown("**Distribution Plots**")
    cols_per_row = 3
    rows_needed  = (len(num_cols) + cols_per_row - 1) // cols_per_row
    for row_i in range(rows_needed):
        row_cols = st.columns(cols_per_row)
        for col_i, col_name in enumerate(num_cols[row_i*cols_per_row:(row_i+1)*cols_per_row]):
            with row_cols[col_i]:
                fig = px.histogram(df, x=col_name, nbins=30, title=col_name,
                                   template=theme, color_discrete_sequence=["#667eea"])
                fig.add_vline(x=df[col_name].mean(), line_dash="dash",
                              annotation_text="mean", line_color="red")
                fig.update_layout(height=250, margin=dict(t=35,b=10,l=10,r=10), showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

    # Box plots for outlier detection
    st.markdown("**Outlier Detection (Box Plots)**")
    fig = go.Figure()
    for col in num_cols:
        norm = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-9)
        fig.add_trace(go.Box(y=norm, name=col, boxpoints="outliers"))
    fig.update_layout(title="Normalized Box Plots — Outlier Overview",
                      template=theme, height=350)
    st.plotly_chart(fig, use_container_width=True)

    # Correlation heatmap
    if len(num_cols) >= 2:
        st.markdown("**Correlation Heatmap**")
        corr = df[num_cols].corr().round(2)
        fig  = px.imshow(corr, text_auto=True, title="Pearson Correlation Matrix",
                         color_continuous_scale="RdBu_r", template=theme,
                         zmin=-1, zmax=1, aspect="auto")
        fig.update_layout(height=max(350, len(num_cols)*60))
        st.plotly_chart(fig, use_container_width=True)

        # High correlations alert
        high_corr = []
        for i in range(len(corr.columns)):
            for j in range(i+1, len(corr.columns)):
                val = corr.iloc[i,j]
                if abs(val) >= 0.75:
                    high_corr.append((corr.columns[i], corr.columns[j], val))
        if high_corr:
            st.markdown('<div class="warning-box">⚠️ <strong>High Correlations Found (|r| ≥ 0.75):</strong> ' +
                " | ".join([f"{a} ↔ {b}: {v:.2f}" for a,b,v in high_corr]) + "</div>",
                unsafe_allow_html=True)


# ─── 5. CATEGORICAL ANALYSIS ─────────────────────────────────────────────────
if cat_cols:
    st.markdown('<div class="section-header">🏷️ Categorical Column Analysis</div>', unsafe_allow_html=True)
    cols_per_row = 2
    rows_needed  = (len(cat_cols) + cols_per_row - 1) // cols_per_row
    for row_i in range(rows_needed):
        row_cols = st.columns(cols_per_row)
        for col_i, col_name in enumerate(cat_cols[row_i*cols_per_row:(row_i+1)*cols_per_row]):
            with row_cols[col_i]:
                vc = df[col_name].value_counts().reset_index()
                vc.columns = [col_name, "Count"]
                vc["Pct"] = (vc["Count"] / len(df) * 100).round(1)
                top_n = vc.head(10)
                fig = px.bar(top_n, x=col_name, y="Count",
                             title=f"{col_name} — {df[col_name].nunique()} unique",
                             template=theme, color="Count",
                             color_continuous_scale="Viridis",
                             text="Pct")
                fig.update_traces(texttemplate="%{text}%", textposition="outside")
                fig.update_layout(height=300, margin=dict(t=40,b=10,l=10,r=10),
                                  showlegend=False, coloraxis_showscale=False)
                st.plotly_chart(fig, use_container_width=True)


# ─── 6. BUSINESS INSIGHTS ────────────────────────────────────────────────────
st.markdown('<div class="section-header">💡 Auto-Generated Business Insights</div>', unsafe_allow_html=True)
insights = []

# Size
if len(df) < 1000:
    insights.append("⚠️ Small dataset (<1K rows) — model results may not generalize well.")
elif len(df) > 50000:
    insights.append("✅ Large dataset (>50K rows) — suitable for deep learning approaches.")
else:
    insights.append(f"✅ Medium-sized dataset ({len(df):,} rows) — suitable for classical ML.")

# Missing
miss_pct = missing / (df.shape[0] * df.shape[1]) * 100
if miss_pct == 0:
    insights.append("✅ No missing values — data is clean and ready for modeling.")
elif miss_pct < 5:
    insights.append(f"⚠️ Low missingness ({miss_pct:.1f}%) — simple imputation (mean/mode) recommended.")
else:
    insights.append(f"🔴 High missingness ({miss_pct:.1f}%) — consider advanced imputation or dropping columns.")

# Duplicates
if dup_rows > 0:
    insights.append(f"⚠️ {dup_rows} duplicate rows found — drop before training to avoid data leakage.")

# Skewness
if num_cols:
    skewed = [c for c in num_cols if abs(df[c].skew()) > 1.5]
    if skewed:
        insights.append(f"⚠️ Highly skewed columns: {', '.join(skewed)} — consider log/sqrt transform.")

# Class imbalance check for binary columns
for col in num_cols:
    if df[col].nunique() == 2 and set(df[col].unique()).issubset({0,1}):
        ratio = df[col].mean()
        if ratio < 0.2 or ratio > 0.8:
            insights.append(f"⚠️ Possible target column '{col}' is imbalanced ({ratio*100:.0f}% positive) — use SMOTE or class_weight.")

# High cardinality
if cat_cols:
    high_card = [c for c in cat_cols if df[c].nunique() > 20]
    if high_card:
        insights.append(f"⚠️ High cardinality columns: {', '.join(high_card)} — consider target encoding instead of one-hot.")

for ins in insights:
    color = "warning-box" if ins.startswith("⚠️") else ("good-box" if ins.startswith("✅") else "warning-box")
    st.markdown(f'<div class="{color}">{ins}</div>', unsafe_allow_html=True)


# ─── 7. DOWNLOAD REPORT ──────────────────────────────────────────────────────
st.markdown('<div class="section-header">📥 Export Data Summary</div>', unsafe_allow_html=True)
csv_buf = io.StringIO()
df.describe(include="all").to_csv(csv_buf)
st.download_button("⬇️ Download Stats Summary (CSV)", csv_buf.getvalue(),
                   "eda_summary.csv", "text/csv", use_container_width=True)

st.markdown("---")
st.markdown("Built with ❤️ by **Deepanshu Garg** | [GitHub](https://github.com/deepanshu0110) | [Freelancer.com](https://www.freelancer.com/u/deepanshu0110)")
