from mimeografo.dbconnection import connect_to_db
import streamlit as st
from streamlit_ace import st_ace

import pandas as pd
import streamlit as st

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
        container = st.container(border=True)

        # Add a text area for SQL code with SQL syntax highlighting and line numbers
        with container:
            st.subheader("Analysis")
            
            st.markdown("**SQL Code**")
            sql_code = st_ace(
                language="sql",
                theme="github",
                height=200,
                show_gutter=True,  # Show line numbers
                placeholder="Write your SQL code here...",
                auto_update=True,
                key=f"sql_code_{i}",
            )

            st.markdown("**Plot Settings**")
            
            col1, col2 = st.columns([2, 1])

            with col1:
                options = ["Bar Plot", "Line Plot", "Scatter Plot"]
                plot = st.selectbox("Choose a plot:", options, key=f"plot_{i}")
                
                col11, col12, col13 = st.columns(3)
                with col11:
                    x_var = st.text_input("X-axis Variable", key=f"x_var_{i}")
                with col12:
                    y_var = st.text_input("Y-axis Variable", key=f"y_var_{i}")
                with col13:
                    hue_var = st.text_input("Hue Variable (optional)", key=f"hue_var_{i}")

            with col2:
                json_code = st.text_area(
                    label="Plot kargs (Optional)",
                    value="{}",
                    height=200,
                    key=f"json_code_{i}",
                )
            
            
            st.markdown("**Slide Properties**")
            col3, col4 = st.columns([2, 1])

            with col3:
                template_slide_options = ["Template 1", "Template 2"]
                plot = st.selectbox("Choose a template:", template_slide_options, key=f"template_{i}")
                slide_title = st.text_input("Slide Title", key=f"slide_title_{i}")
                sub_title = st.text_input("Slide Sub-Title", key=f"sub_title_{i}")

            with col4:
                st.image("https://www.slideegg.com/image/catalog/85346-Google%20Slide%20Template%20Free%20Simple.png")


    



if __name__ == '__main__':
    st.set_page_config(layout="wide")
    

    print('Running the app...')
    main()
