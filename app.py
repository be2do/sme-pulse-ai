import streamlit as st
import pandas as pd
import time

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="SME Pulse AI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. حقن كود الـ CSS المخصص والتنسيقات
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root {
    --bg-deep:    #040810;
    --bg-card:    #0A1120;
    --bg-glass:   rgba(15,25,50,0.7);
    --border:     rgba(56,100,200,0.18);
    --border-glow:rgba(56,180,255,0.35);
    --accent-blue:#3BB4FF;
    --accent-teal:#00E5C8;
    --accent-gold:#FFB347;
    --accent-rose:#FF6B8A;
    --accent-violet:#A78BFA;
    --text-primary:#E8F2FF;
    --text-muted:  #5A7A9A;
    --text-dim:    #2A4A6A;
}

* { box-sizing: border-box; }

html, body, .stApp {
    background: var(--bg-deep) !important;
    font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    color: var(--text-primary) !important;
    direction: rtl;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Grid bg noise ── */
.stApp::before {
    content: '';
    position: fixed; inset: 0; z-index: 0;
    background-image:
        linear-gradient(rgba(59,180,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(59,180,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
}

/* ── Glowing orbs ── */
.stApp::after {
    content: '';
    position: fixed; inset: 0; z-index: 0;
    background:
        radial-gradient(ellipse 600px 400px at 10% 20%, rgba(0,229,200,0.06) 0%, transparent 70%),
        radial-gradient(ellipse 500px 350px at 90% 80%, rgba(59,180,255,0.07) 0%, transparent 70%),
        radial-gradient(ellipse 400px 300px at 50% 50%, rgba(167,139,250,0.04) 0%, transparent 70%);
    pointer-events: none;
}

.main-wrap { position: relative; z-index: 1; }

/* ════════════════════ LOGIN PAGE ════════════════════ */
.login-shell {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
}

.logo-ring {
    width: 90px; height: 90px;
    border-radius: 50%;
    border: 2px solid var(--border-glow);
    display: flex; align-items: center; justify-content: center;
    font-size: 36px;
    background: radial-gradient(circle, rgba(59,180,255,0.1), transparent);
    margin: 0 auto 28px;
    box-shadow: 0 0 40px rgba(59,180,255,0.15), inset 0 0 20px rgba(59,180,255,0.05);
    animation: pulse-ring 3s ease-in-out infinite;
}
@keyframes pulse-ring {
    0%,100% { box-shadow: 0 0 40px rgba(59,180,255,0.15), inset 0 0 20px rgba(59,180,255,0.05); }
    50%      { box-shadow: 0 0 70px rgba(59,180,255,0.30), inset 0 0 30px rgba(59,180,255,0.10); }
}

.brand-name {
    font-family: 'Space Mono', monospace;
    font-size: 48px; font-weight: 700;
    letter-spacing: -1px;
    background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-teal) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-align: center; margin-bottom: 8px;
}
.brand-tagline {
    font-size: 15px; color: var(--text-muted); text-align: center;
    letter-spacing: 0.5px; margin-bottom: 50px; max-width: 400px;
    line-height: 1.7;
}
.stat-strip {
    display: flex; gap: 40px; margin-bottom: 50px; flex-wrap: wrap; justify-content: center;
}
.stat-item { text-align: center; }
.stat-num {
    font-family: 'Space Mono', monospace;
    font-size: 26px; font-weight: 700;
    color: var(--accent-teal);
    display: block;
}
.stat-lbl { font-size: 11px; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase; }
.divider-v { width: 1px; background: var(--border); height: 50px; }

.feature-row {
    display: flex; gap: 16px; margin-bottom: 50px; flex-wrap: wrap; justify-content: center;
}
.feature-pill {
    padding: 8px 18px; border-radius: 30px;
    border: 1px solid var(--border);
    font-size: 13px; color: var(--text-muted);
    background: var(--bg-glass);
    backdrop-filter: blur(8px);
    transition: all 0.3s;
}
.feature-pill:hover { border-color: var(--accent-blue); color: var(--accent-blue); }

/* ════════════════════ STEP BAR ════════════════════ */
.step-bar {
    display: flex; align-items: center; gap: 0;
    justify-content: center;
    padding: 28px 40px 0;
    margin-bottom: 0;
}
.step-node {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 22px;
    font-size: 13px; font-weight: 500;
    color: var(--text-dim);
    position: relative;
}
.step-node.done { color: var(--accent-teal); }
.step-node.active { color: var(--accent-blue); }
.step-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--text-dim); flex-shrink: 0;
}
.step-node.done .step-dot { background: var(--accent-teal); }
.step-node.active .step-dot {
    background: var(--accent-blue);
    box-shadow: 0 0 10px var(--accent-blue);
    animation: blink 1.5s ease-in-out infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.4} }
.step-line { width: 60px; height: 1px; background: var(--border); flex-shrink: 0; }
.step-line.done { background: var(--accent-teal); }

