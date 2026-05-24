import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    # Handle join-code query param: store it and redirect to student portal
    join_code = st.query_params.get('join-code')
    if join_code:
        # Persist the join code in session state so it survives the rerun
        st.session_state['pending_join_code'] = join_code
        if st.session_state['login_type'] != 'student':
            st.session_state['login_type'] = 'student'
            st.rerun()

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()

main()
