import streamlit as st
from streamlit_ace import st_ace

import mimeografo.datahandler as dathand
import mimeografo.dataviz as viz

def get_container_keys(container_number: int = 0):
    return [
        f"container_{container_number}__sql_code",
        f"container_{container_number}__template",
        f"container_{container_number}__title",
        f"container_{container_number}__subtitle",
        f"container_{container_number}__plot",
        f"container_{container_number}__x_var_",
        f"container_{container_number}__y_var",
        f"container_{container_number}__hue_var",
        f"container_{container_number}__chart_kargs",
    ]


def empty_container_state(container_number: int = 0):
    container_keys = get_container_keys(container_number)

    return {key: "" for key in container_keys}


def has_container_state_changed(container_number: int = 0):
    previous_session_state = st.session_state.previous_session_state
    session_state = st.session_state

    container_keys = get_container_keys(container_number)

    has_changed = False
    for key in container_keys:
        if previous_session_state[key] != session_state[key]:
            has_changed = True
            break
    return has_changed

def update_container_state(container_number: int = 0):
    container_keys = get_container_keys(container_number)
    container_session_state = {key: st.session_state[key] \
                               for key in container_keys}

    st.session_state.previous_session_state.update(container_session_state)


def initialize_container_values(container_number: int = 0):
    if container_number >= len(st.session_state.data_preview):
        st.session_state.data_preview.append(None)
        st.session_state.charts.append(None)
        st.session_state.previous_session_state.update(
            empty_container_state(container_number)
        )

def create_slide_container(container_number: int = 0, conn=None):
    initialize_container_values(container_number)

    container = st.container(border=True)

    with container:
        st.subheader(f"Slide Analysis: #{container_number + 1}")

        st.markdown("**SQL Code**")

        # Streaminlit-Ace is not intelligent enough to handle the
        # session_state and values automatically, so we need to
        # manually handle it
        key = f"container_{container_number}__sql_code"
        val = st.session_state[key] if key in st.session_state else ""
        sql_code = st_ace(
            key=key,
            language="sql",
            theme="github",
            height=200,
            show_gutter=True,  # Show line numbers
            placeholder="Write your SQL code here...",
            auto_update=True,
            value=val,
        )

        st.markdown("**Plot Settings**")

        st.markdown("**Slide Properties**")
        col1, col2 = st.columns([2, 1])

        with col1:
            template_slide_options = ["Template 1"]
            template_slide = st.selectbox(
                "Choose a template:",
                template_slide_options,
                key=f"container_{container_number}__template",
            )

            key = f"container_{container_number}__title"
            title = st.text_input(
                "Slide Title", key=f"container_{container_number}__title",
            )

            key = f"container_{container_number}__subtitle"
            subtitle = st.text_input(
                "Slide Sub-Title", key=key,
            )

        with col2:
            st.image("./assets/img/template_1_thumbnail.png",
                     use_column_width=True)

        col3, col4 = st.columns([2, 1])

        with col3:
            options = ["Bar Plot", "Line Plot", "Scatter Plot"]
            key = f"container_{container_number}__plot"
            plot = st.selectbox(
                "Choose a plot:",
                options,
                key=key,
            )

            col31, col32, col33 = st.columns(3)
            with col31:
                key = f"container_{container_number}__x_var_"
                x_var = st.text_input(
                    "X-axis Variable", key=key,
                )
            with col32:
                key = f"container_{container_number}__y_var"
                y_var = st.text_input(
                    "Y-axis Variable", key=key,
                )
            with col33:
                key = f"container_{container_number}__hue_var"
                hue_var = st.text_input(
                    "Hue Variable", key=key,
                )

        with col4:
            key = f"container_{container_number}__chart_kargs"
            chart_kargs = st.text_area(
                label="Chart kargs",
                height=200,
                key=f"container_{container_number}__chart_kargs",
            )

        col5, col6 = st.columns([1, 2])
        with col5:
            st.markdown("**Data Preview**")
            data_preview = st.empty()
            if st.session_state.data_preview[container_number] is not None:
                data_preview.write(st.session_state.data_preview[container_number])
        with col6:
            st.markdown("**Chart Preview**")
            chart = st.empty()
            if st.session_state.charts[container_number] is not None:
                chart.pyplot(
                    st.session_state.charts[container_number], use_container_width=True
                )

        if (st.button("Preview", key=f"generate_slide_{container_number}") or \
           st.session_state.trigger_button) and (conn and \
           sql_code and sql_code != "" and sql_code.upper() != "NONE" and \
           has_container_state_changed(container_number)):
            df = dathand.query_db(sql_code, conn)
            fig = viz.plot_data(df, plot, x_var, y_var, hue_var, chart_kargs)

            data_preview.write(df)
            chart.pyplot(fig, use_container_width=True)

            # prs = pptx.Presentation('./assets/pptx/template.pptx')
            # prs = viz.make_slide(prs, template_slide, title, subtitle, fig)
            # prs.save("test.pptx")

            # just update the previous session state at the end to guarantee
            # that no excepetion were raised before
            st.session_state.data_preview[container_number] = df.head(10)
            st.session_state.charts[container_number] = fig
            update_container_state(container_number)
