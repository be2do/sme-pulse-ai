import streamlit as st
import pandas as pd
import time

# 1. إعدادات الصفحة بثيم داكن فخم ومتناسق
st.set_page_config(
    page_title="SME Pulse AI - System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. هندسة الـ CSS لتحسين التصميم وجعله مطابقاً للـ UI/UX الاحترافي
st.markdown("""
    <style>
    .stApp {
        background-color: #0B111E;
        color: #F8FAFC;
    }
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: 1px;
        background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-size: 16px;
        color: #94A3B8;
        margin-bottom: 30px;
    }
    .data-card {
        background-color: #151F32;
        border: 1px solid #22334F;
        border-radius: 16px;
        padding: 25px;
        text-align: right;
        transition: all 0.3s ease;
        cursor: pointer;
        min-height: 140px;
    }
    .data-card:hover {
        border-color: #3B82F6;
        transform: translateY(-2px);
    }
    .card-title {
        font-size: 18px;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 8px;
    }
    .card-desc {
        font-size: 13px;
        color: #64748B;
        line-height: 1.5;
    }
    .step-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 20px 0 40px 0;
    }
    .step-badge {
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
        background-color: #151F32;
        color: #64748B;
        border: 1px solid #22334F;
    }
    .step-badge.active {
        background-color: #1E3A8A;
        color: #3B82F6;
        border-color: #3B82F6;
    }
    .ai-box {
        background-color: #151F32; 
        padding: 20px; 
        border-radius: 12px; 
        line-height: 1.6;
        font-size: 14px;
        color: #E2E8F0;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة التطبيق (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# ==========================================
# 🛑 الشاشة الأولى: صفحة اضغط للدخول (Login)
# ==========================================
if st.session_state.page == 'login':
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='main-title'>SME Pulse AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>المستشار المالي الذكي وأتمتة الفواتير للمنشآت الصغيرة والمتوسطة والشركات الناشئة</div>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        if st.button("اضغط للدخول إلى النظام ➔", use_container_width=True, type="primary"):
            st.session_state.page = 'data_setup'
            st.rerun()
            
    st.markdown("""
    <div class='step-container'>
        <div class='step-badge active'>➔ Login</div>
        <div class='step-badge'>Data Setup</div>
        <div class='step-badge'>Insights</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 🛠️ الشاشة الثانية: تحصيل البيانات (Data Setup)
# ==========================================
elif st.session_state.page == 'data_setup':
    st.markdown("<div class='main-title' style='font-size: 32px;'>SME Pulse AI نظام</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='step-container'>
        <div class='step-badge'>Login ✓</div>
        <div class='step-badge active'>➔ Data Setup (Step 1 of 4)</div>
        <div class='step-badge'>Insights</div>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📋 تحصيل البيانات", "🤖 تهيئة وحوكمة البيانات"])
    
    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)
        
        with row1_col2:
            st.markdown("<div class='data-card'><div class='card-title'>📄 ارفع الفاتورة الذكية (OCR)</div><div class='card-desc'>ارفع الفاتورة المستلمة أو المصروفة بتقنية الذكاء الاصطناعي لتقرأ وتصنف قيمتها وبنودها آلياً دون أي كتابة يدوية.</div></div>", unsafe_allow_html=True)
            invoice_file = st.file_uploader("اختر ملف الفاتورة أو صورتها هنا:", type=["png", "jpg", "jpeg", "pdf"], key="ocr_upload")
            if invoice_file: st.success("✅ تم استلام الفاتورة وربطها بالهيكل المالي!")
                
        with row1_col1:
            st.markdown("<div class='data-card'><div class='card-title'>🏦 ربط الحساب البنكي وبوابات الدفع</div><div class='card-desc'>ربط حساب المنشأة البنكي وبوابات الدفع (مثل زد، سلة، أو تابي) عبر واجهات الـ API لتحديث التدفقات النقدية والـ Runway فوراً.</div></div>", unsafe_allow_html=True)
            if st.button("🔗 ابدأ الربط البنكي الآمن", use_container_width=True): st.info("جاري فتح بوابة الربط البنكي المعتمدة المفتوحة...")

        with row2_col2:
            st.markdown("<div class='data-card'><div class='card-title'>📝 ادخل البيانات يدوياً</div><div class='card-desc'>إذا كان لديك بنود استثنائية أو مصروفات نقدية مباشرة (كاش)، يمكنك تعبئة تفاصيلها وجدولتها هنا يدوياً.</div></div>", unsafe_allow_html=True)
            if st.button("✍️ فتح جدول الإدخال اليدوي", use_container_width=True): st.toggle("تفعيل لوحة السجلات اليدوية")

        with row2_col1:
            st.markdown("<div class='data-card'><div class='card-title'>📂 ارفع كشف الحساب والبيانات التاريخية</div><div class='card-desc'>ارفع كشف الحساب البنكي التاريخي بصيغة PDF ليقوم النظام بهندسة البيانات، وحساب معدل الحرق النقدّي (Burn Rate).</div></div>", unsafe_allow_html=True)
            statement_file = st.file_uploader("ارفع كشف حساب المنشأة التجاري:", type=["pdf"], key="pdf_upload")
            if statement_file: st.success("✅ تم رفع الكشف بنجاح، جاري هندسة التدفق النقدي!")

    with tab2:
        st.write("---")
        st.info("💡 قسم الأتمتة: بمجرد اختيار وتجهيز البيانات من التبويب الأول، ستقوم محركات الـ AI بحوكمة وتصنيف العمليات طبقاً لأدلة المحاسبة السعودية للهيئات والمنشآت.")

    st.write("---")
    cc1, cc2, cc3 = st.columns([1, 0.5, 1])
    with cc2:
        if st.button("انتقل إلى لوحة التحليلات الذكية ➔", type="secondary", use_container_width=True):
            st.session_state.page = 'insights'
            st.rerun()

# ==========================================
# 📊 الشاشة الثالثة: التحليلات والـ Chatbot (Insights)
# ==========================================
elif st.session_state.page == 'insights':
    st.markdown("<div class='main-title' style='font-size: 32px;'>SME Pulse AI - لوحة القيادة الاستثمارية</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='step-container'>
        <div class='step-badge'>Login ✓</div>
        <div class='step-badge'>Data Setup ✓</div>
        <div class='step-badge active'>➔ Startup Financial KPIs & AI CFO (Step 4 of 4)</div>
    </div>
    """, unsafe_allow_html=True)

    # مؤشرات مالية متطورة جداً خاصة بالشركات الناشئة (Startup KPIs)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric(label="فترة نفاذ السيولة (Runway)", value="14.2 Month", delta="🟢 نطاق آمن جداً")
    with m2: st.metric(label="معدل الحرق الشهري (Burn Rate)", value="8,400 SAR", delta="📉 انخفض بنسبة 6%")
    with m3: st.metric(label="الهامش الإجمالي (Gross Margin)", value="72%", delta="🌱 أداء تشغيلي ممتاز")
    with m4: st.metric(label="جاهزية الامتثال (ZATCA & Tax)", value="95%", delta="متوافق")

    st.write("---")
    
    col_chat, col_viz = st.columns([1.2, 1])
    
    with col_chat:
        st.markdown("### 💬 استشارة المساعد المالي والستيرنج الذكي")
        user_query = st.text_input("اكتب سؤالك المالي هنا واضغط Enter (مثال: كيف أخفض الاستهلاك؟ أو كم الـ Runway؟)")
        
        if user_query:
            with st.spinner('جاري مراجعة النماذج المالية وحساب الـ Cohorts...'):
                time.sleep(1)
            
            q = user_query.lower()
            
            # 1. مسار الاستهلاك والمصاريف وهامش الربح
            if any(word in q for word in ["استهلاك", "اخفض", "مصاريف", "تقليل", "توفير", "المصاريف", "تكاليف"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #10B981;'>
                    <b style='color: #10B981; font-size: 16px;'>🤖 المستشار المالي (ترشيد النفقات وتحسين الهامش الإجمالي):</b><br><br>
                    بناءً على الفواتير المرفوعة وكشوف الحسابات، يتركز <b>الهدر التشغيلي (OpEx)</b> في نقطتين رئيسيتين، معالجتهما سترفع <b>الـ Gross Margin لـ 78%</b>:<br><br>
                    1️⃣ <b>رسوم الخدمات السحابية واشتراكات الـ SaaS المعلقة:</b> رصد النظام 3 اشتراكات برمجية متكررة غير نشطة بقيمة إجمالية 1,200 ريال شهرياً. إلغاؤها فوراً سيخفض <b>معدل الحرق النقدّي (Gross Burn Rate)</b>.<br>
                    2️⃣ <b>كفاءة سلاسل الإمداد (COGS):</b> تكرار الشراء الجزئي من الموردين يرفع تكاليف البضاعة المباعة بنسبة 11%. التحول للطلب الموحد بداية الشهر يحمي <b>الهامش الإجمالي</b> ويحسن دورة رأس المال العامل.
                </div>
                """, unsafe_allow_html=True)
                
            # 2. مسار النفاذ ومعدل الحرق (Runway & Burn Rate) - مصطلحات قوية للشركات الناشئة
            elif any(word in q for word in ["runway", "حرق", "نفاذ", "سيولة", "كاش", "السيولة"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #3B82F6;'>
                    <b style='color: #3B82F6; font-size: 16px;'>🤖 المستشار المالي (تحليل النفاذ الاستباقي للسيولة - Runway Analysis):</b><br><br>
                    حسب التدفقات النقدية الحالية للإيرادات والمصاريف المبرمجة آلياً:<br><br>
                    • <b>الـ Net Burn Rate (صافي الحرق الشهري):</b> مستقر عند 8,400 ريال.<br>
                    • <b>الـ Runway الحالية:</b> الكاش المتوفر في الحسابات والربط يغطي المنشأة لمدة <b>14.2 شهر قادم</b> بدون الحاجة لتمويل خارجي.<br>
                    • <b>توصية حماية الكاش:</b> إذا خططت لشراء أصول رأسمالية (CapEx) بقيمة 15,000 ريال نقداً الأسبوع القادم، ستتقلص فترة النفاذ (Runway) مباشرة إلى 12.4 شهر. ينصح النظام باعتماد خيارات الدفع الآجل (BNPL) لحفظ السيولة في مستواها الأخضر.
                </div>
                """, unsafe_allow_html=True)
                
            # 3. مسار الاستحواذ وجدوى العملاء (CAC & LTV)
            elif any(word in q for word in ["عميل", "استحواذ", "cac", "ltv", "تسويق", "العملاء"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #8B5CF6;'>
                    <b style='color: #8B5CF6; font-size: 16px;'>🤖 المستشار المالي (كفاءة الإنفاق التسويقي وجدوى العملاء):</b><br><br>
                    من خلال ربط فواتير حملات التسويق الرقمي ببيانات المبيعات المستخرجة:<br><br>
                    • <b>تكلفة الاستحواذ على العميل (CAC):</b> تبلغ حالياً 45 ريال لكل عميل جديد.<br>
                    • <b>القيمة الحيوية للعميل (LTV):</b> يبلغ متوسط الدخل المستدام من العميل الواحد 180 ريال.<br>
                    • <b>نسبة الكفاءة (LTV:CAC):</b> مستواكم الحالي هو <b>4:1</b> وهو مؤشر ممتاز جداً جاذب للمستثمرين (المعدل الصحي عالمياً هو 3:1). ميزانيتكم التسويقية الحالية تحقق عائداً إيجابياً وتدعم نمو التدفق النقدي.
                </div>
                """, unsafe_allow_html=True)

            # 4. مسار نقطة التعادل والتمويل (Break-even & Funding)
            elif any(word in q for word in ["تعادل", "تمويل", "قرض", "جولة", "استثمار"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #FBBF24;'>
                    <b style='color: #FBBF24; font-size: 16px;'>🤖 المستشار المالي (تحليل نقطة التعادل والجدارة الاستثمارية):</b><br><br>
                    بناءً على تصنيف التكاليف الثابتة والمتغيرة للفواتير المرفوعة:<br><br>
                    • <b>نقطة التعادل (Break-even Point):</b> تحتاج المنشأة لتحقيق مبيعات شهرية بقيمة 32,000 ريال لتغطية كافة المصاريف التشغيلية بالكامل والبدء في تحقيق صافي ربح حقيقي.<br>
                    • <b>الجدارة الائتمانية للتمويل:</b> نظراً لنمو التدفق النقدي الحر بنسبة 12% شهرياً، فإن جدارتكم الائتمانية تؤهلكم لطلب جولة تمويلية مصغرة أو سحب تمويل نمو متوافق مع الشريعة عبر شركائنا بحد أقصى 75,000 ريال وبأقل نسبة مرابحة في السوق.
                </div>
                """, unsafe_allow_html=True)
                
            # 5. الرد الافتراضي الشامل
            else:
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #64748B;'>
                    <b style='color: #64748B; font-size: 16px;'>🤖 المستشار المالي (SME Pulse AI):</b><br><br>
                    أهلاً بك في غرفة الحوكمة المالية للشركات الناشئة. يمكنك سؤالي واستكشاف المؤشرات الاستثمارية التالية:<br>
                    • <b>حساب الـ Runway و الـ Burn Rate</b> لمعرفة متى ينفد الكاش وعمر الشركة الحالي.<br>
                    • <b>تقييم الـ CAC والـ LTV</b> للتأكد من كفاءة وجدوى الإنفاق على التسويق والعملاء.<br>
                    • <b>تحديد نقطة التعادل (Break-even)</b> ومعادلة الهامش الإجمالي وتحسين الـ OpEx.<br>
                    • جاهزية الامتثال الضريبي وأنظمة الفوترة والربط مع <b>ZATCA</b>.
                </div>
                """, unsafe_allow_html=True)
            
    with col_viz:
        st.markdown("### 📈 نمط التدفقات النقدية والـ Runway المتوقع")
        chart_data = pd.DataFrame({
            'أشهر السنة': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو (الحالي)', 'يونيو (متوقع)'],
            'حجم السيولة المستهدفة': [15000, 18000, 16500, 21000, 22400, 24500]
        })
        st.line_chart(chart_data.set_index('أشهر السنة'))

    st.write("---")
    if st.button("🔄 العودة إلى صفحة الدخول الرئيسية"):
        st.session_state.page = 'login'
        st.rerun()
