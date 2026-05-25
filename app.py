import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen


def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    # Read join-code ONCE and immediately persist it to session state.
    # st.query_params is only reliable on the very first render;
    # after any st.rerun() it may be empty depending on the host.
    join_code = st.query_params.get('join-code')
    if join_code:
        st.session_state['pending_join_code'] = join_code
        # Clear it from the URL so it doesn't re-trigger on every rerun
        st.query_params.clear()

    # If we have a pending code and the user is not yet in the student portal,
    # route them there now.
    if st.session_state.get('pending_join_code'):
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