import streamlit as st

    
def header_home():
    col1, col2 = st.columns(2)
    st.markdown
    with col1:
        if st.button('Teacher Portal'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    st.markdown      
    with col2:
        if st.button('Student Portal'):
            st.session_state['login_type'] = 'student'
            st.rerun()
    



