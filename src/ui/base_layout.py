import streamlit as st


def style_background_home():
    
    st.markdown("""
                <style>
                
                .stApp{
                    background: #5965F2 !important;
                }
                
                </style>
                """
                , unsafe_allow_html = True)
    
def style_base_layout():
    st.markdown("""
                <style>
                
                .stApp {
                    background: #5865F2 !important;
                }
                </style>"""
                ,unsafe_allow_html = True)