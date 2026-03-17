import streamlit as st

st.set_page_config(page_title="QA Intelligence Hub", layout="wide")

st.title("🛡️ QA Ops Intelligence Hub")
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "SOP Library"])

if page == "Dashboard":
    st.subheader("Team Overview")
    c1, c2, c3 = st.columns(3)
    c1.metric("Team Size", "30 Staff")
    c2.metric("System Health", "Stable")
    c3.metric("Focus", "eGovPH / eTravel")
    st.info("Top Concern Today: eKYC Verification Lag")

elif page == "SOP Library":
    st.subheader("Knowledge Base")
    st.markdown("""
    ### 📖 SOP: eGovPH Login Troubleshooting
    1. Verify App Version (Target: 1.0.5)
    2. Check Mobile Data vs WiFi
    3. Escalation: Contact DICT Dev Team if OTP fails 3x.
    """)