/* ════════════════════ PAGE HEADER ════════════════════ */
.page-header {
    padding: 20px 48px 24px;
    border-bottom: 1px solid var(--border);
    display: flex; justify-content: space-between; align-items: center;
    background: linear-gradient(180deg, rgba(10,17,32,0.8) 0%, transparent 100%);
}
.page-title { font-size: 22px; font-weight: 700; color: var(--text-primary); }
.page-sub   { font-size: 13px; color: var(--text-muted); margin-top: 4px; }
.badge-live {
    font-family: 'Space Mono', monospace;
    font-size: 11px; padding: 5px 14px; border-radius: 20px;
    border: 1px solid rgba(0,229,200,0.3);
    color: var(--accent-teal);
    background: rgba(0,229,200,0.07);
    display: flex; align-items: center; gap: 6px;
}
.dot-live {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--accent-teal); animation: blink 1s infinite;
}

/* ════════════════════ DATA SETUP PAGE ════════════════════ */
.setup-grid { padding: 32px 48px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }

.data-tile {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 28px 28px 20px;
    position: relative; overflow: hidden;
    transition: all 0.35s cubic-bezier(.2,.8,.3,1);
}
.data-tile::before {
    content: ''; position: absolute;
    top: 0; right: 0; left: 0; height: 3px;
    border-radius: 20px 20px 0 0;
    opacity: 0; transition: opacity 0.3s;
}
.data-tile.blue::before  { background: linear-gradient(90deg, transparent, var(--accent-blue)); }
.data-tile.teal::before  { background: linear-gradient(90deg, transparent, var(--accent-teal)); }
.data-tile.gold::before  { background: linear-gradient(90deg, transparent, var(--accent-gold)); }
.data-tile.violet::before{ background: linear-gradient(90deg, transparent, var(--accent-violet)); }

.data-tile:hover { transform: translateY(-3px); border-color: var(--border-glow); }
.data-tile:hover::before { opacity: 1; }

.tile-icon { font-size: 28px; margin-bottom: 14px; }
.tile-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; }
.tile-desc  { font-size: 13px; color: var(--text-muted); line-height: 1.7; margin-bottom: 16px; }
.tile-tag {
    display: inline-block; font-size: 11px;
    padding: 4px 12px; border-radius: 12px;
    color: var(--accent-blue);
    border: 1px solid rgba(59,180,255,0.2);
    background: rgba(59,180,255,0.06);
    font-family: 'Space Mono', monospace;
}

/* ════════════════════ KPI CARDS ════════════════════ */
.kpi-strip { display: grid; grid-template-columns: repeat(4,1fr); gap: 16px; padding: 28px 48px 0; }
.kpi-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 18px; padding: 22px 24px;
    position: relative; overflow: hidden;
    transition: border-color 0.3s;
}
.kpi-card:hover { border-color: var(--border-glow); }
.kpi-accent-bar {
    position: absolute; top: 0; right: 0; left: 0; height: 3px;
    border-radius: 18px 18px 0 0;
}
.kpi-label { font-size: 12px; color: var(--text-muted); margin-bottom: 10px; letter-spacing: 0.3px; }
.kpi-value {
    font-family: 'Space Mono', monospace;
    font-size: 30px; font-weight: 700;
    color: var(--text-primary); line-height: 1;
    margin-bottom: 10px;
}
.kpi-delta { font-size: 12px; display: flex; align-items: center; gap: 6px; }
.kpi-sub { font-size: 11px; color: var(--text-dim); margin-top: 4px; }

/* ════════════════════ INSIGHTS PAGE ════════════════════ */
.insights-body { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 24px; padding: 24px 48px 40px; }

.chat-shell {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 20px; padding: 28px; min-height: 480px;
    display: flex; flex-direction: column; gap: 20px;
}
.chat-header { font-size: 14px; font-weight: 600; color: var(--text-primary); display: flex; align-items: center; gap: 10px; }
.chat-icon { font-size: 20px; }

.quick-chips { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 8px; }
.quick-chip {
    padding: 7px 14px; border-radius: 20px;
    border: 1px solid var(--border);
    font-size: 12px; color: var(--text-muted);
    background: rgba(15,25,50,0.5);
    cursor: pointer; transition: all 0.2s;
}
.quick-chip:hover { border-color: var(--accent-blue); color: var(--accent-blue); }

.ai-response {
    border-radius: 16px; padding: 20px 22px;
    background: rgba(59,180,255,0.04);
    border: 1px solid rgba(59,180,255,0.12);
    font-size: 14px; color: #B0C8E8;
    line-height: 1.8; animation: fadeUp 0.4s ease;
}
@keyframes fadeUp { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }

.ai-header {
    font-size: 13px; font-weight: 700;
    margin-bottom: 14px; display: flex; align-items: center; gap: 8px;
}
.ai-tag {
    font-family: 'Space Mono', monospace;
    font-size: 10px; padding: 3px 10px; border-radius: 10px;
    background: rgba(59,180,255,0.1); color: var(--accent-blue);
    border: 1px solid rgba(59,180,255,0.2);
}
.insight-row { display: flex; gap: 10px; margin: 8px 0; align-items: flex-start; }
.insight-dot { font-size: 16px; flex-shrink: 0; margin-top: 2px; }

.viz-shell {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 20px; padding: 28px;
    display: flex; flex-direction: column; gap: 20px;
}
.viz-header { font-size: 14px; font-weight: 600; color: var(--text-primary); }

