import streamlit as st
import numpy as np
import pandas as pd
import time


def main():
    # page setting
    st.set_page_config(layout="wide")

    tabs()
    sidebar()


def sidebar():
    # sidebar
    with st.sidebar:

        therm_dis = st.button('Thermal_Charge_Disable',
                              key='therm_dis', use_container_width=True)
        st.session_state.text_suffix = st.text_input('suffix_file_name', "")
        run_ftm = st.button('Run', key='run_ftm', use_container_width=True)

        print(st.session_state)
        try:
            with st.spinner("Running..."):
                if run_ftm:
                    time.sleep(1)
                    # placeholder for the real main function

            st.success("Done!")

        except:
            st.error('Absorted')


def tabs():
    # tabs
    genre_tab, fcc_tab, ce_tab, endc_tab, ulca_tab, cse_tab, rssiscan_tab, apt_tab = st.tabs(
        ['Genre', 'FCC', 'CE', 'ENDC', 'ULCA', 'CSE', 'RSSISCAN', 'APT'])

    with genre_tab:

        # Seperate 3 columns
        col1_m, col2_m, col3_m = st.columns(3)

        # col1_m
        with col1_m:
            col1m_container = col1_m.container()

            # Instrument
            st.session_state['inst_select'] = col1m_container.selectbox(
                'Instrument', ('cmw100',), )

            # Basic items need activating
            if 'genre' not in st.session_state:
                st.session_state['genre'] = col1m_container.checkbox('Genre')
            else:
                pass

            if 'volMipi' not in st.session_state:
                st.session_state['voltMipi'] = col1m_container.checkbox(
                    'VoltMipi')
            else:
                pass

            if 'getTemp' not in st.session_state:
                st.session_state['getTemp'] = col1m_container.checkbox(
                    'GetTemp')
            else:
                pass

            if 'fdcorrect' not in st.session_state:
                st.session_state['fdcorrect'] = col1m_container.checkbox(
                    'FDCorrect')
            else:
                pass

            # horizontal divider
            col1m_container.divider()

            # Tx port setting
            if 'tx_port' not in st.session_state:
                st.session_state['tx_port'] = col1m_container.number_input(
                    'Tx Port', min_value=1, max_value=8, value=1)
            else:
                pass

            if 'port_table' not in st.session_state:
                st.session_state['port_table'] = col1m_container.checkbox(
                    'port table')
            else:
                pass

            # Tx level select except level sweep
            if 'tx_level' not in st.session_state:
                st.session_state['tx_level'] = col1m_container.slider(
                    'Tx level except level sweep', min_value=-40, max_value=30, value=27)
            else:
                pass

            if 'tx_level_sweep_start' not in st.session_state:
                st.session_state['tx_level_sweep_start'] = col1m_container.slider(
                    'Tx level sweep start', min_value=-40, max_value=30, value=-20)
            else:
                pass

            if 'tx_level_sweep_stop' not in st.session_state:
                st.session_state['tx_level_sweep_stop'] = col1m_container.slider(
                    'Tx level sweep stop', min_value=-40, max_value=30, value=27)
            else:
                pass

        with col2_m:
            # text
            st.text('Test Items')
            col2m_container = col2_m.container()

            # Tx LMH
            if 'tx_lmh' not in st.session_state:
                st.session_state['lmh'] = col2m_container.checkbox('Tx_LMH')
            else:
                pass

            # Rx
            if 'rx' not in st.session_state:
                st.session_state['rx'] = col2m_container.checkbox('Rx')
            else:
                pass

            # Rx_quick
            if 'rx_quick' not in st.session_state:
                st.session_state['rx_quick'] = col2m_container.checkbox(
                    'Rx quick')
            else:
                pass

            # Tx level sweep
            if 'tx_level_sweep' not in st.session_state:
                st.session_state['tx_level_sweep'] = col2m_container.checkbox(
                    'Tx level sweep')
            else:
                pass

            # Tx Freq sweep
            if 'tx_freq_sweep' not in st.session_state:
                st.session_state['tx_freq_sweep'] = col2m_container.checkbox(
                    'Tx Freq sweep')
            else:
                pass

            # Tx 1RB sweep
            if 'tx_1rb_sweep' not in st.session_state:
                st.session_state['tx_lrb_sweep'] = col2m_container.checkbox(
                    'Tx 1RB sweep(only for FR1)')
            else:
                pass

            # horizontal divider
            col2m_container.divider()

            # text
            st.text('UE power(only for Rx)')

            # Tx tx_max sweep
            if 'tx_max' not in st.session_state:
                st.session_state['tx_max'] = col2m_container.checkbox('TxMax')
            else:
                pass

            # Tx tx_max sweep
            if 'tx_-10' not in st.session_state:
                st.session_state['tx_-10'] = col2m_container.checkbox('Tx_-10')
            else:
                pass

        with col3_m:
            pass

        # horizontal divider
        st.divider()

    with fcc_tab:
        pass

    with ce_tab:
        pass

    with endc_tab:
        pass

    with ulca_tab:
        pass

    with cse_tab:
        pass

    with rssiscan_tab:
        pass

    with apt_tab:
        pass

    st.write(st.session_state)


if __name__ == "__main__":
    main()
