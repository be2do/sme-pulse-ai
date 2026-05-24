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
    st.markdown("<div class='sub-title'>المستشار المالي الذكي وأتمتة الفواتير للمنشآت والشركات الناشئة</div>", unsafe_allow_html=True)
    
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
    st.markdown("<div class='main-title' style='font-size: 32px;'>SME Pulse AI - لوحة القيادة الذكية</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='step-container'>
        <div class='step-badge'>Login ✓</div>
        <div class='step-badge'>Data Setup ✓</div>
        <div class='step-badge active'>➔ Financial KPIs & AI CFO (Step 4 of 4)</div>
    </div>
    """, unsafe_allow_html=True)

    # مؤشرات مالية هجينة (للمنشآت والشركات الناشئة)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric(label="السيولة / Runway", value="14.2 Month", delta="🟢 كاش آمن")
    with m2: st.metric(label="معدل المصروف / Burn Rate", value="8,400 SAR", delta="📉 انخفض بنسبة 6%")
    with m3: st.metric(label="الهامش الإجمالي (Gross Margin)", value="72%", delta="🌱 تشغيل ممتاز")
    with m4: st.metric(label="جاهزية الزكاة والضريبة (ZATCA)", value="95%", delta="متوافق ✓")

    st.write("---")
    
    col_chat, col_viz = st.columns([1.2, 1])
    
    with col_chat:
        st.markdown("### 💬 استشارة المستشار المالي (AI CFO)")
        user_query = st.text_input("اكتب سؤالك (مثال: كيف أخفض التكاليف؟ أقدر أشتري معدات؟ كم الـ Runway؟)")
        
        if user_query:
            with st.spinner('جاري مراجعة النماذج المالية وتحليل البيانات...'):
                time.sleep(1)
            
            # تحويل النص لحروف صغيرة لمنع مشاكل الحساسية
            q = user_query.lower()
            
            # 1. الاستهلاك والمصاريف والـ SaaS
            if any(word in q for word in ["استهلاك", "اخفض", "مصاريف", "تقليل", "توفير", "المصاريف", "تكاليف", "مصروف", "هدر"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #10B981;'>
                    <b style='color: #10B981; font-size: 16px;'>🤖 المستشار المالي (ترشيد النفقات التشغيلية OpEx):</b><br><br>
                    بناءً على الفواتير المرفوعة وكشوف الحسابات، يتركز الهدر المالي في نقطتين، معالجتهما سترفع الهامش الإجمالي:<br><br>
                    1️⃣ <b>فواتير الطاقة واشتراكات الـ SaaS:</b> هناك 3 اشتراكات برمجية غير نشطة واستهلاك طاقة خارج أوقات الذروة يبلغ 1,200 ريال شهرياً. إلغاؤها وتنظيمها سيخفض <b>معدل الحرق النقدّي</b> فوراً.<br>
                    2️⃣ <b>كفاءة الموردين:</b> تكرار طلب المواد الخام على دفعات صغيرة يرفع تكاليف البضاعة (COGS) بنسبة 11%. التحول للطلب الموحد بداية الشهر يمنحك خصماً مباشراً ويحسن السيولة.
                </div>
                """, unsafe_allow_html=True)
                
            # 2. الشراء، الأجهزة، والسيولة المؤقتة
            elif any(word in q for word in ["أجهزة", "شراء", "سيولة", "جهاز", "نقد", "معدات", "كاش", "اشتري", "أشتري"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #3B82F6;'>
                    <b style='color: #3B82F6; font-size: 16px;'>🤖 المستشار المالي (توقعات السيولة وقرارات الشراء CapEx):</b><br><br>
                    مؤشر التدفق النقدي الحالي يشير إلى استقرار مالي ممتاز بمعدل سيولة حرة يبلغ 24,500 ريال لشهر يونيو. <br><br>
                    ⚠️ <b>تحذير استباقي:</b> إذا قمت بشراء أصول (أجهزة/معدات) بقيمة تزيد عن 10,000 ريال نقداً خلال هذا الأسبوع، سينخفض مؤشر الأمان المالي للمنطقة الصفراء، مما قد يسبب ضغطاً مؤقتاً لتغطية الرواتب.<br>
                    💡 <b>التوصية الذكية:</b> إرجاء قرار الشراء حتى <b>5 يونيو</b> (بعد تحصيل دفعة العميل الرئيسي) يضمن بقاء منشأتك في النطاق الأخضر الآمن، ويحافظ على فترة النفاذ (Runway).
                </div>
                """, unsafe_allow_html=True)

            # 3. النفاذ ومعدل الحرق (Runway & Burn Rate) للشركات الناشئة
            elif any(word in q for word in ["runway", "حرق", "نفاذ", "معدل الحرق", "ينفد", "بقاء"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #06B6D4;'>
                    <b style='color: #06B6D4; font-size: 16px;'>🤖 المستشار المالي (تحليل نفاذ السيولة - Runway Analysis):</b><br><br>
                    حسب التدفقات النقدية الحالية للإيرادات والمصاريف:<br><br>
                    • <b>الـ Net Burn Rate (صافي الحرق الشهري):</b> مستقر عند 8,400 ريال.<br>
                    • <b>الـ Runway الحالية:</b> الكاش المتوفر في الحسابات يغطي المنشأة لمدة <b>14.2 شهر قادم</b> بدون الحاجة لتمويل خارجي.<br>
                    • وضع المنشأة يعتبر ممتازاً جداً وجاذباً للمستثمرين في الجولات القادمة.
                </div>
                """, unsafe_allow_html=True)
                
            # 4. الاستحواذ وجدوى العملاء (CAC & LTV)
            elif any(word in q for word in ["عميل", "استحواذ", "cac", "ltv", "تسويق", "العملاء", "اعلانات", "إعلانات"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #8B5CF6;'>
                    <b style='color: #8B5CF6; font-size: 16px;'>🤖 المستشار المالي (كفاءة الإنفاق التسويقي):</b><br><br>
                    من خلال تحليل فواتير التسويق ومطابقتها مع المبيعات:<br><br>
                    • <b>تكلفة الاستحواذ (CAC):</b> 45 ريال لكل عميل جديد.<br>
                    • <b>القيمة الحيوية للعميل (LTV):</b> الدخل المستدام من العميل 180 ريال.<br>
                    • <b>نسبة الكفاءة (LTV:CAC):</b> مستواكم الحالي هو <b>4:1</b> (مؤشر صحي جداً يفوق المعدل العالمي 3:1). ميزانيتكم التسويقية تحقق عائداً عالياً ولا يوجد بها هدر.
                </div>
                """, unsafe_allow_html=True)

            # 5. التمويل والقروض والاستثمار
            elif any(word in q for word in ["تمويل", "قرض", "قروض", "فلوس", "بحر", "استثمار", "مستثمر", "جولة"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #EC4899;'>
                    <b style='color: #EC4899; font-size: 16px;'>🤖 المستشار المالي (الجدارة الائتمانية والتمويل):</b><br><br>
                    نظراً لنمو التدفق النقدي الحر (Free Cash Flow) بنسبة 12%، تمتلك المنشأة فرصة قوية للحصول على تمويل:<br><br>
                    • <b>التمويل البنكي:</b> جدارتكم تؤهلكم لطلب تمويل مرابحة بحد أقصى 75,000 ريال بأقل نسبة فائدة عبر شركائنا في المصرفية المفتوحة.<br>
                    • <b>الاستثمار الجريء (VC):</b> مقاييس النمو (Runway 14 Months & LTV:CAC 4:1) تجعلكم جاهزين تماماً لفتح جولة استثمارية (Seed Round) بتقييم تنافسي ممتاز.
                </div>
                """, unsafe_allow_html=True)
                
            # 6. الزكاة والضرائب
            elif any(word in q for word in ["زكاة", "ضريبة", "ضرائب", "zatca", "الزكاة", "اقرار", "إقرار", "فاتورة"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #FBBF24;'>
                    <b style='color: #FBBF24; font-size: 16px;'>🤖 المستشار المالي (حوكمة ZATCA والضرائب):</b><br><br>
                    النظام قام بمراجعة الفواتير المرفوعة ومطابقتها تلقائياً:<br><br>
                    • <b>مستوى الامتثال:</b> 95% متوافق مع أنظمة المرحلة الثانية للربط والتكامل لهيئة الزكاة والضريبة والجمارك.<br>
                    • <b>الإقرار الضريبي:</b> تم تصنيف مبالغ الـ VAT بدقة، والملف جاهز للتصدير بنقرة واحدة لتفادي غرامات التأخير.<br>
                    • <b>تنبيه:</b> توجد فاتورتان قيد المعالجة للتحقق من الرقم الضريبي للمورد.
                </div>
                """, unsafe_allow_html=True)

            # 7. نقطة التعادل
            elif any(word in q for word in ["تعادل", "breakeven", "نقطة التعادل", "ارباح", "ربح", "تغطية"]):
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #F97316;'>
                    <b style='color: #F97316; font-size: 16px;'>🤖 المستشار المالي (تحليل نقطة التعادل Break-even):</b><br><br>
                    بناءً على تصنيف التكاليف الثابتة والمتغيرة:<br><br>
                    • تحتاج المنشأة لتحقيق مبيعات شهرية بقيمة <b>32,000 ريال</b> لتغطية كافة المصاريف التشغيلية بالكامل (نقطة التعادل).<br>
                    • أي ريال يتم إدخاله بعد هذا الرقم سيتحول مباشرة إلى <b>صافي ربح حقيقي (Net Profit)</b> يضاف إلى السيولة النقدية.
                </div>
                """, unsafe_allow_html=True)
                
            # 8. الرد الافتراضي الشامل للترحيب وتوجيه المستخدم (القائمة الذكية)
            else:
                st.markdown("""
                <div class='ai-box' style='border-right: 4px solid #64748B;'>
                    <b style='color: #64748B; font-size: 16px;'>🤖 المستشار المالي (SME Pulse AI):</b><br><br>
                    أهلاً بك. تم مزامنة السجلات المالية بالكامل. يمكنك توجيه أي سؤال لي، وسأقوم بتحليله فوراً. <b>أمثلة لما يمكنك سؤاله:</b><br><br>
                    📉 <i>"كيف أقدر أقلل المصاريف والتكاليف؟"</i><br>
                    💻 <i>"هل السيولة تسمح بشراء أجهزة جديدة؟"</i><br>
                    ⏳ <i>"كم الـ Runway ومعدل الحرق الحالي للشركة؟"</i><br>
                    📊 <i>"كم تكلفة الاستحواذ على العميل CAC؟"</i><br>
                    💰 <i>"هل وضعي يسمح بطلب تمويل أو استثمار؟"</i><br>
                    ⚖️ <i>"متى نوصل لنقطة التعادل أو الربح؟"</i><br>
                    🧾 <i>"هل ملفات الضريبة جاهزة لهيئة الزكاة ZATCA؟"</i>
                </div>
                """, unsafe_allow_html=True)
            
    with col_viz:
        st.markdown("### 📈 نمط التدفقات والـ Runway")
        chart_data = pd.DataFrame({
            'أشهر السنة': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو (متوقع)'],
            'حجم السيولة المستهدفة': [15000, 18000, 16500, 21000, 22400, 24500]
        })
        st.line_chart(chart_data.set_index('أشهر السنة'))

    st.write("---")
    if st.button("🔄 العودة إلى صفحة الدخول"):
        st.session_state.page = 'login'
        st.rerun()
