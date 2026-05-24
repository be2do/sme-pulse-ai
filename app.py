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

st.markdown(”</div>”, unsafe_allow_html=True)
