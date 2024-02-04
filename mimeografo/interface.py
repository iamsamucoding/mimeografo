import streamlit as st
from streamlit_ace import st_ace

import mimeografo.datahandler as dathand
import mimeografo.dataviz as viz


def create_slide_container(container_number: int = 0, conn = None):
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
        
        st.markdown("**Slide Properties**")
        col1, col2 = st.columns([2, 1])

        with col1:
            template_slide_options = ["Template 1", "Template 2"]
            plot = st.selectbox("Choose a template:",
                                template_slide_options,
                                key=f"template_{container_number}")
            slide_title = st.text_input("Slide Title",
                                        key=f"slide_title_{container_number}")
            sub_title = st.text_input("Slide Sub-Title",
                                        key=f"sub_title_{container_number}")

        with col2:
            st.image("https://www.slideegg.com/image/catalog/85346-Google%20Slide%20Template%20Free%20Simple.png")
        
        col3, col4 = st.columns([2, 1])

        with col3:
            options = ["Bar Plot", "Line Plot", "Scatter Plot"]
            plot = st.selectbox("Choose a plot:", options,
                                key=f"plot_{container_number}")
            
            col31, col32, col33 = st.columns(3)
            with col31:
                x_var = st.text_input("X-axis Variable",
                                        key=f"x_var_{container_number}")
            with col32:
                y_var = st.text_input("Y-axis Variable",
                                        key=f"y_var_{container_number}")
            with col33:
                hue_var = st.text_input("Hue Variable",
                                        key=f"hue_var_{container_number}")

        with col4:
            chart_kargs = st.text_area(
                label="Chart kargs",
                value='{\n    "plt": {},\n    "sns": {}\n}',
                height=200,
                key=f"chart_kargs_{container_number}",
            )

        col5, col6 = st.columns([1, 2])
        with col5:
            st.markdown("**Data Preview**")
            data_preview = st.empty()
            if container_number < len(st.session_state.data_preview):
                data_preview.write(st.session_state.data_preview[container_number])
        with col6:
            st.markdown("**Chart Preview**")
            chart = st.empty()
            if container_number < len(st.session_state.charts):
                chart.pyplot(st.session_state.charts[container_number],
                                   use_container_width=True)

        if st.button("Preview",
                     key=f"generate_slide_{container_number}") \
           and conn and sql_code:
            df = dathand.query_db(sql_code, conn)
            fig = viz.plot_data(df, plot, x_var, y_var, hue_var, chart_kargs)

            if container_number < len(st.session_state.charts):
                st.session_state.data_preview[container_number] = df.head(10)
                st.session_state.charts[container_number] = fig
            else:
                st.session_state.data_preview.append(df.head(10))
                st.session_state.charts.append(fig)
            data_preview.write(st.session_state.data_preview[container_number])
            chart.pyplot(st.session_state.charts[container_number],
                               use_container_width=True)
