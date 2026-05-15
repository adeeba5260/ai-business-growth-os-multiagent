import streamlit as st
from app import run_system
import plotly.graph_objects as go
import json
import re

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Growth OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body { font-family: 'DM Sans', sans-serif !important; background: #0c0c12 !important; }
[data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] > .main, .stApp { background: #0c0c12 !important; }
[data-testid="stHeader"] { background: transparent !important; height: 0 !important; visibility: hidden !important; }
.main .block-container { padding: 2rem 2.5rem 4rem 2.5rem !important; max-width: 1380px; margin: 0 auto; background: #0c0c12 !important; }

[data-testid="stSidebar"] { background: #111118 !important; border-right: 1px solid rgba(255,255,255,0.07) !important; min-height: 100vh !important; }
[data-testid="stSidebar"] > div { padding: 0 !important; overflow-y: auto !important; overflow-x: hidden !important; height: 100vh !important; }
[data-testid="stSidebar"] .block-container { padding: 0 !important; background: transparent !important; }
[data-testid="stSidebar"] .stSelectbox label, [data-testid="stSidebar"] .stTextInput label { color: #a0a0c0 !important; font-size: 13px !important; font-weight: 500 !important; font-family: 'DM Sans', sans-serif !important; margin-bottom: 4px !important; }
[data-testid="stSidebar"] div[data-baseweb="select"] > div { background: #1c1c28 !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 9px !important; color: #e8e8f0 !important; font-size: 14px !important; font-family: 'DM Sans', sans-serif !important; min-height: 42px !important; }
[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover { border-color: rgba(124,92,252,0.45) !important; }
[data-testid="stSidebar"] .stTextInput > div > div > input { background: #1c1c28 !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 9px !important; color: #e8e8f0 !important; font-size: 14px !important; font-family: 'DM Sans', sans-serif !important; padding: 10px 14px !important; }
[data-testid="stSidebar"] [data-baseweb="select"] span, [data-testid="stSidebar"] [data-baseweb="select"] div[class*="ValueContainer"] { color: #e8e8f0 !important; font-size: 14px !important; }
[data-testid="stSidebar"] .stButton > button { width: 100% !important; background: linear-gradient(135deg, #7c5cfc 0%, #4facfe 100%) !important; color: #ffffff !important; border: none !important; border-radius: 11px !important; padding: 14px 20px !important; font-family: 'Sora', sans-serif !important; font-size: 14px !important; font-weight: 700 !important; cursor: pointer !important; transition: all 0.25s ease !important; box-shadow: 0 4px 24px rgba(124,92,252,0.4) !important; min-height: 48px !important; }
[data-testid="stSidebar"] .stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 32px rgba(124,92,252,0.55) !important; }

.sb-logo { padding: 22px 20px 18px; border-bottom: 1px solid rgba(255,255,255,0.07); margin-bottom: 4px; }
.sb-logo-row { display: flex; align-items: center; gap: 12px; }
.sb-logo-icon { width: 38px; height: 38px; background: linear-gradient(135deg, #7c5cfc, #4facfe); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; }
.sb-logo-name { font-family: 'Sora', sans-serif; font-size: 16px; font-weight: 800; color: #ffffff; letter-spacing: -0.3px; line-height: 1.1; }
.sb-logo-sub { font-size: 10px; color: #5a5a7a; font-weight: 500; text-transform: uppercase; letter-spacing: 0.8px; }
.sb-section { padding: 16px 20px 6px; font-size: 10px; font-weight: 700; color: #4a4a6a; text-transform: uppercase; letter-spacing: 1.2px; font-family: 'Sora', sans-serif; }
.sb-divider { height: 1px; background: rgba(255,255,255,0.06); margin: 8px 16px; }

.page-header { background: linear-gradient(135deg, #15151f 0%, #1c1830 100%); border: 1px solid rgba(124,92,252,0.2); border-radius: 20px; padding: 28px 36px; margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05); }
.page-header-title { font-family: 'Sora', sans-serif; font-size: 32px; font-weight: 800; letter-spacing: -1px; background: linear-gradient(135deg, #ffffff 0%, #b8a0ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 6px; line-height: 1.1; }
.page-header-sub { font-size: 15px; color: #6a6a8a; font-weight: 400; font-family: 'DM Sans', sans-serif; }
.header-chip { background: rgba(124,92,252,0.14); border: 1px solid rgba(124,92,252,0.35); color: #c0aaff; padding: 10px 22px; border-radius: 30px; font-size: 12px; font-weight: 700; font-family: 'Sora', sans-serif; letter-spacing: 0.8px; text-transform: uppercase; white-space: nowrap; box-shadow: 0 0 20px rgba(124,92,252,0.2); }

.success-banner { display: flex; align-items: center; gap: 12px; background: rgba(34,197,94,0.08); border: 1px solid rgba(34,197,94,0.25); border-radius: 12px; padding: 14px 20px; margin-bottom: 20px; font-size: 15px; font-weight: 500; color: #4ade80; font-family: 'DM Sans', sans-serif; }

.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
.kpi-card { background: #14141e; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 22px 20px; position: relative; overflow: hidden; transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s; }
.kpi-card::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; border-radius: 16px 16px 0 0; }
.kpi-c1::after { background: linear-gradient(90deg, #7c5cfc, #a78bfa); }
.kpi-c2::after { background: linear-gradient(90deg, #4facfe, #00f2fe); }
.kpi-c3::after { background: linear-gradient(90deg, #11998e, #38ef7d); }
.kpi-c4::after { background: linear-gradient(90deg, #f7971e, #ffd200); }
.kpi-card:hover { transform: translateY(-3px); border-color: rgba(124,92,252,0.25); box-shadow: 0 12px 40px rgba(0,0,0,0.3); }
.kpi-icon-box { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; margin-bottom: 16px; }
.kpi-c1 .kpi-icon-box { background: rgba(124,92,252,0.12); }
.kpi-c2 .kpi-icon-box { background: rgba(79,172,254,0.12); }
.kpi-c3 .kpi-icon-box { background: rgba(56,239,125,0.12); }
.kpi-c4 .kpi-icon-box { background: rgba(255,210,0,0.12); }
.kpi-label { font-size: 11px; font-weight: 700; color: #5a5a7a; text-transform: uppercase; letter-spacing: 0.9px; margin-bottom: 6px; font-family: 'Sora', sans-serif; }
.kpi-value { font-family: 'Sora', sans-serif; font-size: 34px; font-weight: 800; color: #ffffff; letter-spacing: -1.5px; line-height: 1; margin-bottom: 10px; }
.kpi-trend { font-size: 12px; font-weight: 600; padding: 3px 10px; border-radius: 8px; display: inline-block; font-family: 'DM Sans', sans-serif; }
.trend-up  { color: #4ade80; background: rgba(74,222,128,0.1); }
.trend-down{ color: #f87171; background: rgba(248,113,113,0.1); }
.trend-neu { color: #a78bfa; background: rgba(167,139,250,0.1); }

.stTabs [data-baseweb="tab-list"] { background: #14141e !important; border: 1px solid rgba(255,255,255,0.08) !important; border-radius: 14px !important; padding: 6px !important; gap: 4px !important; }
.stTabs [data-baseweb="tab"] { background: transparent !important; border-radius: 9px !important; padding: 11px 24px !important; font-family: 'DM Sans', sans-serif !important; font-size: 15px !important; font-weight: 500 !important; color: #6a6a8a !important; border: none !important; transition: all 0.2s !important; white-space: nowrap !important; }
.stTabs [data-baseweb="tab"]:hover { color: #b0b0d0 !important; background: rgba(255,255,255,0.04) !important; }
.stTabs [aria-selected="true"] { background: linear-gradient(135deg, #7c5cfc 0%, #4facfe 100%) !important; color: #ffffff !important; box-shadow: 0 2px 16px rgba(124,92,252,0.45) !important; font-weight: 600 !important; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none !important; }

.sec-hdr { display: flex; align-items: center; gap: 12px; margin: 24px 0 14px; }
.sec-hdr-icon { width: 34px; height: 34px; background: rgba(124,92,252,0.12); border: 1px solid rgba(124,92,252,0.22); border-radius: 9px; display: flex; align-items: center; justify-content: center; font-size: 15px; }
.sec-hdr-title { font-family: 'Sora', sans-serif; font-size: 18px; font-weight: 700; color: #ffffff; letter-spacing: -0.4px; }

.content-card { background: #14141e; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 22px 24px; font-size: 15px; line-height: 1.75; color: #c8c8e0; font-family: 'DM Sans', sans-serif; transition: border-color 0.2s; }
.content-card:hover { border-color: rgba(124,92,252,0.22); }

.idea-card { background: #14141e; border: 1px solid rgba(255,255,255,0.07); border-radius: 13px; padding: 16px 20px; margin-bottom: 12px; transition: all 0.2s; }
.idea-card:hover { border-color: rgba(124,92,252,0.28); transform: translateX(3px); }
.idea-num { font-size: 11px; font-weight: 700; color: #7c5cfc; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 7px; font-family: 'Sora', sans-serif; }
.idea-text { font-size: 15px; color: #c8c8e0; line-height: 1.65; font-family: 'DM Sans', sans-serif; }

.hashtag-cloud { background: #14141e; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px 20px; display: flex; flex-wrap: wrap; gap: 10px; }
.htag { background: rgba(124,92,252,0.1); border: 1px solid rgba(124,92,252,0.22); color: #b0a0f8; padding: 6px 14px; border-radius: 22px; font-size: 13px; font-weight: 500; font-family: 'DM Sans', sans-serif; transition: all 0.15s; cursor: default; }
.htag:hover { background: rgba(124,92,252,0.2); border-color: rgba(124,92,252,0.4); transform: scale(1.05); }

.reel-card { background: #14141e; border: 1px solid rgba(255,255,255,0.07); border-radius: 14px; overflow: hidden; margin-bottom: 14px; transition: all 0.2s; }
.reel-card:hover { border-color: rgba(124,92,252,0.28); transform: translateY(-2px); box-shadow: 0 8px 30px rgba(0,0,0,0.25); }
.reel-hdr { background: rgba(124,92,252,0.1); border-bottom: 1px solid rgba(124,92,252,0.1); padding: 12px 18px; font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #b0a0f8; display: flex; align-items: center; gap: 8px; }
.reel-body { padding: 16px 18px; font-size: 14px; color: #a0a0c0; line-height: 1.65; font-family: 'DM Sans', sans-serif; white-space: pre-wrap; }

.cal-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 10px; margin-bottom: 24px; }
.cal-day { background: #14141e; border: 1px solid rgba(255,255,255,0.08); border-radius: 13px; padding: 14px 10px; text-align: center; min-height: 110px; transition: all 0.2s; }
.cal-day:hover { border-color: rgba(124,92,252,0.3); transform: translateY(-2px); }
.cal-day-name { font-family: 'Sora', sans-serif; font-size: 11px; font-weight: 700; color: #7c5cfc; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 9px; display: block; }
.cal-day-text { font-size: 12px; color: #9898b8; line-height: 1.5; font-family: 'DM Sans', sans-serif; }

.ad-card { background: #14141e; border: 1px solid rgba(255,255,255,0.07); border-radius: 13px; padding: 14px 16px; margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start; transition: all 0.2s; font-family: 'DM Sans', sans-serif; }
.ad-card:hover { border-color: rgba(79,172,254,0.3); }
.ad-card-icon { font-size: 16px; flex-shrink: 0; margin-top: 2px; }
.ad-card-text { font-size: 14px; color: #c0c0d8; line-height: 1.6; }

.tip-card { background: linear-gradient(135deg, rgba(17,153,142,0.08) 0%, rgba(56,239,125,0.04) 100%); border: 1px solid rgba(56,239,125,0.15); border-radius: 13px; padding: 16px 18px; margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start; font-family: 'DM Sans', sans-serif; }
.tip-icon { font-size: 16px; flex-shrink: 0; margin-top: 2px; }
.tip-text { font-size: 15px; color: #c0c0d8; line-height: 1.6; }

.level-banner { text-align: center; border-radius: 18px; padding: 32px; margin-top: 24px; }
.level-banner h2 { font-family: 'Sora', sans-serif; font-size: 26px; font-weight: 800; margin-bottom: 8px; }
.level-banner p { font-size: 15px; color: #8888a8; font-family: 'DM Sans', sans-serif; }

.empty-state { text-align: center; padding: 6rem 2rem; background: #12121c; border: 1px dashed rgba(255,255,255,0.1); border-radius: 22px; margin-top: 1rem; }
.empty-icon { font-size: 54px; display: block; margin-bottom: 20px; }
.empty-title { font-family: 'Sora', sans-serif; font-size: 22px; font-weight: 700; color: #ffffff; margin-bottom: 10px; }
.empty-sub { font-size: 15px; color: #5a5a7a; margin-bottom: 28px; }
.empty-cta { background: rgba(124,92,252,0.1); border: 1px solid rgba(124,92,252,0.25); color: #a78bfa; padding: 12px 28px; border-radius: 10px; font-size: 14px; font-weight: 600; display: inline-block; font-family: 'DM Sans', sans-serif; }

#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; visibility: hidden !important; }
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(124,92,252,0.3); border-radius: 3px; }
.stSpinner > div > div { border-top-color: #7c5cfc !important; }
.streamlit-expanderHeader { background: #14141e !important; border-radius: 10px !important; color: #c0c0d8 !important; font-size: 14px !important; font-family: 'DM Sans', sans-serif !important; }
</style>
""", unsafe_allow_html=True)


# ========== DATA PARSING HELPERS ==========

def extract_last_json_block(text):
    """
    Find the LAST ```json ... ``` block in a string and parse it.
    Falls back to finding the last bare { ... } object if no fenced block found.
    This handles the case where run_system returns a markdown+JSON mixed string.
    """
    if not isinstance(text, str):
        return {} if not isinstance(text, dict) else text

    # Find all ```json ... ``` blocks, return the last one parsed as dict
    fenced = re.findall(r'```(?:json)?\s*(\{[\s\S]*?\})\s*```', text)
    for block in reversed(fenced):
        try:
            parsed = json.loads(block)
            if isinstance(parsed, dict) and len(parsed) > 0:
                return parsed
        except Exception:
            continue

    # No fenced block worked — try finding last bare JSON object
    # Match outermost { } spanning multiple lines
    bare = list(re.finditer(r'\{[\s\S]*?\}', text))
    for m in reversed(bare):
        try:
            parsed = json.loads(m.group())
            if isinstance(parsed, dict) and len(parsed) > 0:
                return parsed
        except Exception:
            continue

    return {}


def safe_parse(data):
    """Return a dict from data (dict, JSON string, or markdown+JSON string)."""
    if isinstance(data, dict):
        return data
    if isinstance(data, str):
        # First try direct JSON parse (clean string)
        cleaned = re.sub(r"```(?:json)?", "", data).replace("```", "").strip()
        try:
            parsed = json.loads(cleaned)
            if isinstance(parsed, dict):
                return parsed
        except Exception:
            pass
        # Fallback: extract last JSON block from messy markdown string
        return extract_last_json_block(data)
    return {}


def parse_list(data, key):
    """Return a clean list from a dict key."""
    if not isinstance(data, dict):
        return []
    val = data.get(key, [])
    if isinstance(val, list):
        return [str(v).strip() for v in val if str(v).strip()]
    if isinstance(val, str):
        return [v.strip() for v in val.splitlines() if v.strip()]
    return []


def get_strategy_lists(result):
    """
    Robustly extract weekly_plan, ads, growth_tips from result.
    Handles: dict with 'strategy' key (dict or messy string).
    Always uses the LAST JSON block in the string — which is the clean
    final summary that run_system appends at the end.
    """
    raw = result.get("strategy", {})

    # Parse the strategy value — if it's a messy string, grab last JSON block
    parsed = safe_parse(raw)

    weekly_plan = parse_list(parsed, "weekly_plan")
    ads         = parse_list(parsed, "ads")
    tips        = parse_list(parsed, "growth_tips")

    return weekly_plan, ads, tips


# ========== UI HELPERS ==========
def kpi_card(label, value, icon, color_cls, trend, trend_cls):
    return f"""
    <div class="kpi-card {color_cls}">
        <div class="kpi-icon-box">{icon}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <span class="kpi-trend {trend_cls}">{trend}</span>
    </div>"""


def sec_hdr(icon, title):
    st.markdown(f"""
    <div class="sec-hdr">
        <div class="sec-hdr-icon">{icon}</div>
        <span class="sec-hdr-title">{title}</span>
    </div>""", unsafe_allow_html=True)


def make_gauge(value, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 14, 'color': '#9898b8', 'family': 'DM Sans'}},
        number={'font': {'size': 44, 'color': '#ffffff', 'family': 'Sora'}, 'suffix': '%'},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 0, 'tickcolor': 'rgba(0,0,0,0)', 'tickfont': {'color': '#5a5a7a', 'size': 10}, 'ticklen': 0},
            'bar': {'color': "#7c5cfc", 'thickness': 0.65},
            'bgcolor': "#1c1c2a", 'borderwidth': 0,
            'steps': [
                {'range': [0,  40], 'color': 'rgba(248,113,113,0.12)'},
                {'range': [40, 70], 'color': 'rgba(250,204,21,0.10)'},
                {'range': [70,100], 'color': 'rgba(74,222,128,0.10)'}
            ],
            'threshold': {'line': {'color': "#4facfe", 'width': 3}, 'thickness': 0.75, 'value': value}
        }
    ))
    fig.update_layout(height=240, margin=dict(l=20, r=20, t=50, b=10),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      font={'family': 'DM Sans'})
    return fig


def make_bar(labels, values, title):
    fig = go.Figure(data=[go.Bar(
        x=labels, y=values,
        marker=dict(color=['rgba(124,92,252,0.85)', 'rgba(79,172,254,0.85)', 'rgba(56,239,125,0.85)'], line=dict(width=0)),
        text=[f"{int(v):,}" for v in values], textposition='outside',
        textfont=dict(color='#9898b8', size=13, family='DM Sans')
    )])
    fig.update_layout(
        title=dict(text=title, font=dict(size=14, color='#9898b8', family='DM Sans')),
        height=240, margin=dict(l=10, r=10, t=50, b=30),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        xaxis=dict(showgrid=False, color='#5a5a7a', tickfont=dict(size=12, family='DM Sans')),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', color='#5a5a7a', zeroline=False, tickfont=dict(size=12))
    )
    return fig


# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("""
    <div class="sb-logo">
        <div class="sb-logo-row">
            <div class="sb-logo-icon">⚡</div>
            <div>
                <div class="sb-logo-name">Growth OS</div>
                <div class="sb-logo-sub">AI Marketing Suite</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">Business</div>', unsafe_allow_html=True)
    business = st.selectbox("Business Type", [
        "Food & Bakery", "Beauty & Salon", "Education & Coaching",
        "Clothing & Fashion", "Fitness & Health", "Freelancer / Services",
        "Digital Creator", "Local Shop / Retail", "Custom"
    ])
    sub_type = None
    if business == "Food & Bakery":
        sub_type = st.selectbox("Business Detail", ["Home Bakery", "Cloud Kitchen", "Cafe"])
    elif business == "Beauty & Salon":
        sub_type = st.selectbox("Business Detail", ["Salon", "Makeup Artist", "Mehendi Artist"])
    elif business == "Custom":
        sub_type = st.text_input("Describe your business")
    final_business = sub_type if sub_type else business

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-section">Audience</div>', unsafe_allow_html=True)
    audience_opt = st.selectbox("Audience Segment", [
        "College Students", "Working Professionals", "Housewives",
        "Small Business Owners", "Custom"
    ])
    audience = st.text_input("Custom Audience") if audience_opt == "Custom" else audience_opt
    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("Age Group", ["18-25", "25-40", "40+"])
    with col2:
        location = st.selectbox("Location", ["Urban", "Rural"])

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-section">Goals</div>', unsafe_allow_html=True)
    platform = st.selectbox("Platform", ["Instagram", "YouTube", "WhatsApp", "Facebook"])
    goal     = st.selectbox("Primary Goal", ["Increase Followers", "Increase Sales", "Brand Awareness"])
    budget   = st.selectbox("Budget Level", ["Low", "Medium", "High"])

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
    generate_btn = st.button("⚡ Generate Growth Plan", use_container_width=True)
    if 'result' in st.session_state and st.session_state.result:
        if st.button("↺  Reset", use_container_width=True):
            st.session_state.result = None
            st.rerun()


# ========== MAIN ==========
if 'result' not in st.session_state:
    st.session_state.result = None

st.markdown("""
<div class="page-header">
    <div>
        <div class="page-header-title">AI Business Growth OS</div>
        <div class="page-header-sub">AI-powered marketing strategy for small businesses</div>
    </div>
    <span class="header-chip">⚡ Powered by Claude</span>
</div>
""", unsafe_allow_html=True)

if generate_btn:
    with st.spinner("🤖 Crafting your personalised growth strategy..."):
        st.session_state.result = run_system(
            final_business, audience, age, location, platform, goal, budget
        )

# ========== RESULTS ==========
if st.session_state.result:
    result = st.session_state.result

    st.markdown('<div class="success-banner">✅ &nbsp;Your growth plan is ready!</div>',
                unsafe_allow_html=True)

    growth   = safe_parse(result.get("growth",  {}))
    content  = safe_parse(result.get("content", {}))

    score      = int(growth.get("score", 0) or 0)
    min_val    = int(growth.get("followers_min", 0) or 0)
    max_val    = int(growth.get("followers_max", 0) or 0)
    followers  = growth.get("followers", "—") or "—"
    time_weeks = 2 if score >= 80 else (4 if score >= 60 else 8)
    fdisp      = followers if followers not in ("N/A", "—", "", None) else "—"
    q_score    = int(result.get("score", 0) or 0)

    st.markdown(f"""
    <div class="kpi-row">
        {kpi_card("Quality Score",    f"{q_score}/100",                     "⭐", "kpi-c1", "↑ Above avg",    "trend-up")}
        {kpi_card("Growth Potential", f"{score}%",                          "📈", "kpi-c2", "↑ +12% vs last", "trend-up")}
        {kpi_card("Est. Followers",   fdisp if fdisp != "—" else "Pending", "👥", "kpi-c3", "→ Monthly gain",  "trend-neu")}
        {kpi_card("Time to Results",  f"{time_weeks} wks",                  "⏱️", "kpi-c4", "→ Estimated",    "trend-neu")}
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "📊  Insights & Analysis",
        "✍️  Content Strategy",
        "📅  Execution Plan",
        "📈  Analytics"
    ])

    # ===== TAB 1 =====
    with tab1:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            sec_hdr("📊", "Market Insights")
            st.markdown(f'<div class="content-card">{result.get("market","No data available.")}</div>', unsafe_allow_html=True)
        with c2:
            sec_hdr("👥", "Audience Psychology")
            st.markdown(f'<div class="content-card">{result.get("audience","No data available.")}</div>', unsafe_allow_html=True)

    # ===== TAB 2 =====
    with tab2:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            sec_hdr("💡", "Post Ideas")
            ideas = parse_list(content, "post_ideas")
            if ideas:
                for i, idea in enumerate(ideas, 1):
                    st.markdown(f"""
                    <div class="idea-card">
                        <div class="idea-num">Idea {i:02d}</div>
                        <div class="idea-text">{idea}</div>
                    </div>""", unsafe_allow_html=True)
            else:
                st.markdown('<div class="content-card">No post ideas available.</div>', unsafe_allow_html=True)

        with c2:
            sec_hdr("✍️", "Captions")
            caps = parse_list(content, "captions")
            if caps:
                for i, cap in enumerate(caps, 1):
                    st.markdown(f"""
                    <div class="idea-card">
                        <div class="idea-num">Caption {i:02d}</div>
                        <div class="idea-text">{cap}</div>
                    </div>""", unsafe_allow_html=True)
            else:
                st.markdown('<div class="content-card">No captions available.</div>', unsafe_allow_html=True)

        sec_hdr("🎬", "Reel Scripts")
        reels = content.get("reels", []) if isinstance(content, dict) else []
        if not isinstance(reels, list):
            reels = []
        if reels:
            rcols = st.columns(min(len(reels), 3), gap="medium")
            for i, reel in enumerate(reels):
                if isinstance(reel, dict):
                    idea_t = reel.get("idea",   f"Reel {i+1}")
                    script = reel.get("script", "")
                else:
                    idea_t, script = f"Reel {i+1}", str(reel)
                with rcols[i % 3]:
                    st.markdown(f"""
                    <div class="reel-card">
                        <div class="reel-hdr">🎬 &nbsp;{idea_t}</div>
                        <div class="reel-body">{script}</div>
                    </div>""", unsafe_allow_html=True)
        else:
            st.markdown('<div class="content-card">No reel scripts generated.</div>', unsafe_allow_html=True)

        sec_hdr("🏷️", "Hashtags")
        hashtags = parse_list(content, "hashtags")
        if hashtags:
            pills = "".join([
                f'<span class="htag">{h if h.startswith("#") else "#" + h}</span>'
                for h in hashtags
            ])
            st.markdown(f'<div class="hashtag-cloud">{pills}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="content-card">No hashtags available.</div>', unsafe_allow_html=True)


    # ===== TAB 3: EXECUTION =====
    with tab3:
        # ── KEY FIX: extract the last clean JSON block from the strategy string ──
        weekly_plan, ads, tips = get_strategy_lists(result)

        sec_hdr("📅", "Weekly Content Calendar")
        if weekly_plan:
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            day_html = ""
            for i, day_text in enumerate(weekly_plan[:7]):
                # Strip leading day name (e.g. "Monday: ")
                clean = re.sub(
                    r'^(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)[:\s\-]+',
                    '', day_text, flags=re.IGNORECASE
                ).strip()
                day_html += f"""
                <div class="cal-day">
                    <span class="cal-day-name">{days[i]}</span>
                    <div class="cal-day-text">{clean}</div>
                </div>"""
            st.markdown(f'<div class="cal-grid">{day_html}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="content-card">No weekly plan available.</div>', unsafe_allow_html=True)

        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            sec_hdr("📢", "Ad Strategies")
            if ads:
                for ad in ads:
                    st.markdown(f'<div class="ad-card"><span class="ad-card-icon">📣</span><div class="ad-card-text">{ad}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="content-card">No ad strategies available.</div>', unsafe_allow_html=True)
        with c2:
            sec_hdr("🚀", "Growth Tips")
            if tips:
                for tip in tips:
                    st.markdown(f'<div class="tip-card"><span class="tip-icon">💡</span><div class="tip-text">{tip}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="content-card">No growth tips available.</div>', unsafe_allow_html=True)

    # ===== TAB 4 =====
    with tab4:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            sec_hdr("⭐", "Growth Score")
            st.plotly_chart(make_gauge(score, "Overall Growth Potential"), use_container_width=True)
        with c2:
            sec_hdr("👥", "Follower Growth Projection")
            if max_val > 0 or min_val > 0:
                st.plotly_chart(make_bar(["Minimum", "Maximum"], [min_val, max_val], "Monthly Follower Estimate"), use_container_width=True)
            else:
                st.markdown('<div class="content-card">No follower projection available.</div>', unsafe_allow_html=True)

        c3, c4 = st.columns(2, gap="large")
        with c3:
            sec_hdr("⏱️", "Timeline Estimate")
            fig = go.Figure(go.Indicator(
                mode="number", value=time_weeks,
                number={'suffix': " weeks", 'font': {'size': 54, 'color': '#4facfe', 'family': 'Sora'}, 'valueformat': '.0f'},
                title={"text": "Estimated Time to Results", "font": {"size": 14, "color": "#9898b8", "family": "DM Sans"}},
                domain={'x': [0, 1], 'y': [0, 1]}
            ))
            fig.update_layout(height=200, margin=dict(l=20, r=20, t=50, b=10), paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
        with c4:
            sec_hdr("📊", "Performance Summary")
            st.plotly_chart(make_bar(["Quality", "Growth %", "Timeline (wk)"], [q_score, score, time_weeks], "Key Metrics Overview"), use_container_width=True)

        level = growth.get("level", "")
        if level:
            lc = "#4ade80" if "high" in level.lower() else ("#fbbf24" if "medium" in level.lower() else "#f87171")
            st.markdown(f"""
            <div class="level-banner" style="background:linear-gradient(135deg,{lc}18,{lc}08);border:1px solid {lc}30;">
                <h2 style="color:{lc};">🏆 {level}</h2>
                <p>Your predicted growth level based on the current strategy</p>
            </div>""", unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="empty-state">
        <span class="empty-icon">⚡</span>
        <div class="empty-title">Build Your Growth Strategy</div>
        <div class="empty-sub">Configure your business in the sidebar and click Generate to get a full AI-powered marketing plan.</div>
        <span class="empty-cta">← Configure in sidebar</span>
    </div>
    """, unsafe_allow_html=True)