import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid #e2e8f0; margin-bottom:20px; font-family:'Poppins', sans-serif;">
        <h3 style="margin:0; color: #1e293b; font-size: 1.3rem; font-weight:600; font-family:'Poppins', sans-serif;">{name}</h3>
        <p style="color:#64748b; margin:10px 0; font-size:0.9rem; font-family:'Poppins', sans-serif;">
            Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px; font-weight:600;">{code}</span>
            &nbsp;|&nbsp; Section : <span style="font-weight:500;">{section}</span>
        </p>
        """
    
    if stats:
        html += """
        <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:8px;">
        """
        for icon, label, value in stats:
            html += f'<div style="background:#EB459E10; padding:5px 12px; border-radius:12px; font-size:0.85rem; font-family:\'Poppins\', sans-serif;">{icon} <b style="font-weight:600;">{value}</b> <span style="color:#64748b;">{label}</span></div>'
        
        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
