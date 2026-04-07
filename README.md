<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:c9a98a,50:b8906e,100:9a7357&height=180&section=header&text=InsightIQ&fontSize=64&fontColor=ffffff&fontAlignY=42&desc=AI-Powered%20Business%20Intelligence%20Dashboard%20Generator&descAlignY=62&descSize=16&animation=fadeIn" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![Status](https://img.shields.io/badge/Status-Active-9a7357?style=for-the-badge)]()

<br/>

> *Upload any dataset. Get a full business intelligence dashboard. Instantly.*

</div>

---

## 🔮 What is InsightIQ?

**InsightIQ** is an AI-powered dashboard generator that transforms raw CSV/Excel files into interactive, insight-rich business dashboards — with zero manual configuration required.

No SQL. No BI tool expertise. No data engineering. Just upload and explore.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📂 **Smart Upload** | Drag & drop CSV or Excel — auto-detected, parsed instantly |
| 📊 **Auto KPI Engine** | Dynamically identifies and computes relevant business metrics |
| 🤖 **AI Insights** | Statistical pattern recognition across all columns |
| 📈 **Adaptive Charts** | 5 chart types selected automatically based on data structure |
| 🎛️ **Live Filters** | Slicer-based filtering that updates the entire dashboard in real-time |
| 📋 **Statistical Summary** | Full describe(), correlation analysis, missing value report |
| 🎨 **Luxury UI** | Elegant warm-tone design — looks like a real BI product |

---

## 🖥️ Dashboard Pages

```
HOME          →  Landing page with product overview
UPLOAD        →  File upload with instant data preview & stats
DASHBOARD     →  KPIs + 4 adaptive charts + category slicers
AI INSIGHTS   →  Auto-generated statistical findings
SUMMARY       →  Full describe(), categorical breakdown, missing values
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/truptibhalekarr/insightiq.git
cd insightiq

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run InsightIq.py
```

Then open `http://localhost:8501` in your browser.

---

## 🛠️ Tech Stack

```python
stack = {
    "Frontend"     : "Streamlit + Custom CSS",
    "Charts"       : "Plotly Express + Graph Objects",
    "Data Engine"  : "Pandas + NumPy",
    "Language"     : "Python 3.10+",
    "Design"       : "Cormorant Garamond + DM Sans + Warm Palette",
}
```

---

## 📦 Requirements

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
plotly>=5.15.0
openpyxl>=3.1.0
```

---

## 📸 Supported File Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| CSV | `.csv` | Any delimiter, auto-detected |
| Excel | `.xlsx` | Multi-sheet support planned |
| Excel Legacy | `.xls` | Supported via openpyxl |

---

## 🧠 How the AI Engine Works

```
1. UPLOAD     →  File parsed into Pandas DataFrame
2. CLASSIFY   →  Columns auto-classified: numerical / categorical / datetime
3. KPIs       →  Revenue, volume, rate metrics auto-computed from column names
4. CHARTS     →  Chart types chosen based on data shape:
                   datetime + numeric  →  Line chart (trend)
                   categorical         →  Bar chart (top 10)
                   2 numerics          →  Scatter plot
                   category share      →  Donut pie chart
                   single numeric      →  Histogram
5. INSIGHTS   →  Mean, max, min, std, correlations, missing values surfaced
6. FILTERS    →  Smart slicers built from low-cardinality categorical columns
```

---

## 🗺️ Roadmap

- [ ] 🤖 LLM-powered natural language insights ("Why did sales drop in Q3?")
- [ ] 💬 Natural language query interface ("Show me top 5 products by revenue")
- [ ] 📄 Export dashboard as PDF / PowerPoint
- [ ] ☁️ Cloud deployment (Streamlit Cloud / Hugging Face Spaces)
- [ ] 🔗 Database connectors (PostgreSQL, BigQuery, Snowflake)
- [ ] 📊 Advanced chart recommendation engine (ML-based)

---

## 👩‍💻 Author

<div align="center">

**Trupti Bhalekar**
*Data Science & Analytics with AI @ itvEdant*

[![GitHub](https://img.shields.io/badge/GitHub-truptibhalekarr-181717?style=flat-square&logo=github)](https://github.com/truptibhalekarr)
[![HuggingFace](https://img.shields.io/badge/🤗-truptibhalekarr-FFD21E?style=flat-square)](https://huggingface.co/truptibhalekarr)

*Building AI that makes data accessible to everyone.*

</div>

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:9a7357,50:b8906e,100:c9a98a&height=100&section=footer&animation=fadeIn" />

⭐ **Star this repo if InsightIQ helped you!**

</div>
