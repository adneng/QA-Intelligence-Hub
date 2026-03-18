import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="QA Ops Hub", page_icon="🛡️", layout="wide")

st.title("🛡️ QA Ops Intelligence Hub")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to:", ["Ops Dashboard", "SOP Library"])

# --- PAGE 1: DASHBOARD ---
if page == "Ops Dashboard":
    st.subheader("📊 Team Performance")
    st.info("Accountability check: 30 Staff Active.")

# --- PAGE 2: SOP LIBRARY ---
elif page == "SOP Library":
    st.subheader("📖 Knowledge Base")
    sop_path = "sops"
    
    if os.path.exists(sop_path):
        files = sorted([f for f in os.listdir(sop_path) if f.endswith('.md')])
        if files:
            selected_file = st.selectbox("Select troubleshooting guide:", files)
            with open(os.path.join(sop_path, selected_file), "r", encoding="utf-8") as f:
                content = f.read()
                st.markdown(content) # Simpleng Markdown display
    else:
        st.error("Folder 'sops' not found!")
