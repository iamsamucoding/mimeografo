import streamlit as st
from streamlit_ace import st_ace


def create_slide_container(container_number: int = 0):
    container = st.container(border=True)

    # Add a text area for SQL code with SQL syntax highlighting and line numbers
    with container:
        st.subheader(f"Slide Analysis: #{container_number + 1}")
        
        st.markdown("**SQL Code**")
        sql_code = st_ace(
            language="sql",
            theme="github",
            height=200,
            show_gutter=True,  # Show line numbers
            placeholder="Write your SQL code here...",
            auto_update=True,
            key=f"sql_code_{container_number}",
        )

        st.markdown("**Plot Settings**")
        
        col1, col2 = st.columns([2, 1])

        with col1:
            options = ["Bar Plot", "Line Plot", "Scatter Plot"]
            plot = st.selectbox("Choose a plot:", options,
                                key=f"plot_{container_number}")
            
            col11, col12, col13 = st.columns(3)
            with col11:
                x_var = st.text_input("X-axis Variable",
                                        key=f"x_var_{container_number}")
            with col12:
                y_var = st.text_input("Y-axis Variable",
                                        key=f"y_var_{container_number}")
            with col13:
                hue_var = st.text_input("Hue Variable (optional)",
                                        key=f"hue_var_{container_number}")

        with col2:
            json_code = st.text_area(
                label="Plot kargs (Optional)",
                value="{}",
                height=200,
                key=f"json_code_{container_number}",
            )
        
        
        st.markdown("**Slide Properties**")
        col3, col4 = st.columns([2, 1])

        with col3:
            template_slide_options = ["Template 1", "Template 2"]
            plot = st.selectbox("Choose a template:",
                                template_slide_options,
                                key=f"template_{container_number}")
            slide_title = st.text_input("Slide Title",
                                        key=f"slide_title_{container_number}")
            sub_title = st.text_input("Slide Sub-Title",
                                        key=f"sub_title_{container_number}")

        with col4:
            st.image("https://www.slideegg.com/image/catalog/85346-Google%20Slide%20Template%20Free%20Simple.png")
        