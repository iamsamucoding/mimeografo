import streamlit as st
from pptx import Presentation

from mimeografo.dbconnection import connect_to_db
import mimeografo.interface as ui

def main():
    if "presentation" not in st.session_state:
        st.session_state.presentation = \
            Presentation('./assets/pptx/template.pptx')
    if 'container_count' not in st.session_state:
        st.session_state.container_count = 1
    if 'data_preview' not in st.session_state:
        st.session_state.data_preview = []
    if 'charts' not in st.session_state:
        st.session_state.charts = []
    if 'previous_session_state' not in st.session_state:
        st.session_state.previous_session_state = {}

    conn = connect_to_db('./orders.db')

    st.sidebar.title("SQL Dashboard")

    col1, col2 = st.columns([6, 1])
    with col1:
        st.header("Mimeografo")
    with col2:
        st.image("./assets/img/mimeograph.jpeg", use_column_width=True)

    add_button = st.button('Add new analysis')
    delete_button = st.button('Delete last analysis')
    trigger_button = st.button('Generate Slides')
    st.session_state.trigger_button = trigger_button

    if add_button:
        st.session_state.container_count += 1

    if delete_button:
        last_cont_idx = st.session_state.container_count - 1

        if st.session_state.container_count > 0:
            print(f"----> DELETING: Container {last_cont_idx}")
            st.session_state.container_count -= 1
            st.session_state.data_preview.pop()
            st.session_state.charts.pop()
            keys_to_delete = [key for key in \
                              st.session_state.previous_session_state.keys() \
                                if key.startswith(f'container_{last_cont_idx}')]
            for key in keys_to_delete:
                del st.session_state.previous_session_state[key]
    
    for i in range(st.session_state.container_count):
        ui.create_slide_container(i, conn)
    
    st.markdown("[Back to Top](#mimeografo)")

    conn.close()


    



if __name__ == '__main__':
    st.set_page_config(layout="wide", page_title="Mimeografo")
    

    print('Running the app...')
    main()
