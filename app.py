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
    # Create a container
    container = st.container(border=True)

    # Add a text area for SQL code with SQL syntax highlighting and line numbers
    with container:
        st.subheader("Analysis")
        
        st.markdown("**SQL Code**")
        sql_code = st_ace(
            language="sql",
            theme="github",
            key="ace-editor",
            height=200,
            show_gutter=True,  # Show line numbers
            placeholder="Write your SQL code here...",
            auto_update=True
        )

        st.markdown("**Plot Settings**")
        
        col1, col2 = st.columns([2, 1])

        with col1:
            options = ["Bar Plot", "Line Plot", "Scatter Plot"]
            plot = st.selectbox("Choose a plot:", options)
            
            col11, col12, col13 = st.columns(3)
            with col11:
                x_var = st.text_input("X-axis Variable")
            with col12:
                y_var = st.text_input("Y-axis Variable")
            with col13:
                hue_var = st.text_input("Hue Variable (optional)")

        with col2:
            json_code = st.text_area(
                label="Plot kargs (Optional)",
                value="{}",
                height=200
            )
        
        
        st.markdown("**Slide Properties**")
        col3, col4 = st.columns([2, 1])

        with col3:
            template_slide_options = ["Template 1", "Template 2"]
            plot = st.selectbox("Choose a template:", template_slide_options)
            slide_title = st.text_input("Slide Title")
            sub_title = st.text_input("Slide Sub-Title")

            if slide_title == "":
                st.warning("Please enter a Slide Title.")
                # st.stop()
        with col4:
            st.image("https://www.slideegg.com/image/catalog/85346-Google%20Slide%20Template%20Free%20Simple.png")





if __name__ == '__main__':
    st.set_page_config(layout="wide")

    print('Running the app...')
    main()
