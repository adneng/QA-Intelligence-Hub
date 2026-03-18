import streamlit as st
import os
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="QA Ops Hub", page_icon="🛡️", layout="wide")

# --- MERMAID FUNCTION ---
def mermaid(code):
    components.html(
        f"""
        <div id="mermaid-container">
            <style>
                /* 1. Force all text inside boxes to be BLACK and BOLD */
                .mermaid text {{
                    fill: black !important;
                    font-weight: bold !important;
                    font-family: 'sans-serif' !important;
                    font-size: 14px !important;
                }}
                /* 2. Force the ARROWS and LINES to be WHITE so they show up on dark background */
                .mermaid .edgePaths path {{
                    stroke: #ffffff !important;
                    stroke-width: 2px !important;
                }}
                /* 3. Force the ARROWHEADS to be WHITE */
                .mermaid .marker {{
                    fill: #ffffff !important;
                    stroke: #ffffff !important;
                }}
                /* 4. Force the labels on arrows (YES/NO) to be black text on white background */
                .mermaid .edgeLabel {{
                    color: black !important;
                    background-color: #ffffff !important;
                    font-weight: bold !important;
                    padding: 2px !important;
                    border-radius: 4px !important;
                }}
            </style>
            <pre class="mermaid">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ 
                startOnLoad: true, 
                theme: 'base',
                themeVariables: {{
                    'primaryColor': '#ffffff',
                    'edgeLabelBackground':'#ffffff',
                    'tertiaryColor': '#ffffff',
                    'lineColor': '#ffffff'
                }}
            }});
        </script>
        """,
        height=2000,
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
        files = sorted([f for f in os.listdir(sop_path) if f.endswith('.md')])
        if files:
            selected_file = st.selectbox("Select troubleshooting guide:", files)
            with open(os.path.join(sop_path, selected_file), "r", encoding="utf-8") as f:
                content = f.read()
                
                if "```mermaid" in content:
                    parts = content.split("```mermaid")
                    st.markdown(parts[0]) 
                    
                    mermaid_code = parts[1].split("```")[0]
                    mermaid(mermaid_code)
                    
                    remaining = parts[1].split("```")
                    if len(remaining) > 1:
                        st.markdown(remaining[1])
                else:
                    st.markdown(content)
    else:
        st.error("Folder 'sops' not found!")