.mini-kpis { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.mini-kpi {
    background: rgba(255,255,255,0.02); border: 1px solid var(--border);
    border-radius: 14px; padding: 16px;
}
.mini-kpi-label { font-size: 11px; color: var(--text-muted); margin-bottom: 6px; }
.mini-kpi-value { font-family: 'Space Mono', monospace; font-size: 20px; font-weight: 700; }

.compliance-bar-shell { margin-top: 4px; }
.compliance-label { display: flex; justify-content: space-between; font-size: 12px; color: var(--text-muted); margin-bottom: 6px; }
.compliance-track {
    height: 6px; border-radius: 10px; background: rgba(255,255,255,0.05);
    overflow: hidden; margin-bottom: 12px;
}
.compliance-fill { height: 100%; border-radius: 10px; }

/* ── STREAMLIT OVERRIDES ── */
.stButton > button {
    background: linear-gradient(135deg, #1A3A6A 0%, #0F2040 100%) !important;
    color: var(--accent-blue) !important;
    border: 1px solid rgba(59,180,255,0.3) !important;
    border-radius: 12px !important;
    font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    font-size: 14px !important; font-weight: 600 !important;
    padding: 12px 24px !important;
    transition: all 0.3s !important;
    box-shadow: 0 4px 20px rgba(59,180,255,0.08) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #1E4A8A 0%, #152A5A 100%) !important;
    border-color: var(--accent-blue) !important;
    box-shadow: 0 4px 30px rgba(59,180,255,0.2) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px dashed rgba(59,180,255,0.25) !important;
    border-radius: 14px !important; padding: 16px !important;
}
.stTextInput > div > input {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    padding: 14px 16px !important;
    font-size: 14px !important;
}
.stTextInput > div > input:focus {
    border-color: var(--accent-blue) !important;
    box-shadow: 0 0 0 3px rgba(59,180,255,0.1) !important;
}
.stTabs [role="tablist"] {
    background: var(--bg-card) !important;
    border-radius: 14px !important; padding: 6px !important;
    gap: 4px !important; border: 1px solid var(--border) !important;
}
.stTabs [role="tab"] {
    background: transparent !important; border-radius: 10px !important;
    color: var(--text-muted) !important; font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    font-size: 14px !important; padding: 10px 20px !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(59,180,255,0.12) !important;
    color: var(--accent-blue) !important;
}
.stSuccess > div {
    background: rgba(0,229,200,0.07) !important;
    border: 1px solid rgba(0,229,200,0.25) !important;
    border-radius: 12px !important; color: var(--accent-teal) !important;
}
.stInfo > div {
    background: rgba(59,180,255,0.07) !important;
    border: 1px solid rgba(59,180,255,0.2) !important;
    border-radius: 12px !important; color: var(--accent-blue) !important;
}
[data-testid="stMetric"] {
    background: transparent !important;
}
div[data-testid="stSpinner"] { color: var(--accent-blue) !important; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الجلسة والتنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'login'

st.markdown("<div class='main-wrap'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# 1. شاشة تسجيل الدخول (LOGIN)
# ══════════════════════════════════════════════
if st.session_state.page == 'login':
    st.markdown("""
    <div class='login-shell'>
        <div class='logo-ring'>◈</div>
        <div class='brand-name'>SME Pulse AI</div>
        <div class='brand-tagline'>
            منصة الذكاء المالي للمنشآت الصغيرة والمتوسطة<br>
            أتمتة الفواتير · تحليل التدفق النقدي · الامتثال الضريبي
        </div>
        <div class='stat-strip'>
            <div class='stat-item'>
                <span class='stat-num'>2,400+</span>
                <span class='stat-lbl'>منشأة نشطة</span>
            </div>
            <div class='divider-v'></div>
            <div class='stat-item'>
                <span class='stat-num'>SAR 1.2B</span>
                <span class='stat-lbl'>فواتير مُعالجة</span>
            </div>
            <div class='divider-v'></div>
            <div class='stat-item'>
                <span class='stat-num'>99.3%</span>
                <span class='stat-lbl'>دقة OCR</span>
            </div>
            <div class='divider-v'></div>
            <div class='stat-item'>
                <span class='stat-num'>ZATCA</span>
                <span class='stat-lbl'>متوافق بالكامل</span>
            </div>
        </div>
        <div class='feature-row'>
            <div class='feature-pill'>⚡ Burn Rate Analysis</div>
            <div class='feature-pill'>📊 Runway Forecast</div>
            <div class='feature-pill'>🔗 Open Banking API</div>
            <div class='feature-pill'>🧾 Smart OCR Invoice</div>
            <div class='feature-pill'>📈 LTV : CAC Ratio</div>
            <div class='feature-pill'>🛡️ ZATCA Compliance</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        if st.button("الدخول إلى النظام  ⟶", use_container_width=True):
            st.session_state.page = 'data_setup'
            st.rerun()

    st.markdown("""
    <div style='text-align:center; margin-top:20px; font-size:12px; color:#2A4A6A; font-family:"Space Mono",monospace;'>
        v2.4.1 · Najran Region · Powered by Claude AI
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# 2. شاشة إعداد البيانات (DATA SETUP)
# ══════════════════════════════════════════════
elif st.session_state.page == 'data_setup':
    st.markdown("""
    <div class='step-bar'>
        <div class='step-node done'><span class='step-dot'></span>تسجيل الدخول</div>
        <div class='step-line done'></div>
        <div class='step-node active'><span class='step-dot'></span>إعداد البيانات</div>
        <div class='step-line'></div>
        <div class='step-node'><span class='step-dot'></span>لوحة القيادة</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-header'>
        <div>
            <div class='page-title'>إعداد البيانات المالية</div>
            <div class='page-sub'>ربط مصادر البيانات · رفع الفواتير · هندسة التدفقات النقدية</div>
        </div>
        <div class='badge-live'><span class='dot-live'></span>OCR Engine نشط</div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["  🗂  تحصيل البيانات  ", "  ⚙️  حوكمة وتصنيف تلقائي  "])

    with tab1:
        st.markdown("""
        <div class='setup-grid'>
            <div class='data-tile blue'>
                <div class='tile-icon'>🧾</div>
                <div class='tile-title'>الفاتورة الذكية — OCR</div>
                <div class='tile-desc'>رفع الفاتورة الورقية أو الإلكترونية (صورة أو PDF) ليقرأها الذكاء الاصطناعي ويستخرج المبالغ والبنود والمورد والتاريخ تلقائياً، ثم يصنفها في الهيكل المحاسبي المعتمد.</div>
                <span class='tile-tag'>OCR · NLP · Auto-Classify</span>
            </div>
            <div class='data-tile teal'>
                <div class='tile-icon'>🏦</div>
                <div class='tile-title'>Open Banking — ربط مباشر</div>
                <div class='tile-desc'>ربط حساب المنشأة ببنوك الراجحي، الأهلي، وبوابات الدفع (زد · سلة · تابي · مدى) عبر Open Banking API لتحديث التدفق النقدي والـ Runway لحظياً.</div>
                <span class='tile-tag'>Open Banking API · Real-time</span>
            </div>
            <div class='data-tile gold'>
                <div class='tile-icon'>📂</div>
                <div class='tile-title'>كشف الحساب التاريخي</div>
                <div class='tile-desc'>رفع كشف الحساب بصيغة PDF لحساب معدل الحرق النقدي (Burn Rate)، وهندسة التدفق النقدي التاريخي، ورسم منحنى الـ Runway المتوقع خلال 12 شهراً.</div>
                <span class='tile-tag'>Burn Rate · Runway · Cash Flow</span>
            </div>
            <div class='data-tile violet'>
                <div class='tile-icon'>✍️</div>
                <div class='tile-title'>الإدخال اليدوي — عمليات نقدية</div>
                <div class='tile-desc'>إضافة المصاريف النقدية (كاش) أو المبالغ الاستثنائية غير الموثقة رقمياً، وجدولتها كتكاليف ثابتة أو متغيرة لحسابات Break-even الدقيقة.</div>
                <span class='tile-tag'>COGS · OpEx · CapEx</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("<div style='padding: 0 48px 0 24px;'>", unsafe_allow_html=True)
            invoice_file = st.file_uploader(
                "ارفع الفاتورة (صورة أو PDF):",
                type=["png", "jpg", "jpeg", "pdf"], key="ocr_up"
            )
            if invoice_file:
                st.success("✅ تم استلام الفاتورة — بدأ محرك OCR بالاستخراج")
            statement_file = st.file_uploader(
                "ارفع كشف الحساب البنكي:",
                type=["pdf"], key="pdf_up"
            )
            if statement_file:
                st.success("✅ تم الرفع — جاري هندسة الـ Burn Rate والـ Runway")
            st.markdown("</div>", unsafe_allow_html=True)

        with col_b:
            st.markdown("<div style='padding: 0 24px 0 48px;'>", unsafe_allow_html=True)
            if st.button("🔗  ابدأ ربط الحساب البنكي (Open Banking)", use_container_width=True):
                st.info("⚡ جاري فتح بوابة الربط الآمنة — معتمد من ساما وهيئة الاتصالات")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("✍️  فتح لوحة الإدخال اليدوي للعمليات النقدية", use_container_width=True):
                st.info("📋 ستُضاف البيانات اليدوية ضمن تصنيف COGS / OpEx تلقائياً")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class='data-tile teal' style='margin: 0 48px 0 24px;'>
                <div class='tile-icon'>🤖</div>
                <div class='tile-title'>التصنيف المحاسبي التلقائي</div>
                <div class='tile-desc'>
                    يقوم النظام بتصنيف كل فاتورة وعملية مالية وفق دليل الحسابات السعودي المعتمد:<br><br>
                    <b style='color:#00E5C8'>• التكاليف الثابتة (Fixed Costs):</b> الإيجار، الرواتب، التراخيص<br>
                    <b style='color:#00E5C8'>• تكلفة البضاعة المباعة (COGS):</b> المواد الخام، التصنيع<br>
                    <b style='color:#00E5C8'>• المصاريف التشغيلية (OpEx):</b> التسويق، الاشتراكات، الخدمات<br>
                    <b style='color:#00E5C8'>• رأس المال الاستثماري (CapEx):</b> الأصول الثابتة، التجهيزات
                </div>
                <span class='tile-tag'>GAAP · IFRS · Saudi Accounting</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class='data-tile blue' style='margin: 0 24px 0 48px;'>
                <div class='tile-icon'>🛡️</div>
                <div class='tile-title'>امتثال ZATCA والفوترة الإلكترونية</div>
                <div class='tile-desc'>
                    التحقق الآلي من متمتطلبات هيئة الزكاة والضريبة والجمارك:<br><br>
                    <b style='color:#3BB4FF'>• الفاتورة الإلكترونية (e-Invoice):</b> توليد وتوقيع رقمي<br>
                    <b style='color:#3BB4FF'>• ضريبة القيمة المضافة (VAT 15%):</b> حساب وإقرار آلي<br>
                    <b style='color:#3BB4FF'>• تقارير الزكاة الربعية:</b> تجميع وإعداد تلقائي<br>
                    <b style='color:#3BB4FF'>• رمز QR للفاتورة:</b> توليد فوري بمعايير ZATCA
                </div>
                <span class='tile-tag'>ZATCA · e-Invoice · VAT · Zakat</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        if st.button("انتقل للوحة القيادة الاستثمارية  ⟶", use_container_width=True):
            st.session_state.page = 'insights'
            st.rerun()

# ══════════════════════════════════════════════
# 3. لوحة القيادة والمستشار الذكي (INSIGHTS)
# ══════════════════════════════════════════════
elif st.session_state.page == 'insights':
    st.markdown("""
    <div class='step-bar'>
        <div class='step-node done'><span class='step-dot'></span>تسجيل الدخول</div>
        <div class='step-line done'></div>
        <div class='step-node done'><span class='step-dot'></span>إعداد البيانات</div>
        <div class='step-line done'></div>
        <div class='step-node active'><span class='step-dot'></span>لوحة القيادة الاستثمارية</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-header'>
        <div>
            <div class='page-title'>لوحة القيادة المالية — Startup KPIs</div>
            <div class='page-sub'>Runway · Burn Rate · Gross Margin · CAC · LTV · Break-even · ZATCA Compliance</div>
        </div>
        <div class='badge-live'><span class='dot-live'></span>Live Data</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='kpi-strip'>
        <div class='kpi-card'>
            <div class='kpi-accent-bar' style='background:linear-gradient(90deg,var(--accent-teal),#00B89C)'></div>
            <div class='kpi-label'>فترة نفاذ السيولة • Runway</div>
            <div class='kpi-value'>14.2<span style='font-size:16px;color:var(--text-muted)'> شهر</span></div>
            <div class='kpi-delta' style='color:var(--accent-teal)'>🟢 نطاق آمن — فوق 12 شهر</div>
            <div class='kpi-sub'>Cash Available ÷ Net Burn Rate</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-accent-bar' style='background:linear-gradient(90deg,var(--accent-rose),#E84A6A)'></div>
            <div class='kpi-label'>معدل الحرق الشهري • Burn Rate</div>
            <div class='kpi-value'>8,400<span style='font-size:16px;color:var(--text-muted)'> SAR</span></div>
            <div class='kpi-delta' style='color:var(--accent-teal)'>📉 انخفض 6.2% عن الشهر الماضي</div>
            <div class='kpi-sub'>Gross Burn — Net Revenue = Net Burn</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-accent-bar' style='background:linear-gradient(90deg,var(--accent-blue),#1A8AFF)'></div>
            <div class='kpi-label'>الهامش الإجمالي • Gross Margin</div>
            <div class='kpi-value'>72<span style='font-size:16px;color:var(--text-muted)'>%</span></div>
            <div class='kpi-delta' style='color:var(--accent-blue)'>🌱 أداء تشغيلي ممتاز — هدف 78%</div>
            <div class='kpi-sub'>(Revenue − COGS) ÷ Revenue</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-accent-bar' style='background:linear-gradient(90deg,var(--accent-gold),#E09030)'></div>
            <div class='kpi-label'>جاهزية الامتثال • ZATCA & VAT</div>
            <div class='kpi-value'>95<span style='font-size:16px;color:var(--text-muted)'>%</span></div>
            <div class='kpi-delta' style='color:var(--accent-gold)'>⚡ 2 بنود تحتاج مراجعة</div>
            <div class='kpi-sub'>e-Invoice · VAT · Zakat Compliance</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='insights-body'>", unsafe_allow_html=True)
    col_chat, col_viz = st.columns([1.1, 0.9])

    with col_chat:
        st.markdown("""
        <div class='chat-shell'>
            <div class='chat-header'>
                <span class='chat-icon'>🤖</span>
                المستشار المالي الذكي — AI CFO
                <span style='margin-right:auto;font-size:11px;font-family:"Space Mono",monospace;color:var(--text-dim)'>GPT-4o Powered</span>
            </div>
            <div class='quick-chips'>
                <div class='quick-chip'>كيف أحسن الـ Runway؟</div>
                <div class='quick-chip'>اشرح الـ Burn Rate</div>
                <div class='quick-chip'>نسبة LTV:CAC</div>
                <div class='quick-chip'>متى نقطة التعادل؟</div>
                <div class='quick-chip'>جاهزية ZATCA</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        user_query = st.text_input(
            "", placeholder="اكتب سؤالك المالي... (مثال: كيف أحسّن الـ Gross Margin؟)",
            key="chat_input", label_visibility="collapsed"
        )

        KEYWORDS = {
            "burn": ["burn rate", "حرق", "معدل الحرق", "gross burn", "net burn", "monthly burn"],
            "runway": ["runway", "نفاذ", "سيولة", "كاش", "cash runway", "فترة النفاذ"],
            "margin": ["margin", "هامش", "استهلاك", "مصاريف", "تكاليف", "gross margin", "opex", "cogs"],
            "cac_ltv": ["cac", "ltv", "عميل", "استحواذ", "تسويق", "customer acquisition"],
            "breakeven": ["تعادل", "break-even", "breakeven", "نقطة التعادل", "fixed cost"],
            "zatca": ["zatca", "ضريبة", "vat", "زكاة", "فاتورة إلكترونية", "e-invoice", "امتثال"],
            "funding": ["تمويل", "قرض", "استثمار", "جولة", "seed", "series", "vc", "مستثمر"],
        }

        def detect(q):
            q_low = q.lower()
            for key, words in KEYWORDS.items():
                if any(w in q_low for w in words):
                    return key
            return "default"

        RESPONSES = {
            "burn": {
                "color": "#FF6B8A", "title": "تحليل معدل الحرق النقدي — Burn Rate Breakdown",
                "tag": "Burn Rate · Cash Flow · OpEx",
                "body": """
                <div class='insight-row'><span class='insight-dot'>🔥</span><div><b>Gross Burn Rate:</b> 18,200 SAR شهرياً — إجمالي المصاريف التشغيلية قبل الإيرادات.</div></div>
                <div class='insight-row'><span class='insight-dot'>💚</span><div><b>Net Burn Rate:</b> 8,400 SAR — بعد خصم الإيرادات الشهرية (9,800 SAR). هذا هو الرقم الحقيقي الذي يستهلك الكاش.</div></div>
                <div class='insight-row'><span class='insight-dot'>⚡</span><div><b>فرصة تخفيض فورية:</b> رصد النظام 3 اشتراكات SaaS غير نشطة بـ 1,200 SAR/شهر. إلغاؤها يخفض الـ Net Burn إلى <b style='color:#00E5C8'>7,200 SAR</b> ويمدد الـ Runway 1.7 شهر إضافي.</div></div>
                <div class='insight-row'><span class='insight-dot'>📊</span><div><b>Burn Multiple:</b> 1.86 — كل ريال مصروف يولد 0.54 ريال إيراد. الهدف الصحي للشركات الناشئة هو ≤ 1.5.</div></div>
                """
            },
            "runway": {
                "color": "#00E5C8", "title": "تحليل فترة النفاذ — Runway Forecast",
                "tag": "Runway · Liquidity · Cash Position",
                "body": """
                <div class='insight-row'><span class='insight-dot'>🟢</span><div><b>Runway الحالي:</b> 14.2 شهر بناءً على الكاش المتوفر (119,280 SAR) ÷ Net Burn Rate (8,400 SAR/شهر).</div></div>
                <div class='insight-row'><span class='insight-dot'>⚠️</span><div><b>سيناريو CapEx:</b> إذا اشتريت أصولاً بـ 15,000 SAR نقداً، ينخفض الـ Runway فوراً إلى <b style='color:#FFB347'>12.4 شهر</b>. التوصية: استخدم تمويل الأصول أو BNPL.</div></div>
                <div class='insight-row'><span class='insight-dot'>🚀</span><div><b>سيناريو النمو:</b> إذا نما MRR بـ 12% شهرياً، يمتد الـ Runway إلى <b style='color:#00E5C8'>19.8 شهر</b> — وضع استثماري ممتاز.</div></div>
                <div class='insight-row'><span class='insight-dot'>💡</span><div><b>Default Rate (نقطة التحذير):</b> عند وصول الـ Runway لأقل من 6 أشهر، يرفع النظام إنذاراً تلقائياً لبدء جولة تمويلية.</div></div>
                """
            },
            "margin": {
                "color": "#3BB4FF", "title": "تحسين الهامش الإجمالي — Gross Margin Optimization",
                "tag": "Gross Margin · COGS · OpEx · Unit Economics",
                "body": """
                <div class='insight-row'><span class='insight-dot'>📈</span><div><b>الهامش الحالي:</b> 72% — جيد، والهدف الاستراتيجي هو <b style='color:#3BB4FF'>78%</b> خلال 3 أشهر.</div></div>
                <div class='insight-row'><span class='insight-dot'>⚡</span><div><b>تحسين COGS:</b> الشراء الجزئي من الموردين يرفع تكاليف البضاعة (COGS) 11%. التحول للطلب الموحد أول كل شهر يوفر ~900 SAR.</div></div>
                <div class='insight-row'><span class='insight-dot'>🔧</span><div><b>ترشيد OpEx:</b> اشتراكات SaaS معلقة (1,200 SAR) + رسوم معالجة مدفوعات مرتفعة (340 SAR). الإجمالي: <b style='color:#00E5C8'>1,540 SAR/شهر يمكن توفيرها.</b></div></div>
                <div class='insight-row'><span class='insight-dot'>📊</span><div><b>تأثير الـ Unit Economics:</b> رفع الهامش لـ 78% يعني زيادة صافي الـ LTV من 180 SAR إلى 216 SAR لكل عميل.</div></div>
                """
            },
            "cac_ltv": {
                "color": "#A78BFA", "title": "كفاءة الاستحواذ على العملاء — CAC & LTV Analysis",
                "tag": "CAC · LTV · Payback Period · Unit Economics",
                "body": """
                <div class='insight-row'><span class='insight-dot'>🎯</span><div><b>تكلفة استحواذ العميل (CAC):</b> 45 SAR — محسوبة من إجمالي إنفاق التسويق ÷ عدد العملاء الجدد.</div></div>
                <div class='insight-row'><span class='insight-dot'>💎</span><div><b>القيمة الحيوية للعميل (LTV):</b> 180 SAR — متوسط الإيراد المستدام طوال دورة حياة العميل.</div></div>
                <div class='insight-row'><span class='insight-dot'>🏆</span><div><b>نسبة LTV:CAC = 4:1</b> — ممتازة جداً. المعدل الصحي عالمياً هو 3:1. هذا الرقم جاذب للمستثمرين في جولات Seed وSeries A.</div></div>
                <div class='insight-row'><span class='insight-dot'>⏱️</span><div><b>Payback Period:</b> 3.2 شهر لاسترداد تكلفة الاستحواذ — ممتاز. أقل من 6 أشهر يُعتبر معياراً مثالياً للشركات الناشئة.</div></div>
                """
            },
            "breakeven": {
                "color": "#FFB347", "title": "تحليل نقطة التعادل — Break-even Analysis",
                "tag": "Break-even · Fixed Cost · Variable Cost · Contribution Margin",
                "body": """
                <div class='insight-row'><span class='insight-dot'>⚖️</span><div><b>نقطة التعادل الشهرية:</b> 32,000 SAR مبيعات — عندها تغطي الإيرادات كامل التكاليف الثابتة والمتغيرة.</div></div>
                <div class='insight-row'><span class='insight-dot'>📌</span><div><b>هيكل التكاليف:</b> ثابتة (Fixed): 14,200 SAR · متغيرة (Variable): 18% من كل ريال مبيعات.</div></div>
                <div class='insight-row'><span class='insight-dot'>📈</span><div><b>Contribution Margin:</b> 82% — من كل ريال إيراد، 0.82 ريال يذهب لتغطية التكاليف الثابتة والربح.</div></div>
                <div class='insight-row'><span class='insight-dot'>🎯</span><div><b>المبيعات الحالية:</b> 24,800 SAR/شهر — الفجوة للتعادل <b style='color:#FFB347'>7,200 SAR</b>. بمعدل النمو الحالي (12%)، ستصل في شهرين.</div></div>
                """
            },
            "zatca": {
                "color": "#FFB347", "title": "جاهزية الامتثال الضريبي — ZATCA Compliance",
                "tag": "ZATCA · e-Invoice · VAT · Zakat · QR Code",
                "body": """
                <div class='insight-row'><span class='insight-dot'>✅</span><div><b>الفوترة الإلكترونية (e-Invoice):</b> مكتملة 100% — توليد وتوقيع رقمي وإرسال تلقائي لـ ZATCA.</div></div>
                <div class='insight-row'><span class='insight-dot'>✅</span><div><b>ضريبة القيمة المضافة VAT (15%):</b> حساب وتحصيل وإقرار آلي — آخر إقرار مقدم في الموعد.</div></div>
                <div class='insight-row'><span class='insight-dot'>⚠️</span><div><b>تحذير — فاتورتان بدون QR Code:</b> فاتورة رقم 1042 و1089 تحتاجان توليد رمز QR المعتمد فوراً لتجنب الغرامة.</div></div>
                <div class='insight-row'><span class='insight-dot'>📋</span><div><b>إقرار الزكاة الربعي:</b> موعد الإقرار القادم خلال 22 يوماً — البيانات المجمعة جاهزة 95%.</div></div>
                """
            },
            "funding": {
                "color": "#00E5C8", "title": "الجاهزية الاستثمارية — Funding Readiness",
                "tag": "Seed · Series A · MRR · ARR · Investor Metrics",
                "body": """
                <div class='insight-row'><span class='insight-dot'>💰</span><div><b>الجدارة الائتمانية:</b> نمو التدفق النقدي الحر 12% شهرياً يؤهلك لجولة Seed بحد أقصى 500,000 SAR.</div></div>
                <div class='insight-row'><span class='insight-dot'>📊</span><div><b>مقاييس المستثمر (Investor Metrics):</b> MRR: 9,800 SAR · ARR: 117,600 SAR · LTV:CAC: 4:1 · Gross Margin: 72%.</div></div>
                <div class='insight-row'><span class='insight-dot'>🏦</span><div><b>تمويل إسلامي (مرابحة):</b> جدارتك الائتمانية تؤهلك للحصول على تمويل نمو 75,000 SAR عبر شركاء المنصة بأقل نسبة مرابحة.</div></div>
                <div class='insight-row'><span class='insight-dot'>📋</span><div><b>ما ينقص الـ Data Room:</b> تقرير التدفق النقدي لـ 12 شهر (جاهز) · كشف الأرباح والخسائر (جاهز) · خطة النمو لـ 18 شهر (تحتاج تحديث).</div></div>
                """
            },
            "default": {
                "color": "#5A7A9A", "title": "مرحباً بك في غرفة الحوكمة المالية — AI CFO",
                "tag": "SME Pulse AI · Startup Finance",
                "body": """
                <div class='insight-row'><span class='insight-dot'>🔥</span><div><b>Burn Rate & Runway:</b> اسألني عن معدل الحرق النقدي وكم تبقى للشركة من عمر مالي.</div></div>
                <div class='insight-row'><span class='insight-dot'>📈</span><div><b>Gross Margin & COGS:</b> تحليل الهامش الإجمالي وتكاليف البضاعة وفرص الترشيد.</div></div>
                <div class='insight-row'><span class='insight-dot'>🎯</span><div><b>CAC · LTV · Payback Period:</b> كفاءة الإنفاق التسويقي وجدوى كل عميل جديد.</div></div>
                <div class='insight-row'><span class='insight-dot'>⚖️</span><div><b>Break-even Analysis:</b> متى تصل لنقطة التعادل ورحلة الربحية.</div></div>
                <div class='insight-row'><span class='insight-dot'>🛡️</span><div><b>ZATCA & VAT Compliance:</b> جاهزية الامتثال الضريبي والفوترة الإلكترونية.</div></div>
                <div class='insight-row'><span class='insight-dot'>💰</span><div><b>Funding Readiness:</b> مؤشراتك أمام المستثمرين وجولات التمويل.</div></div>
                """
            }
        }

        if user_query:
            with st.spinner("يحلل النظام بياناتك المالية..."):
                time.sleep(0.8)
            rtype = detect(user_query)
            r = RESPONSES[rtype]
            st.markdown(f"""
            <div class='ai-response' style='border-color:rgba({",".join(str(int(r["color"].lstrip("#")[i:i+2],16)) for i in (0,2,4))},0.25);'>
                <div class='ai-header' style='color:{r["color"]}'>
                    🤖 {r["title"]}
                    <span class='ai-tag'>{r["tag"]}</span>
                </div>
                {r["body"]}
            </div>
            """, unsafe_allow_html=True)

    with col_viz:
        st.markdown("""
        <div class='viz-shell'>
            <div class='viz-header'>📈 التدفق النقدي والـ Runway المتوقع</div>
        </div>
        """, unsafe_allow_html=True)

        chart_data = pd.DataFrame({
            'الشهر': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو (متوقع)', 'يوليو (متوقع)'],
            'السيولة المتراكمة (SAR)': [82000, 92000, 88000, 103000, 119280, 130000, 143500],
            'هدف الـ Runway (SAR)': [80000, 85000, 90000, 95000, 100000, 105000, 110000],
        })
        st.line_chart(chart_data.set_index('الشهر'))

        st.markdown("""
        <div style='margin-top: 8px;'>
            <div class='viz-header' style='margin-bottom:12px;'>⚡ مؤشرات Unit Economics</div>
            <div class='mini-kpis'>
                <div class='mini-kpi'>
                    <div class='mini-kpi-label'>CAC — تكلفة الاستحواذ</div>
                    <div class='mini-kpi-value' style='color:var(--accent-violet)'>45 SAR</div>
                </div>
                <div class='mini-kpi'>
                    <div class='mini-kpi-label'>LTV — القيمة الحيوية</div>
                    <div class='mini-kpi-value' style='color:var(--accent-teal)'>180 SAR</div>
                </div>
                <div class='mini-kpi'>
                    <div class='mini-kpi-label'>LTV:CAC Ratio</div>
                    <div class='mini-kpi-value' style='color:var(--accent-blue)'>4:1</div>
                </div>
                <div class='mini-kpi'>
                    <div class='mini-kpi-label'>Payback Period</div>
                    <div class='mini-kpi-value' style='color:var(--accent-gold)'>3.2 mo</div>
                </div>
            </div>
            <br>
            <div class='compliance-bar-shell'>
                <div class='viz-header' style='margin-bottom:12px;'>🛡️ الامتثال والجاهزية</div>
                <div class='compliance-label'><span>ZATCA e-Invoice</span><span style='color:var(--accent-teal)'>100%</span></div>
                <div class='compliance-track'><div class='compliance-fill' style='width:100%;background:var(--accent-teal)'></div></div>
                <div class='compliance-label'><span>VAT Reporting</span><span style='color:var(--accent-blue)'>100%</span></div>
                <div class='compliance-track'><div class='compliance-fill' style='width:100%;background:var(--accent-blue)'></div></div>
                <div class='compliance-label'><span>Zakat Return</span><span style='color:var(--accent-gold)'>72%</span></div>
                <div class='compliance-track'><div class='compliance-fill' style='width:72%;background:var(--accent-gold)'></div></div>
                <div class='compliance-label'><span>QR Code Coverage</span><span style='color:var(--accent-rose)'>91%</span></div>
                <div class='compliance-track'><div class='compliance-fill' style='width:91%;background:var(--accent-rose)'></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        if st.button("🔄 العودة للرئيسية", use_container_width=True):
            st.session_state.page = 'login'
            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
