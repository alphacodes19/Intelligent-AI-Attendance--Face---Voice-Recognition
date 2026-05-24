import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
                .stApp {
                    background: #5865F2 !important;
                }
                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                }
        </style>""", unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp {
                    background: #E0E3FF !important;
                }
        </style>""", unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

        /* ── Hide Streamlit chrome ── */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding-top: 1.5rem !important; }

        /* ── Headings ── */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0 !important;
            color: #E0E3FF !important;
        }
        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0 !important;
            color: #5865F2 !important;
        }
        h3 {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600 !important;
        }
        h4, h5, h6 {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 500 !important;
        }

        /* ── Body text ── */
        p, li {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 400 !important;
        }

        /* ── Streamlit-specific text nodes (safe selectors only) ── */
        .stMarkdown p,
        .stMarkdown li,
        .stText,
        [data-testid="stMarkdownContainer"] p {
            font-family: 'Poppins', sans-serif !important;
        }

        /* ── Form inputs ── */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 400 !important;
        }

        /* ── Form labels ── */
        .stTextInput label,
        .stTextArea label,
        .stSelectbox label,
        .stFileUploader label,
        .stCameraInput label,
        .stAudioInput label {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 500 !important;
        }

        /* ── Buttons: target the text span only, NOT the icon span ──
           Streamlit renders: <button><span class="icon">…</span><span class="label">text</span></button>
           We style the button text via the p inside the label span.          */
        button p {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600 !important;
        }

        /* ── Button shapes & colours ── */
        button {
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }
        button[kind="secondary"] {
            background-color: #EB459E !important;
        }
        button[kind="tertiary"] {
            background-color: #111 !important;
        }
        button:hover { transform: scale(1.05); }

        /* ── Subheader / widget text ── */
        [data-testid="stWidgetLabel"] p,
        [data-testid="stWidgetLabel"] label {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 500 !important;
        }

        </style>""", unsafe_allow_html=True)
