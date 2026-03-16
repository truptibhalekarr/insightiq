import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="AI Dashboard Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=DM+Sans:wght@300;400;500&display=swap');

  html, body, [class*="css"] { font-family:'DM Sans',sans-serif; background-color:#fdf0f0; color:#2b2318; }
  #MainMenu, footer, header { visibility:hidden; }
  /* Force remove ALL Streamlit default padding */
  .block-container {
    padding: 0 !important;
    max-width: 100% !important;
  }
  section[data-testid="stMain"] > div {
    padding: 0 !important;
  }
  div[data-testid="stVerticalBlock"] {
    gap: 0 !important;
  }
  /* Add our own side margins to everything INSIDE dash */
  div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
    padding: 0 60px !important;
  }
  /* Prevent zoom / scale issues */
  html {
    zoom: 1 !important;
    -ms-zoom: 1 !important;
    -webkit-text-size-adjust: 100% !important;
  }
  .block-container { padding:0 !important; max-width:100% !important; }
  .stApp, .main, div[data-testid="stAppViewContainer"] { background-color:#fdf0f0 !important; }
  header[data-testid="stHeader"] { background:#fce8e8 !important; }

  .navbar { width:100%; display:flex; justify-content:space-between; align-items:center; padding:22px 48px; background:transparent; position:absolute; top:0; left:0; right:0; z-index:10; box-sizing:border-box; }
  .nav-brand { font-size:13px; font-weight:500; letter-spacing:0.22em; color:rgba(255,255,255,0.95); text-transform:uppercase; }
  .nav-links { display:flex; gap:32px; font-size:13px; color:rgba(255,255,255,0.8); }

  .hero { position:relative; width:100%; min-height:82vh; background:linear-gradient(135deg,#c9a98a 0%,#d4b49a 30%,#b8906e 60%,#9a7357 100%); display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:60px 20px; overflow:hidden; }
  .hero::before { content:''; position:absolute; top:-80px; left:-80px; width:320px; height:320px; background:rgba(255,255,255,0.12); border-radius:50%; filter:blur(60px); }
  .hero::after  { content:''; position:absolute; bottom:-60px; right:-60px; width:260px; height:260px; background:rgba(90,50,20,0.18); border-radius:50%; filter:blur(50px); }
  .shape { position:absolute; border-radius:50%; opacity:0.18; }
  .shape-1 { width:180px; height:180px; background:#fff; top:12%; left:8%; filter:blur(2px); }
  .shape-2 { width:90px; height:90px; background:#5a3214; bottom:18%; left:14%; }
  .shape-3 { width:130px; height:40px; background:#7a5535; border-radius:8px; bottom:26%; right:10%; transform:rotate(-15deg); }
  .hero-title { font-family:'Cormorant Garamond',serif; font-size:clamp(64px,10vw,120px); font-weight:300; color:#fff; letter-spacing:0.12em; line-height:1; margin:0 auto 18px; text-shadow:0 4px 40px rgba(80,40,10,0.18); position:relative; z-index:2; text-align:center; width:100%; display:block; }
  .hero-sub { font-size:clamp(14px,1.6vw,17px); color:rgba(255,255,255,0.90); max-width:540px; line-height:1.8; margin:0 auto 40px; position:relative; z-index:2; text-align:center; display:block; }

  .section { background:#fdf0f0; text-align:center; padding:88px 48px 100px; width:100%; box-sizing:border-box; }
  .section-title { font-family:'Cormorant Garamond',serif; font-size:clamp(38px,5vw,60px); font-weight:400; color:#2b2318; margin:0 auto 20px; letter-spacing:0.02em; text-align:center; width:100%; display:block; }
  .section-sub { font-size:16px; color:#7a6555; width:100%; max-width:100%; margin:0 auto 56px; line-height:1.85; text-align:center; display:block; padding:0; box-sizing:border-box; }
  .cards { display:flex; justify-content:center; align-items:stretch; gap:32px; flex-wrap:wrap; max-width:1200px; margin:0 auto; padding:0 24px; }
  .card { background:#fdf0f0; border:1px solid #e8c4c4; padding:48px 36px; width:300px; min-height:260px; text-align:left; transition:transform 0.25s,box-shadow 0.25s; box-sizing:border-box; display:flex; flex-direction:column; }
  .card:hover { transform:translateY(-8px); box-shadow:0 20px 56px rgba(90,50,20,0.12); }
  .card-icon { font-size:40px; margin-bottom:20px; }
  .card-title { font-family:'Cormorant Garamond',serif; font-size:26px; font-weight:600; color:#2b2318; margin-bottom:14px; }
  .card-desc { font-size:15px; color:#6a5040; line-height:1.9; flex:1; }

  .upload-hero-small { position:relative; width:100%; min-height:28vh; background:linear-gradient(135deg,#c9a98a 0%,#d4b49a 30%,#b8906e 60%,#9a7357 100%); display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:80px 20px 36px; overflow:hidden; }
  .upload-hero-small::before { content:''; position:absolute; top:-80px; left:-80px; width:320px; height:320px; background:rgba(255,255,255,0.12); border-radius:50%; filter:blur(60px); }
  .page-title { font-family:'Cormorant Garamond',serif; font-size:clamp(36px,6vw,72px); font-weight:300; color:#fff; letter-spacing:0.12em; margin:0 0 10px; position:relative; z-index:2; }
  .page-sub { font-size:15px; color:rgba(255,255,255,0.85); position:relative; z-index:2; }

  .upload-body { background:#fdf0f0; padding:48px 24px 64px; display:flex; flex-direction:column; align-items:center; justify-content:center; width:100%; box-sizing:border-box; }
  .upload-box { background:#fff; border:2px dashed #c9a98a; padding:48px; width:100%; max-width:580px; text-align:center; margin:0 auto 28px; box-sizing:border-box; display:block; }
  .upload-box-icon { font-size:44px; margin-bottom:14px; }
  .upload-box-title { font-family:'Cormorant Garamond',serif; font-size:26px; color:#2b2318; margin-bottom:8px; }
  .upload-box-desc { font-size:13px; color:#8a7060; line-height:1.7; }
  .upload-formats { display:inline-block; background:#fdf0f0; color:#9a7357; font-size:11px; letter-spacing:0.14em; text-transform:uppercase; padding:6px 16px; margin-top:10px; }
  .stat-row { display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin:20px 0 32px; }
  .stat-box { background:#fff; border:1px solid #e8ddd6; padding:20px 28px; text-align:center; min-width:140px; }
  .stat-num { font-family:'Cormorant Garamond',serif; font-size:34px; font-weight:300; color:#9a7357; }
  .stat-label { font-size:11px; letter-spacing:0.14em; text-transform:uppercase; color:#8a7060; margin-top:4px; }
  .preview-title { font-family:'Cormorant Garamond',serif; font-size:26px; color:#2b2318; text-align:center; margin:40px 0 6px; }
  .preview-sub { font-size:13px; color:#8a7060; text-align:center; margin-bottom:20px; }

  .stButton > button { background:#2b2318 !important; color:#fdf0f0 !important; border:none !important; border-radius:0 !important; font-size:11px !important; font-weight:500 !important; letter-spacing:0.22em !important; text-transform:uppercase !important; padding:14px 40px !important; transition:all 0.3s !important; }
  .stButton > button:hover { background:#9a7357 !important; }

  /* FILE UPLOADER */
  [data-testid="stFileUploader"] { max-width:580px; margin:0 auto; display:block; }
  [data-testid="stFileUploaderDropzone"] {
    background:#3d1a1a !important;
    border-radius:0 !important;
    color:#fdf0f0 !important;
  }
  [data-testid="stFileUploaderDropzone"] * {
    color:#fdf0f0 !important;
    fill:#fdf0f0 !important;
  }
  [data-testid="stFileUploaderDropzone"] section,
  [data-testid="stFileUploaderDropzone"] section *,
  [data-testid="stFileUploaderDropzoneInstructions"] div,
  [data-testid="stFileUploaderDropzoneInstructions"] div *,
  div[data-testid="stFileUploader"] label,
  div[data-testid="stFileUploader"] label * {
    color:#fdf0f0 !important;
  }
  /* Nuclear option — force ALL text inside uploader white */
  div[data-testid="stFileUploader"] :not(button):not([data-testid="stFileUploaderFileName"]) {
    color:#fdf0f0 !important;
  }
  [data-testid="stFileUploaderDropzoneInstructions"] { color:#fdf0f0 !important; }
  [data-testid="stFileUploaderDropzoneInstructions"] * { color:#fdf0f0 !important; }
  [data-testid="stFileUploaderDropzone"] span,
  [data-testid="stFileUploaderDropzone"] p,
  [data-testid="stFileUploaderDropzone"] div,
  [data-testid="stFileUploaderDropzone"] label,
  [data-testid="stFileUploaderDropzone"] * { color:#fdf0f0 !important; }
  [data-testid="stFileUploaderDropzone"] button { background:#7a2a2a !important; color:#fdf0f0 !important; border:none !important; border-radius:0 !important; }
  [data-testid="stFileUploaderDropzone"] svg path,
  [data-testid="stFileUploaderDropzone"] svg rect,
  [data-testid="stFileUploaderDropzone"] svg circle,
  [data-testid="stFileUploaderDropzone"] svg * {
    fill:#fdf0f0 !important;
    stroke:none !important;
  }
  [data-testid="stFileUploaderDropzone"] small { color:#d4a0a0 !important; }
  [data-testid="stFileUploader"] span, [data-testid="stFileUploader"] p, [data-testid="stFileUploaderFileName"] { color:#3d1a1a !important; font-weight:500 !important; }

  /* DASHBOARD */
  .dash-header {
    background: linear-gradient(135deg,#c9a98a 0%,#d4b49a 30%,#b8906e 60%,#9a7357 100%);
    padding: 32px 40px 28px;
    position: relative;
    overflow: hidden;
    text-align: center;
  }
  .dash-header::before { content:''; position:absolute; top:-80px; left:-80px; width:320px; height:320px; background:rgba(255,255,255,0.10); border-radius:50%; filter:blur(60px); }
  .dash-header-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    position: relative;
    z-index: 2;
  }
  .dash-header-brand { font-size:11px; letter-spacing:0.22em; color:rgba(255,255,255,0.8); text-transform:uppercase; }
  .dash-header-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(28px, 4vw, 52px);
    font-weight: 300;
    color: #fff;
    letter-spacing: 0.1em;
    margin: 0 auto 8px;
    position: relative;
    z-index: 2;
    text-align: center;
    display: block;
  }
  .dash-header-sub {
    font-size: 13px;
    color: rgba(255,255,255,0.82);
    position: relative;
    z-index: 2;
    text-align: center;
    display: block;
  }
  /* Main dashboard container */
  .dash-container { background:#faeae0; border-radius:16px; margin:20px 80px; padding:28px 48px; box-sizing:border-box; }
  /* KPI column */
  .kpi-col { display:flex; flex-direction:column; gap:12px; height:100%; }
  .kpi-box { background:#fdf4ef; border-radius:12px; border:1px solid #e8d5c4; padding:20px 18px; flex:1; }
  .kpi-icon-label { display:flex; justify-content:space-between; align-items:center; margin-bottom:6px; }
  .kpi-emoji { font-size:28px; opacity:0.85; }
  .kpi-value { font-family:'Cormorant Garamond',serif; font-size:38px; font-weight:300; color:#2b2318; line-height:1; }
  .kpi-label { font-size:11px; letter-spacing:0.14em; text-transform:uppercase; color:#9a7060; }
  .kpi-sub { font-size:12px; color:#b89878; margin-top:6px; }
  /* Slicer row */
  .slicer-row { display:flex; gap:12px; margin-bottom:16px; flex-wrap:wrap; }

  /* Chart boxes */
  .chart-box { background:#fdf4ef; border-radius:12px; border:1px solid #e8d5c4; padding:14px 14px 6px; margin: 0 16px; }
  .chart-label { font-size:9px; letter-spacing:0.14em; text-transform:uppercase; color:#9a7357; margin-bottom:2px; }
  .chart-title { font-family:'Cormorant Garamond',serif; font-size:15px; font-weight:600; color:#2b2318; margin-bottom:1px; }
  .chart-subtitle { font-size:11px; color:#9a7060; margin-bottom:6px; }

  /* Bottom buttons */
  .dash-btn { background:#e8c4a0; border-radius:12px; padding:20px 32px; text-align:center; cursor:pointer; border:none; font-family:'DM Sans',sans-serif; font-size:13px; font-weight:500; color:#2b2318; letter-spacing:0.06em; width:100%; transition:background 0.2s; }
  .dash-btn:hover { background:#d4a878; }

  /* Insight page */
  .insight-page { background:#fdf0f0; padding:40px; }
  .insight-card { background:#fff; border:1px solid #e8d5c4; border-left:4px solid #9a7357; border-radius:8px; padding:16px 20px; margin-bottom:12px; font-size:13px; color:#2b2318; line-height:1.8; }
  .insight-number { font-family:'Cormorant Garamond',serif; font-size:28px; font-weight:300; color:#9a7357; margin-right:10px; }

  .divider { border:none; border-top:1px solid #e8d5c4; margin:16px 0; }
  .dash-sec-title { font-family:'Cormorant Garamond',serif; font-size:28px; font-weight:400; color:#2b2318; margin:0 0 4px; }
  .dash-sec-sub { font-size:12px; color:#9a7060; margin-bottom:14px; }
  .stSelectbox > div > div { border-color:#e8d5c4 !important; background:#fdf4ef !important; color:#2b2318 !important; border-radius:8px !important; }
  .stSelectbox label, 
  .stSelectbox label p,
  div[data-testid="stSelectbox"] label,
  div[data-testid="stSelectbox"] label * {
    color:#2b2318 !important;
    font-size:11px !important;
    font-weight:500 !important;
    letter-spacing:0.12em !important;
    text-transform:uppercase !important;
  }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "page"      not in st.session_state: st.session_state.page      = "home"
if "dataframe" not in st.session_state: st.session_state.dataframe = None
if "filename"  not in st.session_state: st.session_state.filename  = None

def get_subtitle(topic):
    topic_lower = topic.lower()
    if any(w in topic_lower for w in ["insurance","policy","claim","premium","coverage"]):
        return "Analysing policyholder profiles, claim patterns, and risk distribution across the portfolio"
    elif any(w in topic_lower for w in ["sales","revenue","profit","order","product"]):
        return "Tracking sales performance, revenue trends, and product-level insights across the dataset"
    elif any(w in topic_lower for w in ["spotify","music","song","track","artist","playlist"]):
        return "Exploring streaming trends, artist performance, and audio feature patterns across tracks"
    elif any(w in topic_lower for w in ["employee","hr","staff","salary","workforce","attrition"]):
        return "Understanding workforce composition, compensation trends, and employee retention patterns"
    elif any(w in topic_lower for w in ["customer","churn","retention","user","subscriber"]):
        return "Examining customer behaviour, engagement metrics, and churn risk indicators"
    elif any(w in topic_lower for w in ["finance","bank","loan","credit","transaction"]):
        return "Evaluating financial transactions, credit profiles, and risk exposure across segments"
    elif any(w in topic_lower for w in ["health","medical","patient","hospital","disease"]):
        return "Investigating patient demographics, clinical outcomes, and healthcare utilisation patterns"
    elif any(w in topic_lower for w in ["marketing","campaign","ad","click","conversion"]):
        return "Measuring campaign effectiveness, audience engagement, and conversion performance"
    else:
        return f"A comprehensive data-driven analysis of {topic} — uncovering trends, patterns, and key metrics"

COLORS = ["#9a7357","#c9a98a","#2b2318","#d4b49a","#5a3214","#b8906e","#7a5535","#e0c4b0"]
def style_fig(fig, height=260):
    fig.update_layout(
        plot_bgcolor="#fdf4ef", paper_bgcolor="#fdf4ef",
        font=dict(family="DM Sans", color="#2b2318", size=11),
        height=height,
        margin=dict(l=24, r=16, t=12, b=24),
        legend=dict(font=dict(color="#2b2318", size=10), bgcolor="rgba(0,0,0,0)"),
        xaxis=dict(tickfont=dict(color="#2b2318",size=10), title_font=dict(color="#2b2318",size=11), gridcolor="#f0e4d8"),
        yaxis=dict(tickfont=dict(color="#2b2318",size=10), title_font=dict(color="#2b2318",size=11), gridcolor="#f0e4d8"),
    )
    return fig

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — HOME
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
      <div class="shape shape-1"></div><div class="shape shape-2"></div><div class="shape shape-3"></div>
      <div class="navbar">
        <span class="nav-brand">AI · BI · Dashboard</span>
        <div class="nav-links"><span>Home</span><span>Upload</span><span>About</span></div>
      </div>
      <div class="hero-title">INSIGHT IQ</div>
      <p class="hero-sub">Upload your dataset and let AI automatically analyse your data, build charts, and surface the insights that matter.</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.5,1,1.5])
    with col2:
        if st.button("Upload Dataset →"):
            st.session_state.page = "upload"; st.rerun()
    st.markdown("""
    <div class="section">
      <div class="section-title">How It Works</div>
      <p class="section-sub">Three simple steps from raw data to a live, interactive business intelligence dashboard.</p>
      <div class="cards">
        <div class="card">
          <div class="card-icon">📂</div>
          <div class="card-title">Upload Your Data</div>
          <div class="card-desc">Drop in any CSV or Excel file. No formatting or coding required — just drag and drop your file to get started instantly.</div>
        </div>
        <div class="card">
          <div class="card-icon" style="font-size:40px;filter:saturate(2) brightness(0.3);">🤖</div>
          <div class="card-title">AI Analyses It</div>
          <div class="card-desc">Our AI engine automatically scans your dataset, detects patterns, identifies correlations, and computes key statistics.</div>
        </div>
        <div class="card">
          <div class="card-icon">📊</div>
          <div class="card-title">View Dashboard</div>
          <div class="card-desc">A full interactive dashboard with charts, KPIs, filters and insights is generated instantly — ready to explore and present.</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — UPLOAD
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "upload":
    st.markdown("""
    <div class="upload-hero-small">
      <div class="navbar">
        <span class="nav-brand">AI · BI · Dashboard</span>
        <div class="nav-links"><span>Home</span><span>Upload</span><span>About</span></div>
      </div>
      <div class="page-title">UPLOAD</div>
      <p class="page-sub">Drop your dataset below to get started</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="upload-body">', unsafe_allow_html=True)
    st.markdown("""
    <div class="upload-box">
      <div class="upload-box-icon">📂</div>
      <div class="upload-box-title">Select Your Dataset</div>
      <div class="upload-box-desc">Supports CSV and Excel files. Your data never leaves your machine.</div>
      <span class="upload-formats">CSV &nbsp;·&nbsp; XLS &nbsp;·&nbsp; XLSX</span>
    </div>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv","xlsx","xls"], label_visibility="collapsed")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            st.session_state.dataframe = df
            st.session_state.filename  = uploaded_file.name
            st.markdown(f"""
            <div class="stat-row">
              <div class="stat-box"><div class="stat-num">{df.shape[0]:,}</div><div class="stat-label">Rows</div></div>
              <div class="stat-box"><div class="stat-num">{df.shape[1]}</div><div class="stat-label">Columns</div></div>
              <div class="stat-box"><div class="stat-num">{df.isnull().sum().sum()}</div><div class="stat-label">Missing Values</div></div>
              <div class="stat-box"><div class="stat-num">{round(uploaded_file.size/1024,1)} KB</div><div class="stat-label">File Size</div></div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="preview-title">Data Preview</div>', unsafe_allow_html=True)
            st.markdown('<p class="preview-sub">Showing the first 5 rows of your dataset</p>', unsafe_allow_html=True)
            st.dataframe(df.head(), use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([2,1,2])
            with col2:
                if st.button("Generate Dashboard →"):
                    st.session_state.page = "dashboard"; st.rerun()
        except Exception as e:
            st.error(f"Could not read file: {e}")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("← Back to Home"):
            st.session_state.page = "home"; st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "dashboard":
    df_raw = st.session_state.dataframe
    if df_raw is None:
        st.warning("No dataset found.")
        if st.button("← Go to Upload"): st.session_state.page = "upload"; st.rerun()
    else:
        filename = st.session_state.filename or "Dataset"
        raw   = filename.replace(".csv","").replace(".xlsx","").replace(".xls","").replace("_"," ").replace("-"," ").strip()
        words = raw.split()
        stop  = {"the","a","an","of","and","in","on","at","to","for","by","with","from","3","2","1"}
        topic = " ".join([w.title() for w in words if w.lower() not in stop]).strip() or raw.title()

        num_cols = df_raw.select_dtypes(include=np.number).columns.tolist()
        cat_cols = df_raw.select_dtypes(include=["object","category"]).columns.tolist()
        df = df_raw.copy()

        # ── HEADER ────────────────────────────────────────────────────────────
        st.markdown(f"""
        <div class="dash-header">
          <div class="dash-header-nav">
            <span class="dash-header-brand">AI · BI · Dashboard</span>
            <span style="font-size:11px;color:rgba(255,255,255,0.65);letter-spacing:0.1em;">{filename}</span>
          </div>
          <div class="dash-header-title">{topic}</div>
          <div class="dash-header-sub">{get_subtitle(topic)}</div>
          </div>
        """, unsafe_allow_html=True)

        # ── SLICERS ───────────────────────────────────────────────────────────
        st.markdown("""
        <style>
          /* Remove ALL streamlit default padding */
          .block-container { padding: 1rem 5rem !important; max-width: 100% !important; }
          section[data-testid="stMain"] > div { padding: 0 !important; }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="dash-container">', unsafe_allow_html=True)

        if cat_cols:
           # Remove ID/unique columns from slicers
            smart_slicers = [
                c for c in cat_cols
                if (df[c].nunique() <= 50
                and not any(x in c.lower() for x in ["id","_id","code","number","num","date","time","name","email","phone","zip","url"]))
                or c.endswith("_month")
            ][:4]

            slicer_cols = st.columns(max(len(smart_slicers), 1))
            active = {}
            for i, col in enumerate(smart_slicers):
                with slicer_cols[i]:
                    nice_label = "Filter by " + col.replace("_month","").replace("_"," ").replace("-"," ").title()
                    if col.endswith("_month"):
                        # Sort months chronologically
                        try:
                            raw_months = df[col].dropna().unique().tolist()
                            sorted_months = sorted(raw_months, key=lambda x: pd.to_datetime(x, format="%b %Y", errors="coerce"))
                            opts = ["All"] + sorted_months
                        except:
                            opts = ["All"] + sorted(df[col].dropna().unique().tolist())
                    else:
                        opts = ["All"] + sorted(df[col].dropna().unique().tolist())
                    choice = st.selectbox(nice_label, opts, key=f"s_{col}")
                    active[col] = choice
            for col, val in active.items():
                if val != "All":
                    df = df[df[col] == val]

        st.markdown('<div class="dash-container">', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        # ── KPI + CHARTS LAYOUT ───────────────────────────────────────────────
        st.markdown('<div style="padding-left:32px;">', unsafe_allow_html=True)
        kpi_col, charts_col = st.columns([1, 4], gap="large")
        st.markdown('</div>', unsafe_allow_html=True)

        with kpi_col:
            st.markdown('<div style="display:flex;flex-direction:column;gap:12px;height:100%;">', unsafe_allow_html=True)
            # Smart KPI — only business-relevant numeric columns
            # Smart KPI — only business-relevant numeric columns
            kpi_num_cols = [
                c for c in num_cols
                if not any(x in c.lower() for x in [
                    "id","_id","code","zip","year","month","day","index","row","num","number"
                ])
            ]

            # Classify columns
            revenue_cols  = [c for c in kpi_num_cols if any(x in c.lower() for x in ["revenue","sales","income","price","amount","earning","profit","gmv","value","cost","sale"])]
            quantity_cols = [c for c in kpi_num_cols if any(x in c.lower() for x in ["quantity","qty","units","count","orders","volume","sold","purchases","clicks","impressions"])]
            cost_cols     = [c for c in kpi_num_cols if any(x in c.lower() for x in ["cost","spend","expense","budget","investment","cpc","cpm"])]
            rate_cols     = [c for c in kpi_num_cols if any(x in c.lower() for x in ["rate","ratio","percent","pct","score","rating","conversion","ctr","roas","roi"])]

            # KPI 1 — ROAS (Revenue / Cost) or ROI (Revenue / Qty) or best available
            kpis = []
            if revenue_cols and cost_cols:
                rev  = df[revenue_cols[0]].sum()
                cost = df[cost_cols[0]].sum()
                roas = round(rev / cost, 2) if cost > 0 else 0
                kpis.append(("ROAS", f"{roas:,.2f}x", f"Rev {rev:,.0f} / Cost {cost:,.0f}", "💹"))
            elif revenue_cols and quantity_cols:
                rev = df[revenue_cols[0]].sum()
                qty = df[quantity_cols[0]].sum()
                roi = round(rev / qty, 2) if qty > 0 else 0
                kpis.append(("ROI", f"{roi:,.2f}x", f"Rev {rev:,.0f} / Qty {qty:,.0f}", "💹"))
            elif rate_cols:
                c = rate_cols[0]
                kpis.append((f"Avg {c.replace('_',' ').title()[:14]}", f"{df[c].mean():,.2f}", f"Max {df[c].max():,.2f}", "💹"))
            elif kpi_num_cols:
                c = kpi_num_cols[0]
                kpis.append((f"Total {c.replace('_',' ').title()[:16]}", f"{df[c].sum():,.0f}", f"Avg {df[c].mean():,.1f}", "💰"))
            else:
                kpis.append(("Total Records", f"{len(df):,}", f"of {len(df_raw):,}", "📊"))

            # Classify columns by type
            revenue_cols  = [c for c in kpi_num_cols if any(x in c.lower() for x in ["revenue","sales","income","price","amount","earning","profit","gmv","value","cost"])]
            quantity_cols = [c for c in kpi_num_cols if any(x in c.lower() for x in ["quantity","qty","units","count","orders","volume","sold","purchases"])]
            rate_cols     = [c for c in kpi_num_cols if any(x in c.lower() for x in ["rate","ratio","percent","pct","score","rating","conversion","ctr","roas","roi"])]
            other_cols    = [c for c in kpi_num_cols if c not in revenue_cols + quantity_cols + rate_cols]

            kpis = []
            kpis.append(("Total Records", f"{len(df):,}", f"of {len(df_raw):,}", "📊"))

            # KPI 2 — Revenue/Sales total
            if revenue_cols:
                c = revenue_cols[0]
                kpis.append((
                    f"Total {c.replace('_',' ').title()[:16]}",
                    f"{df[c].sum():,.0f}",
                    f"Avg {df[c].mean():,.1f} per record",
                    "💰"
                ))
            elif kpi_num_cols:
                c = kpi_num_cols[0]
                kpis.append((
                    f"Total {c.replace('_',' ').title()[:16]}",
                    f"{df[c].sum():,.0f}",
                    f"Avg {df[c].mean():,.1f}",
                    "💰"
                ))

            # KPI 3 — Quantity/Volume
            if quantity_cols:
                c = quantity_cols[0]
                kpis.append((
                    f"Total {c.replace('_',' ').title()[:16]}",
                    f"{df[c].sum():,.0f}",
                    f"Avg {df[c].mean():,.1f} per record",
                    "📦"
                ))
            elif len(kpi_num_cols) >= 2:
                c = kpi_num_cols[1]
                kpis.append((
                    f"Avg {c.replace('_',' ').title()[:16]}",
                    f"{df[c].mean():,.1f}",
                    f"Max {df[c].max():,.0f}",
                    "📦"
                ))

         # KPI 4 — Performance metric (CTR, CPC, ROAS, ROI, Rate, Score)
            if rate_cols:
                c = rate_cols[0]
                # Detect what kind of metric it is
                if any(x in c.lower() for x in ["ctr","click_through","clickthrough"]):
                    label = "Avg CTR"
                    icon  = "🖱️"
                elif any(x in c.lower() for x in ["cpc","cost_per_click"]):
                    label = "Avg CPC"
                    icon  = "💸"
                elif any(x in c.lower() for x in ["roas","return_on_ad"]):
                    label = "Avg ROAS"
                    icon  = "📢"
                elif any(x in c.lower() for x in ["roi","return_on_inv"]):
                    label = "Avg ROI"
                    icon  = "💹"
                elif any(x in c.lower() for x in ["conversion","cvr"]):
                    label = "Conv. Rate"
                    icon  = "🎯"
                elif any(x in c.lower() for x in ["rating","score"]):
                    label = f"Avg {c.replace('_',' ').title()[:14]}"
                    icon  = "⭐"
                else:
                    label = f"Avg {c.replace('_',' ').title()[:14]}"
                    icon  = "📈"
                kpis.append((
                    label,
                    f"{df[c].mean():,.2f}",
                    f"Max {df[c].max():,.2f} · Min {df[c].min():,.2f}",
                    icon
                ))
            elif len(kpi_num_cols) >= 3:
                c = kpi_num_cols[2]
                kpis.append((
                    f"Avg {c.replace('_',' ').title()[:16]}",
                    f"{df[c].mean():,.1f}",
                    f"Max {df[c].max():,.0f}",
                    "📈"
                ))
            else:
                quality = 100 - round(df.isnull().sum().sum()*100/(df.shape[0]*df.shape[1]+1),1)
                kpis.append(("Data Quality", f"{quality}%", f"{df.isnull().sum().sum()} missing", "🎯"))
            for label, value, sub, icon in kpis:
                st.markdown(f"""
                <div class="kpi-box">
                  <div class="kpi-icon-label">
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-emoji">{icon}</div>
                  </div>
                  <div class="kpi-value">{value}</div>
                  <div class="kpi-sub">{sub}</div>
                </div>
                <br>
                """, unsafe_allow_html=True)

        with charts_col:
            r1c1, r1c2 = st.columns([1, 1])

            # Automatically pick best charts based on data
            chart_list = []

            # Chart A — Numeric distribution (histogram)
            if num_cols:
                chart_list.append(("hist", num_cols[0]))

            # Separate date cols from real cat cols
            date_cols    = [c for c in cat_cols if "date" in c.lower() or "time" in c.lower() or "year" in c.lower() or "month" in c.lower()]
            real_cat_cols = [c for c in cat_cols if c not in date_cols]

            # Chart B — Line if date exists, bar if category, else box plot
            if date_cols and num_cols:
                chart_list.append(("line", (date_cols[0], num_cols[0])))
            elif real_cat_cols:
                chart_list.append(("bar", real_cat_cols[0]))
            elif len(num_cols) >= 2:
                chart_list.append(("box", num_cols[1]))

            # Chart C — Scatter if 2 numeric, else another bar
            if len(num_cols) >= 2:
                chart_list.append(("scatter", (num_cols[0], num_cols[1])))
            elif len(real_cat_cols) >= 2:
                chart_list.append(("bar", real_cat_cols[1]))

            # Chart D — Pie from real cat cols only
            if real_cat_cols:
                pie_col_name = real_cat_cols[1] if len(real_cat_cols) >= 2 else real_cat_cols[0]
                chart_list.append(("pie", pie_col_name))
            elif len(num_cols) >= 3:
                chart_list.append(("hist", num_cols[2]))

            # Chart C — Scatter if 2 numeric, else another bar
            if len(num_cols) >= 2:
                chart_list.append(("scatter", (num_cols[0], num_cols[1])))
            elif len(cat_cols) >= 2:
                chart_list.append(("bar", cat_cols[1]))

            # Chart D — Pie if category exists, else histogram of 2nd numeric
            if cat_cols:
                pie_col = cat_cols[1] if len(cat_cols) >= 2 else cat_cols[0]
                chart_list.append(("pie", pie_col))
            elif len(num_cols) >= 3:
                chart_list.append(("hist", num_cols[2]))

            # Render charts in 2x2 grid
            positions = [(r1c1, 1), (r1c2, 2), None, None]
            r2c1, r2c2 = st.columns([1, 1])
            positions[2] = (r2c1, 3)
            positions[3] = (r2c2, 4)

            st.markdown('<br>', unsafe_allow_html=True)

            for idx, chart_info in enumerate(chart_list[:4]):
                col_container = positions[idx][0]
                chart_num     = positions[idx][1]
                chart_type    = chart_info[0]
                chart_data    = chart_info[1]

                with col_container:
                    if chart_type == "hist":
                        col_name = chart_data
                        st.markdown(f"""<div class="chart-box">
                          <div class="chart-label">Chart {chart_num} · Distribution</div>
                          <div class="chart-title">{col_name.replace("_"," ").title()}</div>
                          <div class="chart-subtitle">How values are spread</div>""", unsafe_allow_html=True)
                        fig = px.histogram(df, x=col_name, nbins=20, color_discrete_sequence=[COLORS[0]])
                        fig.update_traces(marker_line_color="#fff", marker_line_width=0.8)
                        st.plotly_chart(style_fig(fig), use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    elif chart_type == "bar":
                        col_name = chart_data
                        top_data = df[col_name].value_counts().head(10).reset_index()
                        top_data.columns = [col_name, "Count"]
                        st.markdown(f"""<div class="chart-box">
                          <div class="chart-label">Chart {chart_num} · Top 10</div>
                          <div class="chart-title">{col_name.replace("_"," ").title()}</div>
                          <div class="chart-subtitle">Top 10 categories by count</div>""", unsafe_allow_html=True)
                        fig = px.bar(top_data, x=col_name, y="Count",
                                     color=col_name, color_discrete_sequence=COLORS, text="Count")
                        fig.update_traces(textfont_color="#2b2318", textposition="outside", textfont_size=10)
                        fig.update_layout(showlegend=False)
                        st.plotly_chart(style_fig(fig), use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    elif chart_type == "box":
                        col_name = chart_data
                        st.markdown(f"""<div class="chart-box">
                          <div class="chart-label">Chart {chart_num} · Box Plot</div>
                          <div class="chart-title">{col_name.replace("_"," ").title()}</div>
                          <div class="chart-subtitle">Median, quartiles & outliers</div>""", unsafe_allow_html=True)
                        color_arg = cat_cols[0] if cat_cols else None
                        top_cats  = df[color_arg].value_counts().head(5).index if color_arg else None
                        df_box    = df[df[color_arg].isin(top_cats)] if color_arg else df
                        fig = px.box(df_box, y=col_name, color=color_arg,
                                     color_discrete_sequence=COLORS)
                        fig.update_layout(showlegend=False)
                        st.plotly_chart(style_fig(fig), use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    elif chart_type == "scatter":
                        x_col, y_col = chart_data
                        color_arg    = cat_cols[0] if cat_cols else None
                        top_cats     = df[color_arg].value_counts().head(5).index if color_arg else None
                        df_scatter   = df[df[color_arg].isin(top_cats)] if color_arg else df
                        st.markdown(f"""<div class="chart-box">
                          <div class="chart-label">Chart {chart_num} · Scatter</div>
                          <div class="chart-title">{x_col.replace("_"," ").title()} vs {y_col.replace("_"," ").title()}</div>
                          <div class="chart-subtitle">Top 5 categories shown</div>""", unsafe_allow_html=True)
                        fig = px.scatter(df_scatter, x=x_col, y=y_col,
                                         color=color_arg,
                                         color_discrete_sequence=COLORS, opacity=0.7)
                        st.plotly_chart(style_fig(fig), use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    elif chart_type == "line":
                        date_col, val_col = chart_data
                        df_line = df[[date_col, val_col]].dropna()
                        df_line[date_col] = pd.to_datetime(df_line[date_col], errors="coerce")
                        df_line = df_line.dropna().sort_values(date_col)
                        df_line = df_line.groupby(date_col)[val_col].sum().reset_index().tail(50)
                        st.markdown(f"""<div class="chart-box">
                          <div class="chart-label">Chart {chart_num} · Trend</div>
                          <div class="chart-title">{val_col.replace("_"," ").title()} Over Time</div>
                          <div class="chart-subtitle">How {val_col.replace("_"," ").title()} changes over time</div>""", unsafe_allow_html=True)
                        fig = px.line(df_line, x=date_col, y=val_col,
                                      color_discrete_sequence=[COLORS[0]])
                        fig.update_traces(line_width=2)
                        st.plotly_chart(style_fig(fig), use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    elif chart_type == "pie":
                        col_name = chart_data
                        pie_data = df[col_name].value_counts().head(5).reset_index()
                        pie_data.columns = [col_name, "Count"]
                        st.markdown(f"""<div class="chart-box">
                          <div class="chart-label">Chart {chart_num} · Top 5 Share</div>
                          <div class="chart-title">{col_name.replace("_"," ").title()}</div>
                          <div class="chart-subtitle">Top 5 categories by share</div>""", unsafe_allow_html=True)
                        fig = px.pie(pie_data, names=col_name, values="Count",
                                     color_discrete_sequence=COLORS, hole=0.42)
                        fig.update_traces(
                            textfont_color="#ffffff",
                            textfont_size=12,
                            textinfo="percent+label",
                            textposition="inside",
                            insidetextorientation="radial",
                            pull=[0.03] * len(pie_data),
                            marker=dict(line=dict(color="#fdf4ef", width=2))
                        )
                        fig.update_layout(
                            showlegend=True,
                            legend=dict(
                                font=dict(color="#2b2318", size=11),
                                orientation="v",
                                x=1.02, y=0.5
                            )
                        )
                        st.plotly_chart(style_fig(fig), use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)

        # ── BOTTOM BUTTONS ────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2, b3, b4 = st.columns([1,1,1,1])
        with b2:
            if st.button("🤖 View AI Insights"):
                st.session_state.page = "insights"; st.rerun()
        with b3:
            if st.button("📋 Statistical Summary"):
                st.session_state.page = "summary"; st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2,1,2])
        with col2:
            if st.button("← Upload New Dataset"):
                st.session_state.page = "upload"
                st.session_state.dataframe = None; st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — AI INSIGHTS
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "insights":
    df = st.session_state.dataframe
    if df is None:
        st.warning("No dataset."); st.stop()

    filename = st.session_state.filename or "Dataset"
    topic    = filename.replace(".csv","").replace(".xlsx","").replace("_"," ").replace("-"," ").title()
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    cat_cols = df.select_dtypes(include=["object","category"]).columns.tolist()

    st.markdown(f"""
    <div class="dash-header">
      <div class="dash-header-nav">
        <span class="dash-header-brand">AI · BI · Dashboard</span>
        <span style="font-size:11px;color:rgba(255,255,255,0.65);">{filename}</span>
      </div>
      <div class="dash-header-title">AI Insights — {topic}</div>
      <div class="dash-header-sub">Key patterns and quantitative findings discovered in the {topic} dataset</div>
      </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="padding:36px 40px 60px;background:#fdf0f0;">', unsafe_allow_html=True)

    insights = []

    if num_cols:
        for col in num_cols[:6]:
            mean_val  = df[col].mean()
            max_val   = df[col].max()
            min_val   = df[col].min()
            std_val   = df[col].std()
            pct_above = round((df[col] > mean_val).sum() * 100 / len(df), 1)
            insights.append(f"📊 <b>{col}</b> — Average: <b>{mean_val:,.2f}</b> · Max: <b>{max_val:,.2f}</b> · Min: <b>{min_val:,.2f}</b> · Std Dev: <b>{std_val:,.2f}</b> · <b>{pct_above}%</b> of records are above average.")

    if df.isnull().sum().sum() > 0:
        for col in df.columns:
            missing = df[col].isnull().sum()
            if missing > 0:
                pct = round(missing * 100 / len(df), 1)
                insights.append(f"⚠️ <b>{col}</b> has <b>{missing:,} missing values</b> ({pct}% of total rows).")
    else:
        insights.append(f"✅ Dataset is <b>100% complete</b> — all {df.shape[0]:,} rows × {df.shape[1]} columns have values with <b>0 missing entries</b>.")

    if df.duplicated().sum() > 0:
        pct_dup = round(df.duplicated().sum() * 100 / len(df), 1)
        insights.append(f"🔁 Found <b>{df.duplicated().sum():,} duplicate rows</b> ({pct_dup}% of total dataset).")
    else:
        insights.append(f"✅ <b>No duplicate rows</b> found across all {df.shape[0]:,} records.")

    if cat_cols:
        for col in cat_cols[:3]:
            top_val   = df[col].value_counts().index[0]
            top_count = df[col].value_counts().iloc[0]
            top_pct   = round(top_count * 100 / len(df), 1)
            n_unique  = df[col].nunique()
            insights.append(f"🏷️ <b>{col}</b> has <b>{n_unique} unique values</b>. Most common: <b>'{top_val}'</b> appearing <b>{top_count:,} times</b> ({top_pct}% of records).")

    if len(num_cols) >= 2:
        corr = df[num_cols].corr().abs()
        np.fill_diagonal(corr.values, 0)
        pair = corr.stack().idxmax()
        val  = corr.stack().max()
        insights.append(f"🔗 Strongest correlation: <b>{pair[0]}</b> ↔ <b>{pair[1]}</b> with r = <b>{val:.3f}</b> — {'strong positive' if val > 0.7 else 'moderate'} relationship.")

    # Show in 2 columns
    left_ins  = insights[:len(insights)//2 + len(insights)%2]
    right_ins = insights[len(insights)//2 + len(insights)%2:]
    ic1, ic2  = st.columns(2)
    with ic1:
        for ins in left_ins:
            st.markdown(f'<div class="insight-card">{ins}</div>', unsafe_allow_html=True)
    with ic2:
        for ins in right_ins:
            st.markdown(f'<div class="insight-card">{ins}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("← Back to Dashboard"):
            st.session_state.page = "dashboard"; st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — STATISTICAL SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "summary":
    df = st.session_state.dataframe
    if df is None:
        st.warning("No dataset."); st.stop()

    filename = st.session_state.filename or "Dataset"
    topic    = filename.replace(".csv","").replace(".xlsx","").replace("_"," ").replace("-"," ").title()
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    cat_cols = df.select_dtypes(include=["object","category"]).columns.tolist()

    st.markdown(f"""
    <div class="dash-header">
      <div class="dash-header-nav">
        <span class="dash-header-brand">AI · BI · Dashboard</span>
        <span style="font-size:11px;color:rgba(255,255,255,0.65);">{filename}</span>
      </div>
      <div class="dash-header-title">Statistical Summary — {topic}</div>
      <div class="dash-header-sub">Complete statistical breakdown of all columns in the {topic} dataset</div>
      </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="padding:36px 40px 60px;background:#fdf0f0;">', unsafe_allow_html=True)

    if num_cols:
        st.markdown('<div class="dash-sec-title">📊 Numeric Columns</div>', unsafe_allow_html=True)
        st.markdown('<div class="dash-sec-sub">Count, mean, std deviation, min, quartiles and max for each numeric column</div>', unsafe_allow_html=True)
        st.dataframe(df[num_cols].describe().round(3), use_container_width=True)

    if cat_cols:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="dash-sec-title">🏷️ Categorical Columns</div>', unsafe_allow_html=True)
        st.markdown('<div class="dash-sec-sub">Unique values, most frequent value and its count</div>', unsafe_allow_html=True)
        cat_summary = pd.DataFrame({
            "Column"         : cat_cols,
            "Unique Values"  : [df[c].nunique() for c in cat_cols],
            "Most Frequent"  : [df[c].value_counts().index[0] for c in cat_cols],
            "Frequency Count": [df[c].value_counts().iloc[0] for c in cat_cols],
            "Frequency %"    : [f"{round(df[c].value_counts().iloc[0]*100/len(df),1)}%" for c in cat_cols],
            "Missing Values" : [df[c].isnull().sum() for c in cat_cols],
        })
        st.dataframe(cat_summary, use_container_width=True)

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div class="dash-sec-title">🔍 Missing Values Summary</div>', unsafe_allow_html=True)
    missing_df = pd.DataFrame({
        "Column"  : df.columns,
        "Missing" : df.isnull().sum().values,
        "% Missing": [f"{round(v*100/len(df),1)}%" for v in df.isnull().sum().values],
    }).query("Missing > 0")
    if len(missing_df) > 0:
        st.dataframe(missing_df, use_container_width=True)
    else:
        st.markdown('<div class="insight-card">✅ No missing values found in any column!</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("← Back to Dashboard"):
            st.session_state.page = "dashboard"; st.rerun()