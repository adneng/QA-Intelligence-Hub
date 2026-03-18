import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="QA Ops Hub", page_icon="🛡️", layout="wide")

# --- MERMAID FUNCTION ---
def mermaid(code):
    st.components.v1.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=600,
    )

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
        files = [f for f in os.listdir(sop_path) if f.endswith('.md')]
        if files:
            selected_file = st.selectbox("Select troubleshooting guide:", files)
            with open(os.path.join(sop_path, selected_file), "r", encoding="utf-8") as f:
                content = f.read()
                
                # Split content to check for Mermaid code
                if "```mermaid" in content:
                    parts = content.split("```mermaid")
                    st.markdown(parts[0]) # Text before flowchart
                    
                    # Extract and render the flowchart
                    mermaid_code = parts[1].split("```")[0]
                    mermaid(mermaid_code)
                    
                    # Show any text after the flowchart
                    if "```" in parts[1]:
                        remaining = parts[1].split("```", 1)[1]
                        st.markdown(remaining)
                else:
                    st.markdown(content)
