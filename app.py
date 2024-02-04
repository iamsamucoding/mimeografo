import pandas as pd
import streamlit as st

from mimeografo.dbconnection import connect_to_db
import mimeografo.interface as ui

def main():
    # print('Connecting to the database...')
    conn = connect_to_db('./orders.db')

    st.sidebar.title("SQL Dashboard")

    col1, col2 = st.columns([6, 1])
    with col1:
        st.header("Mimeografo")
    with col2:
        st.image("./img/mimeograph.jpeg", use_column_width=True)

    if 'container_count' not in st.session_state:
        st.session_state.container_count = 1
    
    if 'data_preview' not in st.session_state:
        st.session_state.data_preview = []

    if 'charts' not in st.session_state:
        st.session_state.charts = []
    
    add_button = st.button('Add new analysis')
    delete_button = st.button('Delete last analysis')

    if add_button:
        st.session_state.container_count += 1
    if delete_button:
        st.session_state.container_count -= 1
        if st.session_state.container_count < 0:
            st.session_state.container_count = 0
    
    for i in range(st.session_state.container_count):
        ui.create_slide_container(i, conn)
    
    conn.close()


    



if __name__ == '__main__':
    st.set_page_config(layout="wide", page_title="Mimeografo")
    

    print('Running the app...')
    main()
