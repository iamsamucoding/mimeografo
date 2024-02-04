import pandas as pd
import streamlit as st

from mimeografo.dbconnection import connect_to_db
import mimeografo.interface as ui

def main():
    # print('Connecting to the database...')
    # conn = connect_to_db('../orders.db')

    # query = """
    # SELECT * FROM Orders LIMIT 10
    # """

    # print('Executing query...')
    # df = pd.read_sql_query(query, conn)
    # print(df.head())

    st.sidebar.title("SQL Dashboard")

    if 'container_count' not in st.session_state:
        st.session_state.container_count = 1
    
    add_button = st.button('Add new analysis')
    delete_button = st.button('Delete last analysis')

    if add_button:
        st.session_state.container_count += 1
    if delete_button:
        st.session_state.container_count -= 1
        if st.session_state.container_count < 0:
            st.session_state.container_count = 0
    
    for i in range(st.session_state.container_count):
        ui.create_slide_container(i)
    
    


    



if __name__ == '__main__':
    st.set_page_config(layout="wide")
    

    print('Running the app...')
    main()
