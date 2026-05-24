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
    /* تغيير خلفية التطبيق بالكامل للكحلي الداكن الفخم */
    .stApp {
        background-color: #0B111E;
        color: #F8FAFC;
    }
    
    /* ستايل العنوان الرئيسي */
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

    /* ستايل بطاقات خيارات تحصيل البيانات (قماش البطاقة) */
    .data-card {
        background-color: #151F32;
        border: 1px solid #22334F;
        border-radius: 16px;
        padding: 25px;
        text-align: right;
        transition: all 0.3s ease;
        cursor: pointer;
        min-height: 140px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .data-card:hover {
        border-color: #3B82F6;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.2);
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

    /* شريط تقدم الخطوات الاحترافي (Step Progress) */
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
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة التطبيق (Session State) للتنقل بين الشاشات بلمسة زر
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# ==========================================
# 🛑 الشاشة الأولى: صفحة اضغط للدخول (Login)
# ==========================================
if st.session_state.page == 'login':
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='main-title'>SME Pulse AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>المستشار المالي الذكي وأتمتة الفواتير للمنشآت الصغيرة والمتوسطة</div>", unsafe_allow_html=True)
    
    # زر الدخول ممتد ومحسّن بصرياً في المنتصف
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        if st.button("اضغط للدخول إلى النظام ➔", use_container_width=True, type="primary"):
            st.session_state.page = 'data_setup'
            st.rerun()
            
    # مؤشر الخطوات السفلي الصغير
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
    st.markdown("<div class='sub-title'>إعداد وتهيئة البيانات المالية للمنشأة</div>", unsafe_allow_html=True)
    
    # شريط الخطوات المحدث
    st.markdown("""
    <div class='step-container'>
        <div class='step-badge'>Login ✓</div>
        <div class='step-badge active'>➔ Data Setup (Step 1 of 4)</div>
        <div class='step-badge'>Insights</div>
    </div>
    """, unsafe_allow_html=True)
    
    # علامات التبويب المودرن (Tabs) لتوزيع الخيارات مثل الصورة
    tab1, tab2 = st.tabs(["📋 تحصيل البيانات", "🤖 تهيئة وحوكمة البيانات"])
    
    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # إنشاء شبكة بطاقات (2x2 Grid) قابلة للتفاعل والضغط
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)
        
        with row1_col2:
            st.markdown("""
            <div class='data-card'>
                <div class='card-title'>📄 ارفع الفاتورة الذكية (OCR)</div>
                <div class='card-desc'>ارفع الفاتورة المستلمة أو المصروفة بتقنية الذكاء الاصطناعي لتقرأ وتصنف قيمتها وبنودها آلياً دون أي كتابة يدوية.</div>
            </div>
            """, unsafe_allow_html=True)
            invoice_file = st.file_uploader("اختر ملف الفاتورة أو صورتها هنا:", type=["png", "jpg", "jpeg", "pdf"], key="ocr_upload")
            if invoice_file:
                st.success("✅ تم استلام الفاتورة وربطها بالهيكل المالي!")
                
        with row1_col1:
            st.markdown("""
            <div class='data-card'>
                <div class='card-title'>🏦 اربط حسابك البنكي مباشرة</div>
                <div class='card-desc'>ربط حساب المنشأة البنكي التجاري عبر واجهات الـ API الآمنة لتحديث كشف الحساب والتدفقات النقدية أولاً بأول.</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🔗 ابدأ الربط البنكي الآمن", use_container_width=True):
                st.info("جاري فتح بوابة الربط البنكي المعتمدة المفتوحة...")

        with row2_col2:
            st.markdown("""
            <div class='data-card'>
                <div class='card-title'>📝 ادخل البيانات يدوياً</div>
                <div class='card-desc'>إذا كان لديك بنود استثنائية أو مصروفات نقدية مباشرة (كاش)، يمكنك تعبئة تفاصيلها وجدولتها هنا يدوياً.</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("✍️ فتح جدول الإدخال اليدوي", use_container_width=True):
                st.toggle("تفعيل لوحة السجلات اليدوية")

        with row2_col1:
            st.markdown("""
            <div class='data-card'>
                <div class='card-title'>📂 ارفع كشف الحساب كـ PDF</div>
                <div class='card-desc'>ارفع كشف الحساب البنكي التاريخي (لأخر 3 أشهر أو سنة) بصيغة PDF ليقوم النظام بهندسة البيانات وبناء نموذج التنبؤ.</div>
            </div>
            """, unsafe_allow_html=True)
            statement_file = st.file_uploader("ارفع كشف حساب المنشأة التجاري:", type=["pdf"], key="pdf_upload")
            if statement_file:
                st.success("✅ تم رفع الكشف بنجاح، جاري هندسة التدفق النقدي!")

    with tab2:
        st.write("---")
        st.info("💡 قسم الأتمتة: بمجرد اختيار وتجهيز البيانات من التبويب الأول، ستقوم محركات الـ AI بحوكمة وتصنيف العمليات طبقاً لأدلة المحاسبة السعودية للهيئات والمنشآت.")

    # زر الانتقال للشاشة التالية (التحليلات والمستشار المالي)
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
    st.markdown("<div class='main-title' style='font-size: 32px;'>SME Pulse AI - لوحة القيادة</div>", unsafe_allow_html=True)
    
    # شريط الخطوات المكتمل
    st.markdown("""
    <div class='step-container'>
        <div class='step-badge'>Login ✓</div>
        <div class='step-badge'>Data Setup ✓</div>
        <div class='step-badge active'>➔ Insights & AI CFO (Step 4 of 4)</div>
    </div>
    """, unsafe_allow_html=True)

    # إحصائيات النظام الفخمة المستخرجة
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="السيولة المتوقعة (الشهر القادم)", value="24,500 SAR", delta="🌱 نمو مستقر +12%")
    with m2:
        st.metric(label="إجمالي المصاريف الحالية", value="12,400 SAR", delta="📉 انخفاض في التكاليف -4%")
    with m3:
        st.metric(label="جاهزية ملفات الزكاة والدخل", value="95%", delta="✓ ZATCA متوافق مع")

    st.write("---")
    
    # غرف العمل المشتركة بين التحليل البصري والشات الذكي
    col_chat, col_viz = st.columns([1.2, 1])
    
    with col_chat:
        st.markdown("### 💬 استشارة المساعد المالي الذكي")
        user_query = st.text_input("اكتب سؤالك المالي بالعامية أو الفصحى (مثال: هل أقدر أشتري أجهزة جديدة؟)")
        if user_query:
            with st.spinner('جاري تحليل المحفظة المالية...'):
                time.sleep(1)
            st.markdown("""
            <div style='background-color: #151F32; padding: 15px; border-radius: 10px; border-right: 4px solid #3B82F6;'>
                <b>🤖 المستشار الذكي:</b> بناءً على قراءات الفواتير المرفوعة ومؤشر السيولة القادم، وضعك مستقر وممتاز جداً. يفضل إتمام عمليات الشراء الرأسمالية بعد تاريخ 5 يونيو لضمان بقاء التدفق النقدي في الأمان الجيد.
            </div>
            """, unsafe_allow_html=True)
            
    with col_viz:
        st.markdown("### 📈 نمط التدفقات النقدية")
        # بناء رسم بياني تفاعلي محاكي للمستقبل
        chart_data = pd.DataFrame({
            'أشهر السنة': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو (الحالي)', 'يونيو (متوقع)'],
            'حجم السيولة المستهدفة': [15000, 18000, 16500, 21000, 22400, 24500]
        })
        st.line_chart(chart_data.set_index('أشهر السنة'))

    # زر الرجوع للبداية لإعادة التجربة أمام الحكام
    st.write("---")
    if st.button("🔄 العودة إلى صفحة الدخول الرئيسية"):
        st.session_state.page = 'login'
        st.rerun()
