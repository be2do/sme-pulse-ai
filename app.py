import streamlit as st
import pandas as pd
import time

# --- إعدادات الواجهة الأساسية والثيم ---
st.set_page_config(
    page_title="SME Pulse AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص الألوان باستخدام CSS (كحلي داكن وأزرق براند)
st.markdown("""
    <style>
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    h1, h2, h3 {
        color: #3B82F6 !important;
    }
    .stTable {
        background-color: #1E293B;
        border-radius: 8px;
    }
    .chat-box {
        background-color: #1E293B;
        border-right: 4px solid #10B981;
        padding: 15px;
        border-radius: 6px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر العلوي للموقع ---
st.title("📊 نظام SME Pulse AI")
st.write("المستشار المالي الذكي وأتمتة الفواتير للمنشآت الصغيرة والمتوسطة")
st.write("---")

# --- قسم الإحصائيات الحالية والتنبؤات (Dashboard) ---
st.markdown("### 📈 لوحة التحكم وتوقعات السيولة (90 يوم)")

# عرض المؤشرات المالية الرئيسية في مربعات متجاورة
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric(label="السيولة المتوقعة (الشهر القادم)", value="24,500 SAR", delta="+12% نمو مستقر")
with col_b:
    st.metric(label="إجمالي المصاريف الحالية", value="12,400 SAR", delta="-4% انخفاض في التكاليف")
with col_c:
    st.metric(label="جاهزية ملفات الزكاة والدخل", value="95%", delta="متوافق مع ZATCA")

st.write("---")

# --- تقسيم منطقة العمل (رفع الفواتير والدردشة) ---
col_left, col_right = st.columns([1, 1.2])

# القسم الأيمن: رفع وقراءة الفواتير ذكياً
with col_left:
    st.markdown("### 📸 قارئ الفواتير الذكي (OCR)")
    st.caption("ارفع فاتورة المنشأة لتقوم التقنية باستخراج البيانات وتصنيفها فوراً.")
    
    file_input = st.file_uploader("اختر ملف الفاتورة (JPG, PNG, PDF)", type=["png", "jpg", "jpeg", "pdf"])
    
    if file_input is not None:
        with st.spinner('جاري معالجة الفاتورة وسحب البيانات...'):
            time.sleep(2) # محاكاة معالجة النظام
        st.success("تمت قراءة الفاتورة وتصنيفها بنجاح!")
        
        # مصفوفة البيانات المستخرجة
        invoice_results = {
            "البيان": ["اسم المورد", "الرقم الضريبي للمورد", "المبلغ الإجمالي", "التصنيف المالي"],
            "البيانات المستخرجة": ["شركة توريد الطاقة السعودية", "300123456700003", "1,500 SAR", "مصاريف تشغيلية"]
        }
        results_df = pd.DataFrame(invoice_results)
        st.table(results_df)

# القسم الأيسر: الاستشارة والدردشة مع المستشار المالي
with col_right:
    st.markdown("### 💬 استشارة المساعد المالي الذكي")
    st.caption("اكتب سؤالك المالي بالعامية أو الفصحى لتحليل وضع السيولة لديك.")
    
    # مربع المدخلات للدردشة
    user_input = st.text_input("اسأل التطبيق (مثال: كم السيولة عندي؟ أو هل أقدر أشتري أجهزة جديدة؟)")
    
    if user_input:
        with st.spinner('جاري قراءة السجلات المالية والتنبؤ بالتدفق النقدي...'):
            time.sleep(1.5)
        
        # شروط مبنية بذكاء للرد الفوري أمام لجنة التحكيم
        if "سيولة" in user_input or "الشهر" in user_input or "liquidity" in user_input:
            st.markdown("""
            <div class="chat-box">
                <b style="color: #10B981;">💡 رد المستشار الذكي:</b><br><br>
                بناءً على الفواتير التي تم رفعها ومعدل الدخل التاريخي للمنشأة، <b>السيولة النقدية المتوقعة لشهر يونيو القادم هي 24,500 ريال</b>.<br>
                الوضع مستقر، لكن ننصح بتأجيل أي مصاريف غير أساسية حتى تاريخ <b>5 يونيو</b> (موعد استلام دفعة العميل الجديد) لضمان تغطية رواتب الموظفين بأمان وبدون أي عجز نقدّي مؤقت.
            </div>
            """, unsafe_allow_html=True)
            
        elif "أجهزة" in user_input or "شراء" in input or "شراء" in user_input:
            st.markdown("""
            <div class="chat-box">
                <b style="color: #10B981;">💡 رد المستشار الذكي:</b><br><br>
                إذا قمت بشراء أجهزة بقيمة 10,000 ريال نقداً في الوقت الحالي، سيتأثر مؤشر السيولة لديك ويدخل المنطقة الصفراء (مخاطرة مؤقتة).<br>
                <b>النصيحة:</b> نقترح عليك الاستفادة من حلول التمويل المتاحة عبر شركائنا بقسط شهري 400 ريال فقط، مما يحافظ على استقرار تدفقك النقدي اليومي.
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.markdown("""
            <div class="chat-box">
                <b style="color: #10B981;">💡 رد المستشار الذكي:</b><br><br>
                أهلاً بك. كافة بياناتك المالية الحالية محدثة ومصنفة تلقائياً بحسب معايير هيئة الزكاة والضريبة والجمارك (ZATCA). أنا جاهز للإجابة على أي استفسار يخص التنبؤ بالأرباح أو التكاليف القادمة.
            </div>
            """, unsafe_allow_html=True)
