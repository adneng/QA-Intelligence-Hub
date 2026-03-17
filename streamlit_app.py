import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="QA Ops Hub", page_icon="🛡️", layout="wide")

# --- APP TITLE ---
st.title("🛡️ QA Ops Intelligence Hub")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to:", ["Ops Dashboard", "SOP Library"])
    st.markdown("---")
    st.info("Team: 30 Staff\nFocus: eGovPH / eTravel")

# --- PAGE 1: DASHBOARD ---
if page == "Ops Dashboard":
    st.subheader("📊 Team Performance")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Testers", "30")
    col2.metric("System Health", "Stable")
    col3.metric("Focus", "eGovPH / eTravel")
    
    st.write("### Today's Focus")
    st.warning("⚠️ Monitoring eKYC latency for National ID syncing.")

# --- PAGE 2: SOP LIBRARY (THE CORRECTED PART) ---
elif page == "SOP Library":
    st.subheader("📖 Knowledge Base")
    
    # This points directly to the 'sops' folder in your repo
    sop_path = "sops"
    
    if os.path.exists(sop_path):
        # This lists all files ending in .md
        files = [f for f in os.listdir(sop_path) if f.endswith('.md')]
        
        if files:
            selected_file = st.selectbox("Select troubleshooting guide:", files)
            
            # Read and display the content
            with open(os.path.join(sop_path, selected_file), "r", encoding="utf-8") as f:
                st.markdown("---")
                st.markdown(f.read())
        else:
            st.warning("No files found in 'sops' folder yet.")
    else:
        st.error(f"Cannot find the 'sops' folder. Please make sure it exists in your GitHub repo.")
