import streamlit as st
import numpy as np
import pandas as pd
import time
import setting


def sidebar():
    # sidebar
    with st.sidebar:
        # specific key name for sidebar
        specifc_name_sidebar = 'ftm'

        therm_dis = st.button('Thermal_Charge_Disable',
                              key=f'therm_dis_{specifc_name_sidebar}', use_container_width=True)
        text_suffix = st.text_input('suffix_file_name', "", key='text_suffix')
        run_ftm = st.button(
            'Run', key=f'run_{specifc_name_sidebar}', use_container_width=True)

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
    tab_title = {}
    tab_list = ['Genre', 'FCC', 'CE', 'ENDC', 'ULCA', 'CSE', 'RSSISCAN', 'APT']
    genre_tab, fcc_tab, ce_tab, endc_tab, ulca_tab, cse_tab, rssiscan_tab, apt_tab = st.tabs(
        tab_list)

    with genre_tab:
        # specify key name in this page and tab
        specifc_name = 'Genre_ftm'

        # Seperate 3 columns
        col1_m, col2_m, col3_m = st.columns(3)

        # col1_m
        with col1_m:
            # container
            col1m_container = col1_m.container()

            # Instrument
            instrument = col1m_container.selectbox(
                'Instrument', ('cmw100',), key=f'inst_select_{specifc_name}')

            # Basic items need activating
            genre_state = col1m_container.checkbox(
                'Genre_Tab_activated', key=f'activated_{specifc_name}')
            volt_mipi_state = col1m_container.checkbox(
                'VoltMipi', key=f'volt_mipi_{specifc_name}')
            get_temp_state = col1m_container.checkbox(
                'GetTemp', key=f'get_temp_{specifc_name}')
            fd_correct_state = col1m_container.checkbox(
                'FDCorrect', key=f'fd_correct_{specifc_name}')

            # horizontal divider
            col1m_container.divider()

            # Tx port setting
            tx_port = col1m_container.number_input(
                'Tx Port', min_value=1, max_value=8, value=1, key=f'tx_port_{specifc_name}')
            port_table_state = col1m_container.checkbox(
                'port table', key=f'port_table_{specifc_name}')

            # Tx level select except level sweep
            tx_level = col1m_container.slider(
                'Tx level excluding level sweep', min_value=-40, max_value=30, value=27, key=f'tx_level_{specifc_name}')

            # Tx level sweep
            tx_level_sweep_start = col1m_container.slider(
                'Tx level sweep start', min_value=-40, max_value=30, value=-20, key=f'tx_level_sweep_start_{specifc_name}')
            tx_level_sweep_stop = col1m_container.slider(
                'Tx level sweep stop', min_value=-40, max_value=30, value=27, key=f'tx_level_sweep_stop_{specifc_name}')

        with col2_m:
            # container
            col2m_container = col2_m.container()

            # text
            col2m_container.text('Test Items')

            # Tx LMH
            tx_lmh_state = col2m_container.checkbox(
                'Tx LMH', key=f'tx_lmh_{specifc_name}')

            # Rx
            rx_state = col2m_container.checkbox('Rx', key=f'rx_{specifc_name}')

            # Rx_quick
            rx_quick_state = col2m_container.checkbox(
                'Rx Quick', key=f'rx_quick_{specifc_name}')

            # Tx level sweep
            tx_level_sweep_state = col2m_container.checkbox(
                'Tx level sweep', key=f'tx_level_sweep_{specifc_name}')

            # Tx Freq sweep
            tx_freq_sweep_state = col2m_container.checkbox(
                'Tx Freq sweep', key=f'tx_freq_sweep_{specifc_name}')

            # Tx 1RB sweep
            tx_1rb_sweep_state = col2m_container.checkbox(
                'Tx 1RB sweep(only for FR1)', key=f'tx_1rb_sweep_{specifc_name}')

            # horizontal divider
            col2m_container.divider()

            # text
            col2m_container.text('UE power(only for Rx)')

            # Tx tx_max sweep
            tx_max_state = col2m_container.checkbox(
                'TxMax', key=f'tx_max_{specifc_name}', value=rx_ue_power_select(rx_state, rx_quick_state))

            # Tx tx_max sweep
            tx_minus10_state = col2m_container.checkbox(
                'Tx_-10', key=f'tx_-10_{specifc_name}', value=rx_ue_power_select(rx_state, rx_quick_state))

        with col3_m:
            # container
            col3m_container = col3_m.container()

            # text
            col3m_container.text('RATs')

            # FR1
            fr1_state = col3m_container.checkbox(
                'FR1', key=f'fr1_{specifc_name}')

            # LTE
            lte_state = col3m_container.checkbox(
                'LTE', key=f'lte_{specifc_name}')

            # WCDMA
            wcdma_state = col3m_container.checkbox(
                'WCDMA', key=f'wcdma_{specifc_name}')

            # GSM
            fsm_state = col3m_container.checkbox(
                'GSM', key=f'gsm_{specifc_name}')

            # horizontal divider
            col3m_container.divider()

            # text
            col3m_container.text('Channels')

            # L chan
            lch_state = col3m_container.checkbox(
                'L', key=f'lch_{specifc_name}')

            # M chan
            mch_state = col3m_container.checkbox(
                'M', key=f'mch_{specifc_name}')

            # H chan
            hch_state = col3m_container.checkbox(
                'H', key=f'hch_{specifc_name}')

        # horizontal divider
        st.divider()

        # Seperate 3 columns
        col1_path, col2_path, col3_path = st.columns(3)

        with col1_path:
            # container
            col1_path_container = col1_path.container()

            # text
            col1_path_container.text('Tx Path')

            # TX1(Main)
            tx1_state = col1_path_container.checkbox(
                'TX1(Main)', key=f'tx1_path_{specifc_name}')

            # TX2(SUB)
            tx2_state = col1_path_container.checkbox(
                'TX2(Sub)', key=f'tx2_path_{specifc_name}')

            # MIMO
            mimo_state = col1_path_container.checkbox(
                'MIMO', key=f'mimo_path_{specifc_name}')

        with col2_path:
            # container
            col2_path_container = col2_path.container()

            # text
            col2_path_container.text('Rx Path')

            # RX0
            rx0_state = col2_path_container.checkbox(
                'RX0', key=f'rx0_{specifc_name}')

            # RX1
            rx1_state = col2_path_container.checkbox(
                'RX1', key=f'rx1_{specifc_name}')

            # RX2
            rx2_state = col2_path_container.checkbox(
                'RX2', key=f'rx2_{specifc_name}')

            # RX3
            rx3_state = col2_path_container.checkbox(
                'RX3', key=f'rx3_{specifc_name}')

            # RX0+RX1
            rx0rx1_state = col2_path_container.checkbox(
                'RX0RX1', key=f'rx0rx1_{specifc_name}')

            # RX2+RX3
            rx2rx3_state = col2_path_container.checkbox(
                'RX2RX3', key=f'rx2rx3_{specifc_name}')

            # RX0+RX1+RX2+RX3
            rx0rx1rx2rx3_state = col2_path_container.checkbox(
                'RX0RX1RX2RX3', key=f'rx0r1rx2rx3_{specifc_name}')

        with col3_path:
            # container
            col3_path_container = col3_path.container()

            # Sync Path
            sync_path = col3_path_container.selectbox(
                'Sync Path', ('Main', 'CA#1', 'CA#2', 'CA#3'), key=f'sync_path_{specifc_name}')

            # AS path
            as_path = col3_path_container.number_input(
                'AS Path', min_value=0, max_value=1, value=0, key=f'as_path_{specifc_name}')
            as_path_enable_state = col3_path_container.checkbox(
                'AS enable', key=f'as_path_eable_{specifc_name}')

            # SRS path
            srs_path = col3_path_container.number_input(
                'SRS Path', min_value=0, max_value=3, value=0, key=f'srs_path_{specifc_name}')
            srs_path_enable_state = col3_path_container.checkbox(
                'SRS enable', key=f'srs_path_eable_{specifc_name}')

            # freq sweep steps
            freq_sweep_step = col3_path_container.text_input(
                'Tx_Freq_Sweep_Step(KHz) only for FR1 and LTE', value=1000, key=f'freq_step_{specifc_name}')

            # freq sweep start
            freq_sweep_start = col3_path_container.text_input(
                'Tx_Freq_Sweep_Start(KHz) only for FR1 and LTE', value=0, key=f'freq_start_{specifc_name}')

            # freq sweep stop
            freq_sweep_stop = col3_path_container.text_input(
                'Tx_Freq_Sweep_Start(KHz) only for FR1 and LTE', value=0, key=f'freq_stop_{specifc_name}')

        # horizontal divider
        st.divider()

        # container for FR1
        fr1_container = st.container()

        # subheader
        fr1_container.subheader('FR1')

        # Seperate 4 columns
        col1_bw, col2_mcs, col3_type, col4_rb = fr1_container.columns(4)

        with col1_bw:
            # container
            col1_bw_fr1 = col1_bw.container()

            # text
            col1_bw_fr1.text('BW')

            # bw_fr1
            bw5_fr1_state = col1_bw_fr1.checkbox(
                '5MHz', key=f'bw5_fr1_{specifc_name}')
            bw10_fr1_state = col1_bw_fr1.checkbox(
                '10MHz', key=f'bw10_fr1_{specifc_name}')
            bw15_fr1_state = col1_bw_fr1.checkbox(
                '15MHz', key=f'bw15_fr1_{specifc_name}')
            bw20_fr1_state = col1_bw_fr1.checkbox(
                '20MHz', key=f'bw20_fr1_{specifc_name}')
            bw25_fr1_state = col1_bw_fr1.checkbox(
                '25MHz', key=f'bw25_fr1_{specifc_name}')
            bw30_fr1_state = col1_bw_fr1.checkbox(
                '30MHz', key=f'bw30_fr1_{specifc_name}')
            bw40_fr1_state = col1_bw_fr1.checkbox(
                '40MHz', key=f'bw40_fr1_{specifc_name}')
            bw50_fr1_state = col1_bw_fr1.checkbox(
                '50MHz', key=f'bw50_fr1_{specifc_name}')
            bw60_fr1_state = col1_bw_fr1.checkbox(
                '60MHz', key=f'bw60_fr1_{specifc_name}')
            bw70_fr1_state = col1_bw_fr1.checkbox(
                '70MHz', key=f'bw70_fr1_{specifc_name}')
            bw80_fr1_state = col1_bw_fr1.checkbox(
                '80MHz', key=f'bw80_fr1_{specifc_name}')
            bw90_fr1_state = col1_bw_fr1.checkbox(
                '90MHz', key=f'bw90_fr1_{specifc_name}')
            bw100_fr1_state = col1_bw_fr1.checkbox(
                '100MHz', key=f'bw100_fr1_{specifc_name}')

        with col2_mcs:
            # container
            col2_mcs_fr1 = col2_mcs.container()

            # text
            col2_mcs_fr1.text('MCS')

            # mcs_fr1
            qpsk_fr1_state = col2_mcs_fr1.checkbox(
                'QPSK', key=f'qpdk_fr1_{specifc_name}')
            q16_fr1_state = col2_mcs_fr1.checkbox(
                'Q16', key=f'q16_fr1_{specifc_name}')
            q64_fr1_state = col2_mcs_fr1.checkbox(
                'Q64', key=f'q64_fr1_{specifc_name}')
            q256_fr1_state = col2_mcs_fr1.checkbox(
                'Q256', key=f'q256_fr1_{specifc_name}')
            bpsk_fr1_state = col2_mcs_fr1.checkbox(
                'BPSK', key=f'bpsk_fr1_{specifc_name}')

        with col3_type:
            # container
            col3_type_fr1 = col3_type.container()

            # text
            col3_type_fr1.text('TYPE')

            # mcs_fr1
            dfts_fr1_state = col3_type_fr1.checkbox(
                'DFTS', key=f'dfts_fr1_{specifc_name}')
            cp_fr1_state = col3_type_fr1.checkbox(
                'CP', key=f'cp_fr1_{specifc_name}')

        with col4_rb:
            # container
            col4_rb_fr1 = col4_rb.container()

            # text
            col4_rb_fr1.text('RB SETTING')

            # mcs_fr1
            inner_full_fr1_state = col4_rb_fr1.checkbox(
                'INNER_FULL', key=f'inner_full_fr1_{specifc_name}')
            outer_full_fr1_state = col4_rb_fr1.checkbox(
                'OUTER_FULL', key=f'outer_full_fr1_{specifc_name}')
            inner_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_LEFT', key=f'inner_1rb_left_fr1_{specifc_name}')
            inner_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_RIGHT', key=f'inner_1rb_right_fr1_{specifc_name}')
            edge_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_LEFT', key=f'edge_1rb_left_fr1_{specifc_name}')
            edge_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_RIGHT', key=f'edge_1rb_right_fr1_{specifc_name}')
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_LEFT', key=f'edge_full_left_fr1_{specifc_name}')
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_RIGHT', key=f'edge_full_right_fr1_{specifc_name}')

        # horizontal divider
        fr1_container.divider()
        fr1_container.subheader('FR1')

        col1_lb, col2_mhb, col3_uhb = fr1_container.columns(3)

        with col1_lb:
            # container
            col1_lb_fr1 = col1_lb.container()

            # text
            col1_lb_fr1.text('LB')

            # LB
            lb_all_fr1_state = col1_lb_fr1.checkbox(
                'LB_ALL', key=f'lb_all_fr1_{specifc_name}')
            b5_fr1_state = col1_lb_fr1.checkbox(
                'N5', key=f'b5_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b8_fr1_state = col1_lb_fr1.checkbox(
                'N8', key=f'b8_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b12_fr1_state = col1_lb_fr1.checkbox(
                'N12', key=f'b12_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b13_fr1_state = col1_lb_fr1.checkbox(
                'N13', key=f'b13_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b14_fr1_state = col1_lb_fr1.checkbox(
                'N14', key=f'b14_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b20_fr1_state = col1_lb_fr1.checkbox(
                'N20', key=f'b20_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b24_fr1_state = col1_lb_fr1.checkbox(
                'N24', key=f'b24_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b26_fr1_state = col1_lb_fr1.checkbox(
                'N26', key=f'b26_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28a_fr1_state = col1_lb_fr1.checkbox(
                'N28A', key=f'b28a_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28b_fr1_state = col1_lb_fr1.checkbox(
                'N28B', key=f'b28b_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b29_fr1_state = col1_lb_fr1.checkbox(
                'N29', key=f'b29_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b32_fr1_state = col1_lb_fr1.checkbox(
                'N32', key=f'b32_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b71_fr1_state = col1_lb_fr1.checkbox(
                'N71', key=f'b71_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])

        with col2_mhb:
            # container
            col2_mhb_fr1 = col2_mhb.container()

            # text
            col2_mhb_fr1.text('MHB')

            # MHB
            mhb_all_fr1_state = col2_mhb_fr1.checkbox(
                'MHB_ALL', key=f'mhb_all_fr1_{specifc_name}')
            b1_fr1_state = col2_mhb_fr1.checkbox(
                'N1', key=f'b1_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b2_fr1_state = col2_mhb_fr1.checkbox(
                'N2', key=f'b2_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b3_fr1_state = col2_mhb_fr1.checkbox(
                'N3', key=f'b3_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b7_fr1_state = col2_mhb_fr1.checkbox(
                'N7', key=f'b7_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b30_fr1_state = col2_mhb_fr1.checkbox(
                'N30', key=f'b30_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b25_fr1_state = col2_mhb_fr1.checkbox(
                'N25', key=f'b25_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b66_fr1_state = col2_mhb_fr1.checkbox(
                'N66', key=f'b66_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b70_fr1_state = col2_mhb_fr1.checkbox(
                'N70', key=f'b70_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b40_fr1_state = col2_mhb_fr1.checkbox(
                'N40', key=f'b40_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b38_fr1_state = col2_mhb_fr1.checkbox(
                'N38', key=f'b38_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b41_fr1_state = col2_mhb_fr1.checkbox(
                'N41', key=f'b41_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b34_fr1_state = col2_mhb_fr1.checkbox(
                'N34', key=f'b34_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b75_fr1_state = col2_mhb_fr1.checkbox(
                'N75', key=f'b75_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b76_fr1_state = col2_mhb_fr1.checkbox(
                'N76', key=f'b76_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b255_fr1_state = col2_mhb_fr1.checkbox(
                'N255', key=f'b255_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b256_fr1_state = col2_mhb_fr1.checkbox(
                'N256', key=f'b256_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])

        with col3_uhb:
            # container
            col3_uhb_fr1 = col3_uhb.container()

            # text
            col3_uhb_fr1.text('UHB')

            # UHB
            uhb_all_fr1_state = col3_uhb_fr1.checkbox(
                'UHB_ALL', key=f'uhb_all_fr1_{specifc_name}')
            b48_fr1_state = col3_uhb_fr1.checkbox(
                'N48', key=f'b48_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b77_fr1_state = col3_uhb_fr1.checkbox(
                'N77', key=f'b77_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b78_fr1_state = col3_uhb_fr1.checkbox(
                'N78', key=f'b78_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b79_fr1_state = col3_uhb_fr1.checkbox(
                'N79', key=f'b79_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])

        # horizontal divider
        st.divider()

        # container for LTE
        lte_container = st.container()

        # subheader
        lte_container.subheader('LTE')

        # Seperate 4 columns
        col1_bw, col2_mcs, col3_rb = lte_container.columns(3)

        with col1_bw:
            # container
            col1_bw_lte = col1_bw.container()

            # text
            col1_bw_lte.text('BW')

            # bw_lte
            bw1p4_lte_state = col1_bw_lte.checkbox(
                '1.4MHz', key=f'bw1p4_lte_{specifc_name}')
            bw3_lte_state = col1_bw_lte.checkbox(
                '3MHz', key=f'bw3_lte_{specifc_name}')
            bw5_lte_state = col1_bw_lte.checkbox(
                '5MHz', key=f'bw5_lte_{specifc_name}')
            bw10_lte_state = col1_bw_lte.checkbox(
                '10MHz', key=f'bw10_lte_{specifc_name}')
            bw15_lte_state = col1_bw_lte.checkbox(
                '15MHz', key=f'bw15_lte_{specifc_name}')
            bw20_lte_state = col1_bw_lte.checkbox(
                '20MHz', key=f'bw20_lte_{specifc_name}')

        with col2_mcs:
            # container
            col2_mcs_lte = col2_mcs.container()

            # text
            col2_mcs_lte.text('MCS')

            # mcs_lte
            qpsk_lte_state = col2_mcs_lte.checkbox(
                'QPSK', key=f'qpdk_lte_{specifc_name}')
            q16_lte_state = col2_mcs_lte.checkbox(
                'Q16', key=f'q16_lte_{specifc_name}')
            q64_lte_state = col2_mcs_lte.checkbox(
                'Q64', key=f'q64_lte_{specifc_name}')
            q256_lte_state = col2_mcs_lte.checkbox(
                'Q256', key=f'q256_lte_{specifc_name}')

        with col3_rb:
            # container
            col3_rb_lte = col3_rb.container()

            # text
            col3_rb_lte.text('RB SETTING')

            # mcs_lte
            prb_lte_state = col3_rb_lte.checkbox(
                'PRB', key=f'prb_lte_{specifc_name}')
            frb_lte_state = col3_rb_lte.checkbox(
                'FRB', key=f'frb_lte_{specifc_name}')
            one_rb_0_lte_state = col3_rb_lte.checkbox(
                '1RB_0', key=f'one_rb_0_lte_{specifc_name}')
            one_rb_max_lte_state = col3_rb_lte.checkbox(
                '1RB_MAX', key=f'one_rb_max_lte_{specifc_name}')

        # horizontal divider
        lte_container.divider()
        lte_container.subheader('LTE')

        col1_lb, col2_mhb, col3_uhb = lte_container.columns(3)

        with col1_lb:
            # container
            col1_lb_lte = col1_lb.container()

            # text
            col1_lb_lte.text('LB')

            # LB
            lb_all_lte_state = col1_lb_lte.checkbox(
                'LB_ALL', key=f'lb_all_lte_{specifc_name}')
            b5_lte_state = col1_lb_lte.checkbox(
                'L5', key=f'b5_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b8_lte_state = col1_lb_lte.checkbox(
                'L8', key=f'b8_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b12_lte_state = col1_lb_lte.checkbox(
                'L12', key=f'b12_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b13_lte_state = col1_lb_lte.checkbox(
                'L13', key=f'b13_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b14_lte_state = col1_lb_lte.checkbox(
                'L14', key=f'b14_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b17_lte_state = col1_lb_lte.checkbox(
                'L17', key=f'b17_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b18_lte_state = col1_lb_lte.checkbox(
                'L18', key=f'b18_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b19_lte_state = col1_lb_lte.checkbox(
                'L19', key=f'b19_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b20_lte_state = col1_lb_lte.checkbox(
                'L20', key=f'b20_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b24_lte_state = col1_lb_lte.checkbox(
                'L24', key=f'b24_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b26_lte_state = col1_lb_lte.checkbox(
                'L26', key=f'b26_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b28a_lte_state = col1_lb_lte.checkbox(
                'L28A', key=f'b28a_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b28b_lte_state = col1_lb_lte.checkbox(
                'L28B', key=f'b28b_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b29_lte_state = col1_lb_lte.checkbox(
                'L29', key=f'b29_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b32_lte_state = col1_lb_lte.checkbox(
                'L32', key=f'b32_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b71_lte_state = col1_lb_lte.checkbox(
                'L71', key=f'b71_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])

        with col2_mhb:
            # container
            col2_mhb_lte = col2_mhb.container()

            # text
            col2_mhb_lte.text('MHB')

            # MHB
            mhb_all_lte_state = col2_mhb_lte.checkbox(
                'MHB_ALL', key=f'mhb_all_lte_{specifc_name}')
            b1_lte_state = col2_mhb_lte.checkbox(
                'L1', key=f'b1_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b2_lte_state = col2_mhb_lte.checkbox(
                'L2', key=f'b2_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b3_lte_state = col2_mhb_lte.checkbox(
                'L3', key=f'b3_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b7_lte_state = col2_mhb_lte.checkbox(
                'L7', key=f'b7_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b30_lte_state = col2_mhb_lte.checkbox(
                'L30', key=f'b30_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b25_lte_state = col2_mhb_lte.checkbox(
                'L25', key=f'b25_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b66_lte_state = col2_mhb_lte.checkbox(
                'L66', key=f'b66_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b70_lte_state = col2_mhb_lte.checkbox(
                'L70', key=f'b70_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b39_lte_state = col2_mhb_lte.checkbox(
                'L39', key=f'b39_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b40_lte_state = col2_mhb_lte.checkbox(
                'L40', key=f'b40_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b38_lte_state = col2_mhb_lte.checkbox(
                'L38', key=f'b38_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b41_lte_state = col2_mhb_lte.checkbox(
                'L41', key=f'b41_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b23_lte_state = col2_mhb_lte.checkbox(
                'L23', key=f'b23_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b34_lte_state = col2_mhb_lte.checkbox(
                'L34', key=f'b34_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b75_lte_state = col2_mhb_lte.checkbox(
                'L75', key=f'b75_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b76_lte_state = col2_mhb_lte.checkbox(
                'L76', key=f'b76_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])

        with col3_uhb:
            # container
            col3_uhb_lte = col3_uhb.container()

            # text
            col3_uhb_lte.text('UHB')

            # UHB
            uhb_all_lte_state = col3_uhb_lte.checkbox(
                'UHB_ALL', key=f'uhb_all_lte_{specifc_name}')
            b42_lte_state = col3_uhb_lte.checkbox(
                'L42', key=f'b42_lte_{specifc_name}', value=st.session_state[f'uhb_all_lte_{specifc_name}'])
            b48_lte_state = col3_uhb_lte.checkbox(
                'L48', key=f'b48_lte_{specifc_name}', value=st.session_state[f'uhb_all_lte_{specifc_name}'])

    with fcc_tab:
        # specify key name in this page and tab
        specifc_name = 'FCC_ftm'

        # Seperate 3 columns
        col1_m, col2_m, col3_m = st.columns(3)

        # col1_m
        with col1_m:
            # container
            col1m_container = col1_m.container()

            # Instrument
            instrument = col1m_container.selectbox(
                'Instrument', ('cmw100',), key=f'inst_select_{specifc_name}')

            # Basic items need activating
            fcc_state = col1m_container.checkbox(
                'FCC_Tab_activated', key=f'activated_{specifc_name}')
            volt_mipi_state = col1m_container.checkbox(
                'VoltMipi', key=f'volt_mipi_{specifc_name}', disabled=True)
            get_temp_state = col1m_container.checkbox(
                'GetTemp', key=f'get_temp_{specifc_name}', disabled=True)
            fd_correct_state = col1m_container.checkbox(
                'FDCorrect', key=f'fd_correct_{specifc_name}')

            # horizontal divider
            col1m_container.divider()

            # Tx port setting
            tx_port = col1m_container.number_input(
                'Tx Port', min_value=1, max_value=8, value=1, key=f'tx_port_{specifc_name}')
            port_table_state = col1m_container.checkbox(
                'port table', key=f'port_table_{specifc_name}')

            # Tx level select except level sweep
            tx_level = col1m_container.slider(
                'Tx level excluding level sweep', min_value=-40, max_value=30, value=27, key=f'tx_level_{specifc_name}')

            # Tx level sweep
            tx_level_sweep_start = col1m_container.slider(
                'Tx level sweep start', min_value=-40, max_value=30, value=-20, key=f'tx_level_sweep_start_{specifc_name}', disabled=True)
            tx_level_sweep_stop = col1m_container.slider(
                'Tx level sweep stop', min_value=-40, max_value=30, value=27, key=f'tx_level_sweep_stop_{specifc_name}', disabled=True)

        with col2_m:
            # container
            col2m_container = col2_m.container()

            # text
            col2m_container.text('Test Items')

            # Tx LMH
            tx_lmh_state = col2m_container.checkbox(
                'Tx LMH', key=f'tx_lmh_{specifc_name}')

            # Rx
            rx_state = col2m_container.checkbox(
                'Rx', key=f'rx_{specifc_name}', disabled=True)

            # Rx_quick
            rx_quick_state = col2m_container.checkbox(
                'Rx Quick', key=f'rx_quick_{specifc_name}', disabled=True)

            # Tx level sweep
            tx_level_sweep_state = col2m_container.checkbox(
                'Tx level sweep', key=f'tx_level_sweep_{specifc_name}', disabled=True)

            # Tx Freq sweep
            tx_freq_sweep_state = col2m_container.checkbox(
                'Tx Freq sweep', key=f'tx_freq_sweep_{specifc_name}', disabled=True)

            # Tx 1RB sweep
            tx_1rb_sweep_state = col2m_container.checkbox(
                'Tx 1RB sweep(only for FR1)', key=f'tx_1rb_sweep_{specifc_name}', disabled=True)

            # horizontal divider
            col2m_container.divider()

            # text
            col2m_container.text('UE power(only for Rx)')

            # Tx tx_max sweep
            tx_max_state = col2m_container.checkbox(
                'TxMax', key=f'tx_max_{specifc_name}', value=rx_ue_power_select(rx_state, rx_quick_state), disabled=True)

            # Tx tx_max sweep
            tx_minus10_state = col2m_container.checkbox(
                'Tx_-10', key=f'tx_-10_{specifc_name}', value=rx_ue_power_select(rx_state, rx_quick_state), disabled=True)

        with col3_m:
            # container
            col3m_container = col3_m.container()

            # text
            col3m_container.text('RATs')

            # FR1
            fr1_state = col3m_container.checkbox(
                'FR1', key=f'fr1_{specifc_name}')

            # LTE
            lte_state = col3m_container.checkbox(
                'LTE', key=f'lte_{specifc_name}', disabled=True)

            # WCDMA
            wcdma_state = col3m_container.checkbox(
                'WCDMA', key=f'wcdma_{specifc_name}', disabled=True)

            # GSM
            fsm_state = col3m_container.checkbox(
                'GSM', key=f'gsm_{specifc_name}', disabled=True)

            # horizontal divider
            col3m_container.divider()

            # text
            col3m_container.text('Channels')

            # L chan
            lch_state = col3m_container.checkbox(
                'L', key=f'lch_{specifc_name}', disabled=True)

            # M chan
            mch_state = col3m_container.checkbox(
                'M', key=f'mch_{specifc_name}', disabled=True)

            # H chan
            hch_state = col3m_container.checkbox(
                'H', key=f'hch_{specifc_name}', disabled=True)

        # horizontal divider
        st.divider()

        # Seperate 3 columns
        col1_path, col2_path, col3_path = st.columns(3)

        with col1_path:
            # container
            col1_path_container = col1_path.container()

            # text
            col1_path_container.text('Tx Path')

            # TX1(Main)
            tx1_state = col1_path_container.checkbox(
                'TX1(Main)', key=f'tx1_path_{specifc_name}')

            # TX2(SUB)
            tx2_state = col1_path_container.checkbox(
                'TX2(Sub)', key=f'tx2_path_{specifc_name}')

            # MIMO
            mimo_state = col1_path_container.checkbox(
                'MIMO', key=f'mimo_path_{specifc_name}')

        with col2_path:
            # container
            col2_path_container = col2_path.container()

            # text
            col2_path_container.text('Rx Path')

            # RX0
            rx0_state = col2_path_container.checkbox(
                'RX0', key=f'rx0_{specifc_name}', disabled=True)

            # RX1
            rx1_state = col2_path_container.checkbox(
                'RX1', key=f'rx1_{specifc_name}', disabled=True)

            # RX2
            rx2_state = col2_path_container.checkbox(
                'RX2', key=f'rx2_{specifc_name}', disabled=True)

            # RX3
            rx3_state = col2_path_container.checkbox(
                'RX3', key=f'rx3_{specifc_name}', disabled=True)

            # RX0+RX1
            rx0rx1_state = col2_path_container.checkbox(
                'RX0RX1', key=f'rx0rx1_{specifc_name}', disabled=True)

            # RX2+RX3
            rx2rx3_state = col2_path_container.checkbox(
                'RX2RX3', key=f'rx2rx3_{specifc_name}', disabled=True)

            # RX0+RX1+RX2+RX3
            rx0rx1rx2rx3_state = col2_path_container.checkbox(
                'RX0RX1RX2RX3', key=f'rx0r1rx2rx3_{specifc_name}', disabled=True)

        with col3_path:
            # container
            col3_path_container = col3_path.container()

            # Sync Path
            sync_path = col3_path_container.selectbox(
                'Sync Path', ('Main', 'CA#1', 'CA#2', 'CA#3'), key=f'sync_path_{specifc_name}')

            # AS path
            as_path = col3_path_container.number_input(
                'AS Path', min_value=0, max_value=1, value=0, key=f'as_path_{specifc_name}')
            as_path_enable_state = col3_path_container.checkbox(
                'AS enable', key=f'as_path_eable_{specifc_name}')

            # SRS path
            srs_path = col3_path_container.number_input(
                'SRS Path', min_value=0, max_value=3, value=0, key=f'srs_path_{specifc_name}')
            srs_path_enable_state = col3_path_container.checkbox(
                'SRS enable', key=f'srs_path_eable_{specifc_name}')

        # horizontal divider
        st.divider()

        # container for FR1
        fr1_container = st.container()

        # subheader
        fr1_container.subheader('FR1')

        # Seperate 4 columns
        col1_bw, col2_mcs, col3_type, col4_rb = fr1_container.columns(4)

        with col1_bw:
            # container
            col1_bw_fr1 = col1_bw.container()

            # text
            col1_bw_fr1.text('BW')

            # bw_fr1
            bw5_fr1_state = col1_bw_fr1.checkbox(
                '5MHz', key=f'bw5_fr1_{specifc_name}')
            bw10_fr1_state = col1_bw_fr1.checkbox(
                '10MHz', key=f'bw10_fr1_{specifc_name}')
            bw15_fr1_state = col1_bw_fr1.checkbox(
                '15MHz', key=f'bw15_fr1_{specifc_name}')
            bw20_fr1_state = col1_bw_fr1.checkbox(
                '20MHz', key=f'bw20_fr1_{specifc_name}')
            bw25_fr1_state = col1_bw_fr1.checkbox(
                '25MHz', key=f'bw25_fr1_{specifc_name}')
            bw30_fr1_state = col1_bw_fr1.checkbox(
                '30MHz', key=f'bw30_fr1_{specifc_name}')
            bw40_fr1_state = col1_bw_fr1.checkbox(
                '40MHz', key=f'bw40_fr1_{specifc_name}')
            bw50_fr1_state = col1_bw_fr1.checkbox(
                '50MHz', key=f'bw50_fr1_{specifc_name}')
            bw60_fr1_state = col1_bw_fr1.checkbox(
                '60MHz', key=f'bw60_fr1_{specifc_name}')
            bw70_fr1_state = col1_bw_fr1.checkbox(
                '70MHz', key=f'bw70_fr1_{specifc_name}')
            bw80_fr1_state = col1_bw_fr1.checkbox(
                '80MHz', key=f'bw80_fr1_{specifc_name}')
            bw90_fr1_state = col1_bw_fr1.checkbox(
                '90MHz', key=f'bw90_fr1_{specifc_name}')
            bw100_fr1_state = col1_bw_fr1.checkbox(
                '100MHz', key=f'bw100_fr1_{specifc_name}')

        with col2_mcs:
            # container
            col2_mcs_fr1 = col2_mcs.container()

            # text
            col2_mcs_fr1.text('MCS')

            # mcs_fr1
            qpsk_fr1_state = col2_mcs_fr1.checkbox(
                'QPSK', key=f'qpdk_fr1_{specifc_name}')
            q16_fr1_state = col2_mcs_fr1.checkbox(
                'Q16', key=f'q16_fr1_{specifc_name}')
            q64_fr1_state = col2_mcs_fr1.checkbox(
                'Q64', key=f'q64_fr1_{specifc_name}')
            q256_fr1_state = col2_mcs_fr1.checkbox(
                'Q256', key=f'q256_fr1_{specifc_name}')
            bpsk_fr1_state = col2_mcs_fr1.checkbox(
                'BPSK', key=f'bpsk_fr1_{specifc_name}')

        with col3_type:
            # container
            col3_type_fr1 = col3_type.container()

            # text
            col3_type_fr1.text('TYPE')

            # mcs_fr1
            dfts_fr1_state = col3_type_fr1.checkbox(
                'DFTS', key=f'dfts_fr1_{specifc_name}')
            cp_fr1_state = col3_type_fr1.checkbox(
                'CP', key=f'cp_fr1_{specifc_name}')

        with col4_rb:
            # container
            col4_rb_fr1 = col4_rb.container()

            # text
            col4_rb_fr1.text('RB SETTING')

            # mcs_fr1
            inner_full_fr1_state = col4_rb_fr1.checkbox(
                'INNER_FULL', key=f'inner_full_fr1_{specifc_name}', disabled=True)
            outer_full_fr1_state = col4_rb_fr1.checkbox(
                'OUTER_FULL', key=f'outer_full_fr1_{specifc_name}', disabled=True)
            inner_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_LEFT', key=f'inner_1rb_left_fr1_{specifc_name}', disabled=True)
            inner_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_RIGHT', key=f'inner_1rb_right_fr1_{specifc_name}', disabled=True)
            edge_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_LEFT', key=f'edge_1rb_left_fr1_{specifc_name}', disabled=True)
            edge_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_RIGHT', key=f'edge_1rb_right_fr1_{specifc_name}', disabled=True)
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_LEFT', key=f'edge_full_left_fr1_{specifc_name}', disabled=True)
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_RIGHT', key=f'edge_full_right_fr1_{specifc_name}', disabled=True)

        # horizontal divider
        fr1_container.divider()
        fr1_container.subheader('FR1')

        col1_lb, col2_mhb, col3_uhb = fr1_container.columns(3)

        with col1_lb:
            # container
            col1_lb_fr1 = col1_lb.container()

            # text
            col1_lb_fr1.text('LB')

            # LB
            lb_all_fr1_state = col1_lb_fr1.checkbox(
                'LB_ALL', key=f'lb_all_fr1_{specifc_name}')
            b5_fr1_state = col1_lb_fr1.checkbox(
                'N5', key=f'b5_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b8_fr1_state = col1_lb_fr1.checkbox(
                'N8', key=f'b8_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b12_fr1_state = col1_lb_fr1.checkbox(
                'N12', key=f'b12_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b13_fr1_state = col1_lb_fr1.checkbox(
                'N13', key=f'b13_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b14_fr1_state = col1_lb_fr1.checkbox(
                'N14', key=f'b14_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b20_fr1_state = col1_lb_fr1.checkbox(
                'N20', key=f'b20_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b24_fr1_state = col1_lb_fr1.checkbox(
                'N24', key=f'b24_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b26_fr1_state = col1_lb_fr1.checkbox(
                'N26', key=f'b26_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28a_fr1_state = col1_lb_fr1.checkbox(
                'N28A', key=f'b28a_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28b_fr1_state = col1_lb_fr1.checkbox(
                'N28B', key=f'b28b_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b29_fr1_state = col1_lb_fr1.checkbox(
                'N29', key=f'b29_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b32_fr1_state = col1_lb_fr1.checkbox(
                'N32', key=f'b32_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b71_fr1_state = col1_lb_fr1.checkbox(
                'N71', key=f'b71_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])

        with col2_mhb:
            # container
            col2_mhb_fr1 = col2_mhb.container()

            # text
            col2_mhb_fr1.text('MHB')

            # MHB
            mhb_all_fr1_state = col2_mhb_fr1.checkbox(
                'MHB_ALL', key=f'mhb_all_fr1_{specifc_name}')
            b1_fr1_state = col2_mhb_fr1.checkbox(
                'N1', key=f'b1_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b2_fr1_state = col2_mhb_fr1.checkbox(
                'N2', key=f'b2_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b3_fr1_state = col2_mhb_fr1.checkbox(
                'N3', key=f'b3_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b7_fr1_state = col2_mhb_fr1.checkbox(
                'N7', key=f'b7_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b30_fr1_state = col2_mhb_fr1.checkbox(
                'N30', key=f'b30_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b25_fr1_state = col2_mhb_fr1.checkbox(
                'N25', key=f'b25_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b66_fr1_state = col2_mhb_fr1.checkbox(
                'N66', key=f'b66_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b70_fr1_state = col2_mhb_fr1.checkbox(
                'N70', key=f'b70_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b40_fr1_state = col2_mhb_fr1.checkbox(
                'N40', key=f'b40_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b38_fr1_state = col2_mhb_fr1.checkbox(
                'N38', key=f'b38_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b41_fr1_state = col2_mhb_fr1.checkbox(
                'N41', key=f'b41_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b34_fr1_state = col2_mhb_fr1.checkbox(
                'N34', key=f'b34_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b75_fr1_state = col2_mhb_fr1.checkbox(
                'N75', key=f'b75_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b76_fr1_state = col2_mhb_fr1.checkbox(
                'N76', key=f'b76_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b255_fr1_state = col2_mhb_fr1.checkbox(
                'N255', key=f'b255_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b256_fr1_state = col2_mhb_fr1.checkbox(
                'N256', key=f'b256_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])

        with col3_uhb:
            # container
            col3_uhb_fr1 = col3_uhb.container()

            # text
            col3_uhb_fr1.text('UHB')

            # UHB
            uhb_all_fr1_state = col3_uhb_fr1.checkbox(
                'UHB_ALL', key=f'uhb_all_fr1_{specifc_name}')
            b48_fr1_state = col3_uhb_fr1.checkbox(
                'N48', key=f'b48_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b77_fr1_state = col3_uhb_fr1.checkbox(
                'N77', key=f'b77_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b78_fr1_state = col3_uhb_fr1.checkbox(
                'N78', key=f'b78_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b79_fr1_state = col3_uhb_fr1.checkbox(
                'N79', key=f'b79_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])

    with ce_tab:
        # specify key name in this page and tab
        specifc_name = 'CE_ftm'

        # Seperate 3 columns
        col1_m, col2_m, col3_m = st.columns(3)

        # col1_m
        with col1_m:
            # container
            col1m_container = col1_m.container()

            # Instrument
            instrument = col1m_container.selectbox(
                'Instrument', ('cmw100',), key=f'inst_select_{specifc_name}')

            # Basic items need activating
            fcc_state = col1m_container.checkbox(
                'CE_Tab_activated', key=f'activated_{specifc_name}')
            volt_mipi_state = col1m_container.checkbox(
                'VoltMipi', key=f'volt_mipi_{specifc_name}', disabled=True)
            get_temp_state = col1m_container.checkbox(
                'GetTemp', key=f'get_temp_{specifc_name}', disabled=True)
            fd_correct_state = col1m_container.checkbox(
                'FDCorrect', key=f'fd_correct_{specifc_name}')

            # horizontal divider
            col1m_container.divider()

            # Tx port setting
            tx_port = col1m_container.number_input(
                'Tx Port', min_value=1, max_value=8, value=1, key=f'tx_port_{specifc_name}')
            port_table_state = col1m_container.checkbox(
                'port table', key=f'port_table_{specifc_name}')

            # Tx level select except level sweep
            tx_level = col1m_container.slider(
                'Tx level excluding level sweep', min_value=-40, max_value=30, value=27, key=f'tx_level_{specifc_name}')

            # Tx level sweep
            tx_level_sweep_start = col1m_container.slider(
                'Tx level sweep start', min_value=-40, max_value=30, value=-20, key=f'tx_level_sweep_start_{specifc_name}', disabled=True)
            tx_level_sweep_stop = col1m_container.slider(
                'Tx level sweep stop', min_value=-40, max_value=30, value=27, key=f'tx_level_sweep_stop_{specifc_name}', disabled=True)

        with col2_m:
            # container
            col2m_container = col2_m.container()

            # text
            col2m_container.text('Test Items')

            # Tx LMH
            tx_lmh_state = col2m_container.checkbox(
                'Tx LMH', key=f'tx_lmh_{specifc_name}')

            # Rx
            rx_state = col2m_container.checkbox(
                'Rx', key=f'rx_{specifc_name}', disabled=True)

            # Rx_quick
            rx_quick_state = col2m_container.checkbox(
                'Rx Quick', key=f'rx_quick_{specifc_name}', disabled=True)

            # Tx level sweep
            tx_level_sweep_state = col2m_container.checkbox(
                'Tx level sweep', key=f'tx_level_sweep_{specifc_name}', disabled=True)

            # Tx Freq sweep
            tx_freq_sweep_state = col2m_container.checkbox(
                'Tx Freq sweep', key=f'tx_freq_sweep_{specifc_name}', disabled=True)

            # Tx 1RB sweep
            tx_1rb_sweep_state = col2m_container.checkbox(
                'Tx 1RB sweep(only for FR1)', key=f'tx_1rb_sweep_{specifc_name}', disabled=True)

            # horizontal divider
            col2m_container.divider()

            # text
            col2m_container.text('UE power(only for Rx)')

            # Tx tx_max sweep
            tx_max_state = col2m_container.checkbox(
                'TxMax', key=f'tx_max_{specifc_name}', value=rx_ue_power_select(rx_state, rx_quick_state), disabled=True)

            # Tx tx_max sweep
            tx_minus10_state = col2m_container.checkbox(
                'Tx_-10', key=f'tx_-10_{specifc_name}', value=rx_ue_power_select(rx_state, rx_quick_state), disabled=True)

        with col3_m:
            # container
            col3m_container = col3_m.container()

            # text
            col3m_container.text('RATs')

            # FR1
            fr1_state = col3m_container.checkbox(
                'FR1', key=f'fr1_{specifc_name}')

            # LTE
            lte_state = col3m_container.checkbox(
                'LTE', key=f'lte_{specifc_name}', disabled=True)

            # WCDMA
            wcdma_state = col3m_container.checkbox(
                'WCDMA', key=f'wcdma_{specifc_name}', disabled=True)

            # GSM
            fsm_state = col3m_container.checkbox(
                'GSM', key=f'gsm_{specifc_name}', disabled=True)

            # horizontal divider
            col3m_container.divider()

            # text
            col3m_container.text('Channels')

            # L chan
            lch_state = col3m_container.checkbox(
                'L', key=f'lch_{specifc_name}', disabled=True)

            # M chan
            mch_state = col3m_container.checkbox(
                'M', key=f'mch_{specifc_name}', disabled=True)

            # H chan
            hch_state = col3m_container.checkbox(
                'H', key=f'hch_{specifc_name}', disabled=True)

        # horizontal divider
        st.divider()

        # Seperate 3 columns
        col1_path, col2_path, col3_path = st.columns(3)

        with col1_path:
            # container
            col1_path_container = col1_path.container()

            # text
            col1_path_container.text('Tx Path')

            # TX1(Main)
            tx1_state = col1_path_container.checkbox(
                'TX1(Main)', key=f'tx1_path_{specifc_name}')

            # TX2(SUB)
            tx2_state = col1_path_container.checkbox(
                'TX2(Sub)', key=f'tx2_path_{specifc_name}')

            # MIMO
            mimo_state = col1_path_container.checkbox(
                'MIMO', key=f'mimo_path_{specifc_name}')

        with col2_path:
            # container
            col2_path_container = col2_path.container()

            # text
            col2_path_container.text('Rx Path')

            # RX0
            rx0_state = col2_path_container.checkbox(
                'RX0', key=f'rx0_{specifc_name}', disabled=True)

            # RX1
            rx1_state = col2_path_container.checkbox(
                'RX1', key=f'rx1_{specifc_name}', disabled=True)

            # RX2
            rx2_state = col2_path_container.checkbox(
                'RX2', key=f'rx2_{specifc_name}', disabled=True)

            # RX3
            rx3_state = col2_path_container.checkbox(
                'RX3', key=f'rx3_{specifc_name}', disabled=True)

            # RX0+RX1
            rx0rx1_state = col2_path_container.checkbox(
                'RX0RX1', key=f'rx0rx1_{specifc_name}', disabled=True)

            # RX2+RX3
            rx2rx3_state = col2_path_container.checkbox(
                'RX2RX3', key=f'rx2rx3_{specifc_name}', disabled=True)

            # RX0+RX1+RX2+RX3
            rx0rx1rx2rx3_state = col2_path_container.checkbox(
                'RX0RX1RX2RX3', key=f'rx0r1rx2rx3_{specifc_name}', disabled=True)

        with col3_path:
            # container
            col3_path_container = col3_path.container()

            # Sync Path
            sync_path = col3_path_container.selectbox(
                'Sync Path', ('Main', 'CA#1', 'CA#2', 'CA#3'), key=f'sync_path_{specifc_name}')

            # AS path
            as_path = col3_path_container.number_input(
                'AS Path', min_value=0, max_value=1, value=0, key=f'as_path_{specifc_name}')
            as_path_enable_state = col3_path_container.checkbox(
                'AS enable', key=f'as_path_eable_{specifc_name}')

            # SRS path
            srs_path = col3_path_container.number_input(
                'SRS Path', min_value=0, max_value=3, value=0, key=f'srs_path_{specifc_name}')
            srs_path_enable_state = col3_path_container.checkbox(
                'SRS enable', key=f'srs_path_eable_{specifc_name}')

        # horizontal divider
        st.divider()

        # container for FR1
        fr1_container = st.container()

        # subheader
        fr1_container.subheader('FR1')

        # Seperate 4 columns
        col1_bw, col2_mcs, col3_type, col4_rb = fr1_container.columns(4)

        with col1_bw:
            # container
            col1_bw_fr1 = col1_bw.container()

            # text
            col1_bw_fr1.text('BW')

            # bw_fr1
            bw5_fr1_state = col1_bw_fr1.checkbox(
                '5MHz', key=f'bw5_fr1_{specifc_name}')
            bw10_fr1_state = col1_bw_fr1.checkbox(
                '10MHz', key=f'bw10_fr1_{specifc_name}')
            bw15_fr1_state = col1_bw_fr1.checkbox(
                '15MHz', key=f'bw15_fr1_{specifc_name}')
            bw20_fr1_state = col1_bw_fr1.checkbox(
                '20MHz', key=f'bw20_fr1_{specifc_name}')
            bw25_fr1_state = col1_bw_fr1.checkbox(
                '25MHz', key=f'bw25_fr1_{specifc_name}')
            bw30_fr1_state = col1_bw_fr1.checkbox(
                '30MHz', key=f'bw30_fr1_{specifc_name}')
            bw40_fr1_state = col1_bw_fr1.checkbox(
                '40MHz', key=f'bw40_fr1_{specifc_name}')
            bw50_fr1_state = col1_bw_fr1.checkbox(
                '50MHz', key=f'bw50_fr1_{specifc_name}')
            bw60_fr1_state = col1_bw_fr1.checkbox(
                '60MHz', key=f'bw60_fr1_{specifc_name}')
            bw70_fr1_state = col1_bw_fr1.checkbox(
                '70MHz', key=f'bw70_fr1_{specifc_name}')
            bw80_fr1_state = col1_bw_fr1.checkbox(
                '80MHz', key=f'bw80_fr1_{specifc_name}')
            bw90_fr1_state = col1_bw_fr1.checkbox(
                '90MHz', key=f'bw90_fr1_{specifc_name}')
            bw100_fr1_state = col1_bw_fr1.checkbox(
                '100MHz', key=f'bw100_fr1_{specifc_name}')

        with col2_mcs:
            # container
            col2_mcs_fr1 = col2_mcs.container()

            # text
            col2_mcs_fr1.text('MCS')

            # mcs_fr1
            qpsk_fr1_state = col2_mcs_fr1.checkbox(
                'QPSK', key=f'qpdk_fr1_{specifc_name}')
            q16_fr1_state = col2_mcs_fr1.checkbox(
                'Q16', key=f'q16_fr1_{specifc_name}')
            q64_fr1_state = col2_mcs_fr1.checkbox(
                'Q64', key=f'q64_fr1_{specifc_name}')
            q256_fr1_state = col2_mcs_fr1.checkbox(
                'Q256', key=f'q256_fr1_{specifc_name}')
            bpsk_fr1_state = col2_mcs_fr1.checkbox(
                'BPSK', key=f'bpsk_fr1_{specifc_name}')

        with col3_type:
            # container
            col3_type_fr1 = col3_type.container()

            # text
            col3_type_fr1.text('TYPE')

            # mcs_fr1
            dfts_fr1_state = col3_type_fr1.checkbox(
                'DFTS', key=f'dfts_fr1_{specifc_name}')
            cp_fr1_state = col3_type_fr1.checkbox(
                'CP', key=f'cp_fr1_{specifc_name}')

        with col4_rb:
            # container
            col4_rb_fr1 = col4_rb.container()

            # text
            col4_rb_fr1.text('RB SETTING')

            # mcs_fr1
            inner_full_fr1_state = col4_rb_fr1.checkbox(
                'INNER_FULL', key=f'inner_full_fr1_{specifc_name}', disabled=True)
            outer_full_fr1_state = col4_rb_fr1.checkbox(
                'OUTER_FULL', key=f'outer_full_fr1_{specifc_name}', disabled=True)
            inner_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_LEFT', key=f'inner_1rb_left_fr1_{specifc_name}', disabled=True)
            inner_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_RIGHT', key=f'inner_1rb_right_fr1_{specifc_name}', disabled=True)
            edge_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_LEFT', key=f'edge_1rb_left_fr1_{specifc_name}', disabled=True)
            edge_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_RIGHT', key=f'edge_1rb_right_fr1_{specifc_name}', disabled=True)
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_LEFT', key=f'edge_full_left_fr1_{specifc_name}', disabled=True)
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_RIGHT', key=f'edge_full_right_fr1_{specifc_name}', disabled=True)

        # horizontal divider
        fr1_container.divider()
        fr1_container.subheader('FR1')

        col1_lb, col2_mhb, col3_uhb = fr1_container.columns(3)

        with col1_lb:
            # container
            col1_lb_fr1 = col1_lb.container()

            # text
            col1_lb_fr1.text('LB')

            # LB
            lb_all_fr1_state = col1_lb_fr1.checkbox(
                'LB_ALL', key=f'lb_all_fr1_{specifc_name}')
            b5_fr1_state = col1_lb_fr1.checkbox(
                'N5', key=f'b5_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b8_fr1_state = col1_lb_fr1.checkbox(
                'N8', key=f'b8_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b12_fr1_state = col1_lb_fr1.checkbox(
                'N12', key=f'b12_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b13_fr1_state = col1_lb_fr1.checkbox(
                'N13', key=f'b13_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b14_fr1_state = col1_lb_fr1.checkbox(
                'N14', key=f'b14_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b20_fr1_state = col1_lb_fr1.checkbox(
                'N20', key=f'b20_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b24_fr1_state = col1_lb_fr1.checkbox(
                'N24', key=f'b24_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b26_fr1_state = col1_lb_fr1.checkbox(
                'N26', key=f'b26_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28a_fr1_state = col1_lb_fr1.checkbox(
                'N28A', key=f'b28a_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28b_fr1_state = col1_lb_fr1.checkbox(
                'N28B', key=f'b28b_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b29_fr1_state = col1_lb_fr1.checkbox(
                'N29', key=f'b29_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b32_fr1_state = col1_lb_fr1.checkbox(
                'N32', key=f'b32_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b71_fr1_state = col1_lb_fr1.checkbox(
                'N71', key=f'b71_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])

        with col2_mhb:
            # container
            col2_mhb_fr1 = col2_mhb.container()

            # text
            col2_mhb_fr1.text('MHB')

            # MHB
            mhb_all_fr1_state = col2_mhb_fr1.checkbox(
                'MHB_ALL', key=f'mhb_all_fr1_{specifc_name}')
            b1_fr1_state = col2_mhb_fr1.checkbox(
                'N1', key=f'b1_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b2_fr1_state = col2_mhb_fr1.checkbox(
                'N2', key=f'b2_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b3_fr1_state = col2_mhb_fr1.checkbox(
                'N3', key=f'b3_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b7_fr1_state = col2_mhb_fr1.checkbox(
                'N7', key=f'b7_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b30_fr1_state = col2_mhb_fr1.checkbox(
                'N30', key=f'b30_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b25_fr1_state = col2_mhb_fr1.checkbox(
                'N25', key=f'b25_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b66_fr1_state = col2_mhb_fr1.checkbox(
                'N66', key=f'b66_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b70_fr1_state = col2_mhb_fr1.checkbox(
                'N70', key=f'b70_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b40_fr1_state = col2_mhb_fr1.checkbox(
                'N40', key=f'b40_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b38_fr1_state = col2_mhb_fr1.checkbox(
                'N38', key=f'b38_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b41_fr1_state = col2_mhb_fr1.checkbox(
                'N41', key=f'b41_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b34_fr1_state = col2_mhb_fr1.checkbox(
                'N34', key=f'b34_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b75_fr1_state = col2_mhb_fr1.checkbox(
                'N75', key=f'b75_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b76_fr1_state = col2_mhb_fr1.checkbox(
                'N76', key=f'b76_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b255_fr1_state = col2_mhb_fr1.checkbox(
                'N255', key=f'b255_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b256_fr1_state = col2_mhb_fr1.checkbox(
                'N256', key=f'b256_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])

        with col3_uhb:
            # container
            col3_uhb_fr1 = col3_uhb.container()

            # text
            col3_uhb_fr1.text('UHB')

            # UHB
            uhb_all_fr1_state = col3_uhb_fr1.checkbox(
                'UHB_ALL', key=f'uhb_all_fr1_{specifc_name}')
            b48_fr1_state = col3_uhb_fr1.checkbox(
                'N48', key=f'b48_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b77_fr1_state = col3_uhb_fr1.checkbox(
                'N77', key=f'b77_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b78_fr1_state = col3_uhb_fr1.checkbox(
                'N78', key=f'b78_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b79_fr1_state = col3_uhb_fr1.checkbox(
                'N79', key=f'b79_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])

    with endc_tab:
        pass

    with ulca_tab:
        # specify key name in this page and tab
        specifc_name = 'ULCA_ftm'

        # Seperate 3 columns
        col1_m, col2_m, col3_m = st.columns(3)

        # col1_m
        with col1_m:
            # container
            col1m_container = col1_m.container()

            # Instrument
            instrument = col1m_container.selectbox(
                'Instrument', ('cmw100', 'cmw100+fsw',), key=f'inst_select_{specifc_name}')

            # Basic items need activating
            ulca_state = col1m_container.checkbox(
                'ULCA_Tab_activated', key=f'activated_{specifc_name}')
            debug_mode_state = col1m_container.checkbox(
                'Debug mode', key=f'debug_mode_{specifc_name}')
            fd_correct_state = col1m_container.checkbox(
                'FDCorrect', key=f'fd_correct_{specifc_name}')

            # horizontal divider
            col1m_container.divider()

            # Tx port setting
            tx_port = col1m_container.number_input(
                'Tx Port', min_value=1, max_value=8, value=1, key=f'tx_port_{specifc_name}')
            port_table_state = col1m_container.checkbox(
                'port table', key=f'port_table_{specifc_name}')

            # Tx level select except level sweep
            tx_level = col1m_container.slider(
                'Tx level excluding level sweep', min_value=-40, max_value=30, value=27, key=f'tx_level_{specifc_name}')

        with col2_m:
            # container
            col2m_container = col2_m.container()

            # text
            col2m_container.text('Test Items')

            # Tx Harmonic
            tx_harmonic_state = col2m_container.checkbox(
                'Tx LMH', key=f'tx_lmh_{specifc_name}')

            # Tx CBE
            tx_cbe_state = col2m_container.checkbox(
                'Tx CBE', key=f'tx_cbe_{specifc_name}')

        with col3_m:
            # container
            col3m_container = col3_m.container()

            # text
            col3m_container.text('RATs')

            # FR1
            fr1_state = col3m_container.checkbox(
                'FR1', key=f'fr1_{specifc_name}', disabled=True)

            # LTE
            lte_state = col3m_container.checkbox(
                'LTE', key=f'lte_{specifc_name}')

            # WCDMA
            wcdma_state = col3m_container.checkbox(
                'WCDMA', key=f'wcdma_{specifc_name}', disabled=True)

            # GSM
            fsm_state = col3m_container.checkbox(
                'GSM', key=f'gsm_{specifc_name}', disabled=True)

            # horizontal divider
            col3m_container.divider()

            # text
            col3m_container.text('Channels')

            # L chan
            lch_state = col3m_container.checkbox(
                'L', key=f'lch_{specifc_name}')

            # M chan
            mch_state = col3m_container.checkbox(
                'M', key=f'mch_{specifc_name}')

            # H chan
            hch_state = col3m_container.checkbox(
                'H', key=f'hch_{specifc_name}')

        # horizontal divider
        st.divider()

        # Seperate 3 columns
        col1_path, col2_path, col3_path = st.columns(3)

        with col1_path:
            # container
            col1_path_container = col1_path.container()

            # text
            col1_path_container.text('Tx Path')

            # TX1(Main)
            tx1_state = col1_path_container.checkbox(
                'TX1(Main)', key=f'tx1_path_{specifc_name}')

            # TX2(SUB)
            tx2_state = col1_path_container.checkbox(
                'TX2(Sub)', key=f'tx2_path_{specifc_name}', disabled=True)

            # MIMO
            mimo_state = col1_path_container.checkbox(
                'MIMO', key=f'mimo_path_{specifc_name}', disabled=True)

        with col2_path:
            # container
            col2_path_container = col2_path.container()

            # text
            col2_path_container.text('Rx Path')

            # RX0
            rx0_state = col2_path_container.checkbox(
                'RX0', key=f'rx0_{specifc_name}', disabled=True)

            # RX1
            rx1_state = col2_path_container.checkbox(
                'RX1', key=f'rx1_{specifc_name}', disabled=True)

            # RX2
            rx2_state = col2_path_container.checkbox(
                'RX2', key=f'rx2_{specifc_name}', disabled=True)

            # RX3
            rx3_state = col2_path_container.checkbox(
                'RX3', key=f'rx3_{specifc_name}', disabled=True)

            # RX0+RX1
            rx0rx1_state = col2_path_container.checkbox(
                'RX0RX1', key=f'rx0rx1_{specifc_name}', disabled=True)

            # RX2+RX3
            rx2rx3_state = col2_path_container.checkbox(
                'RX2RX3', key=f'rx2rx3_{specifc_name}', disabled=True)

            # RX0+RX1+RX2+RX3
            rx0rx1rx2rx3_state = col2_path_container.checkbox(
                'RX0RX1RX2RX3', key=f'rx0r1rx2rx3_{specifc_name}', disabled=True)

        with col3_path:
            # container
            col3_path_container = col3_path.container()

            # Sync Path
            sync_path = col3_path_container.selectbox(
                'Sync Path', ('Main', 'CA#1', 'CA#2', 'CA#3'), key=f'sync_path_{specifc_name}')

            # AS path
            as_path = col3_path_container.number_input(
                'AS Path', min_value=0, max_value=1, value=0, key=f'as_path_{specifc_name}')
            as_path_enable_state = col3_path_container.checkbox(
                'AS enable', key=f'as_path_eable_{specifc_name}')

            # SRS path
            srs_path = col3_path_container.number_input(
                'SRS Path', min_value=0, max_value=3, value=0, key=f'srs_path_{specifc_name}', disabled=True)
            srs_path_enable_state = col3_path_container.checkbox(
                'SRS enable', key=f'srs_path_eable_{specifc_name}', disabled=True)

            # freq sweep steps
            cbe_limit_margin = col3_path_container.number_input(
                'CBE Limit Margin', min_value=0.0, max_value=5.0, step=0.5, value=1.5, key=f'cbe_limit_margin_{specifc_name}')

        # horizontal divider
        st.divider()

        # container for LTE
        lte_container = st.container()

        # subheader
        lte_container.subheader('LTE')

        # Seperate 4 columns
        col1_bw, col2_mcs, col3_rb = lte_container.columns(3)

        with col1_bw:
            # container
            col1_bw_lte = col1_bw.container()

            # text
            col1_bw_lte.text('BW')

            # bw_lte
            bw_ulca_lte_all_state = col1_bw_lte.checkbox(
                'BW ALL', key=f'bw_ulca_lte_{specifc_name}')
            bw20_5_lte_state = col1_bw_lte.checkbox(
                '20+5', key=f'bw20_5_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw5_20_lte_state = col1_bw_lte.checkbox(
                '5+20', key=f'bw5_20_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw20_10_lte_state = col1_bw_lte.checkbox(
                '20+10', key=f'bw20_10_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw10_20_lte_state = col1_bw_lte.checkbox(
                '10+20', key=f'bw10_20_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw20_15_lte_state = col1_bw_lte.checkbox(
                '20+15', key=f'bw20_15_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw15_20_lte_state = col1_bw_lte.checkbox(
                '15+20', key=f'bw15_20_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw20_20_lte_state = col1_bw_lte.checkbox(
                '20+20', key=f'bw20_20_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw15_15_lte_state = col1_bw_lte.checkbox(
                '15+15', key=f'bw15_15_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw15_10_lte_state = col1_bw_lte.checkbox(
                '15+10', key=f'bw15_10_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw10_15_lte_state = col1_bw_lte.checkbox(
                '10+15', key=f'bw10_15_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw5_10_lte_state = col1_bw_lte.checkbox(
                '5+10', key=f'bw5_10_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw10_5_lte_state = col1_bw_lte.checkbox(
                '10+5', key=f'bw10_5_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw10_10_lte_state = col1_bw_lte.checkbox(
                '10+10', key=f'bw10_10_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw5_15_lte_state = col1_bw_lte.checkbox(
                '5+15', key=f'bw5_15_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw15_5_lte_state = col1_bw_lte.checkbox(
                '15+5', key=f'bw15_5_lte_{specifc_name}', value=st.session_state[f'bw_ulca_lte_{specifc_name}'])
            bw40_lte_state = col1_bw_lte.checkbox(
                '40', key=f'bw40_lte_{specifc_name}', disabled=True)

        with col2_mcs:
            # container
            col2_mcs_lte = col2_mcs.container()

            # text
            col2_mcs_lte.text('MCS')

            # mcs_lte
            qpsk_lte_state = col2_mcs_lte.checkbox(
                'QPSK', key=f'qpdk_lte_{specifc_name}')
            q16_lte_state = col2_mcs_lte.checkbox(
                'Q16', key=f'q16_lte_{specifc_name}')
            q64_lte_state = col2_mcs_lte.checkbox(
                'Q64', key=f'q64_lte_{specifc_name}')
            q256_lte_state = col2_mcs_lte.checkbox(
                'Q256', key=f'q256_lte_{specifc_name}')

        with col3_rb:
            # container
            col3_rb_lte = col3_rb.container()

            # text
            col3_rb_lte.text('RB SETTING')

            # mcs_lte
            one_rb_0_null_lte_state = col3_rb_lte.checkbox(
                '1RB0_NULL', key=f'one_rb0_null_lte_{specifc_name}')
            prb_null_lte_state = col3_rb_lte.checkbox(
                'PRB_NULL', key=f'prb_null_lte_{specifc_name}')
            frb_null_lte_state = col3_rb_lte.checkbox(
                'FRB_NULL', key=f'frb_null_lte_{specifc_name}')
            frb_frb_lte_state = col3_rb_lte.checkbox(
                'FRB_FRB', key=f'frb_frb_lte_{specifc_name}')
            one_rb_max_one_rb_0_lte_state = col3_rb_lte.checkbox(
                '1RB0_1RBmax', key=f'one_rb0_one_rbmax_lte_{specifc_name}')
            one_rb_max_one_rb_0_lte_state = col3_rb_lte.checkbox(
                '1RBmax_1RB0', key=f'one_rbmax_one_rb0_lte_{specifc_name}')

            # divider
            col3_rb_lte.divider()

            # option to select
            criteria_ulca = col3_rb_lte.radio(
                'Criteria', ('3GPP', 'FCC'), index=1)

        # horizontal divider
        lte_container.divider()
        lte_container.subheader('LTE')

        col1_lb, col2_mhb, col3_uhb = lte_container.columns(3)

        with col1_lb:
            # container
            col1_lb_lte = col1_lb.container()

            # text
            col1_lb_lte.text('LB')

            # LB
            b5b_lte_state = col1_lb_lte.checkbox(
                'L5B', key=f'b5b_lte_{specifc_name}')

        with col2_mhb:
            # container
            col2_mhb_lte = col2_mhb.container()

            # text
            col2_mhb_lte.text('MHB')

            # MHB
            mhb_ulca_all_lte_state = col2_mhb_lte.checkbox(
                'MHB_ALL', key=f'mhb_all_lte_{specifc_name}')
            b1c_lte_state = col2_mhb_lte.checkbox(
                'L1C', key=f'b1c_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b3c_lte_state = col2_mhb_lte.checkbox(
                'L3C', key=f'b3c_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b7c_lte_state = col2_mhb_lte.checkbox(
                'L7C', key=f'b7c_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b66b_lte_state = col2_mhb_lte.checkbox(
                'L66B', key=f'b66b_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b66c_lte_state = col2_mhb_lte.checkbox(
                'L66C', key=f'b66c_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b40c_lte_state = col2_mhb_lte.checkbox(
                'L40C', key=f'b40c_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b38c_lte_state = col2_mhb_lte.checkbox(
                'L38C', key=f'b38c_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b41c_lte_state = col2_mhb_lte.checkbox(
                'L41C', key=f'b41c_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])

        with col3_uhb:
            # container
            col3_uhb_lte = col3_uhb.container()

            # text
            col3_uhb_lte.text('UHB')

            # UHB
            b42c_lte_state = col3_uhb_lte.checkbox(
                'L42C', key=f'b42c_lte_{specifc_name}')
            b48c_lte_state = col3_uhb_lte.checkbox(
                'L48C', key=f'b48c_lte_{specifc_name}', disabled=True)

    with cse_tab:
        # specify key name in this page and tab
        specifc_name = 'CSE_ftm'

        # Seperate 3 columns
        col1_m, col2_m, col3_m = st.columns(3)

        # col1_m
        with col1_m:
            # container
            col1m_container = col1_m.container()

            # Instrument
            instrument = col1m_container.selectbox(
                'Instrument', ('cmw100+fsw',), key=f'inst_select_{specifc_name}')

            # Basic items need activating
            cse_state = col1m_container.checkbox(
                'CSE_Tab_activated', key=f'activated_{specifc_name}')
            get_temp_state = col1m_container.checkbox(
                'GetTemp', key=f'get_temp_{specifc_name}')
            fd_correct_state = col1m_container.checkbox(
                'FDCorrect', key=f'fd_correct_{specifc_name}')

            # horizontal divider
            col1m_container.divider()

            # Tx port setting
            tx_port = col1m_container.number_input(
                'Tx Port', min_value=1, max_value=8, value=1, key=f'tx_port_{specifc_name}')
            port_table_state = col1m_container.checkbox(
                'port table', key=f'port_table_{specifc_name}')

            # Tx level select except level sweep
            tx_level = col1m_container.slider(
                'Tx level excluding level sweep', min_value=-40, max_value=30, value=27, key=f'tx_level_{specifc_name}')

        with col2_m:
            # container
            col2m_container = col2_m.container()

            # text
            col2m_container.text('Test Items')

            # Tx Harmonic
            tx_harmonic_state = col2m_container.checkbox(
                'Tx Harmonic', key=f'tx_harmonic_{specifc_name}')

            # Tx CBE
            tx_cbe_state = col2m_container.checkbox(
                'Tx CBE', key=f'tx_cbe_{specifc_name}')

        with col3_m:
            # container
            col3m_container = col3_m.container()

            # text
            col3m_container.text('RATs')

            # FR1
            fr1_state = col3m_container.checkbox(
                'FR1', key=f'fr1_{specifc_name}')

            # LTE
            lte_state = col3m_container.checkbox(
                'LTE', key=f'lte_{specifc_name}')

            # WCDMA
            wcdma_state = col3m_container.checkbox(
                'WCDMA', key=f'wcdma_{specifc_name}')

            # GSM
            fsm_state = col3m_container.checkbox(
                'GSM', key=f'gsm_{specifc_name}')

            # horizontal divider
            col3m_container.divider()

            # text
            col3m_container.text('Channels')

            # L chan
            lch_state = col3m_container.checkbox(
                'L', key=f'lch_{specifc_name}')

            # M chan
            mch_state = col3m_container.checkbox(
                'M', key=f'mch_{specifc_name}')

            # H chan
            hch_state = col3m_container.checkbox(
                'H', key=f'hch_{specifc_name}')

        # horizontal divider
        st.divider()

        # Seperate 3 columns
        col1_path, col2_path, col3_path = st.columns(3)

        with col1_path:
            # container
            col1_path_container = col1_path.container()

            # text
            col1_path_container.text('Tx Path')

            # TX1(Main)
            tx1_state = col1_path_container.checkbox(
                'TX1(Main)', key=f'tx1_path_{specifc_name}')

            # TX2(SUB)
            tx2_state = col1_path_container.checkbox(
                'TX2(Sub)', key=f'tx2_path_{specifc_name}')

            # MIMO
            mimo_state = col1_path_container.checkbox(
                'MIMO', key=f'mimo_path_{specifc_name}')

        with col2_path:
            # container
            col2_path_container = col2_path.container()

            # text
            col2_path_container.text('Rx Path')

            # RX0
            rx0_state = col2_path_container.checkbox(
                'RX0', key=f'rx0_{specifc_name}', disabled=True)

            # RX1
            rx1_state = col2_path_container.checkbox(
                'RX1', key=f'rx1_{specifc_name}', disabled=True)

            # RX2
            rx2_state = col2_path_container.checkbox(
                'RX2', key=f'rx2_{specifc_name}', disabled=True)

            # RX3
            rx3_state = col2_path_container.checkbox(
                'RX3', key=f'rx3_{specifc_name}', disabled=True)

            # RX0+RX1
            rx0rx1_state = col2_path_container.checkbox(
                'RX0RX1', key=f'rx0rx1_{specifc_name}', disabled=True)

            # RX2+RX3
            rx2rx3_state = col2_path_container.checkbox(
                'RX2RX3', key=f'rx2rx3_{specifc_name}', disabled=True)

            # RX0+RX1+RX2+RX3
            rx0rx1rx2rx3_state = col2_path_container.checkbox(
                'RX0RX1RX2RX3', key=f'rx0r1rx2rx3_{specifc_name}', disabled=True)

        with col3_path:
            # container
            col3_path_container = col3_path.container()

            # Sync Path
            sync_path = col3_path_container.selectbox(
                'Sync Path', ('Main', 'CA#1', 'CA#2', 'CA#3'), key=f'sync_path_{specifc_name}')

            # AS path
            as_path = col3_path_container.number_input(
                'AS Path', min_value=0, max_value=1, value=0, key=f'as_path_{specifc_name}')
            as_path_enable_state = col3_path_container.checkbox(
                'AS enable', key=f'as_path_eable_{specifc_name}')

            # SRS path
            srs_path = col3_path_container.number_input(
                'SRS Path', min_value=0, max_value=3, value=0, key=f'srs_path_{specifc_name}')
            srs_path_enable_state = col3_path_container.checkbox(
                'SRS enable', key=f'srs_path_eable_{specifc_name}')

            # freq sweep steps
            cbe_limit_margin = col3_path_container.number_input(
                'CBE Limit Margin', min_value=0.0, max_value=5.0, step=0.5, value=1.5, key=f'cbe_limit_margin_{specifc_name}')

        # horizontal divider
        st.divider()

        # container for FR1
        fr1_container = st.container()

        # subheader
        fr1_container.subheader('FR1')

        # Seperate 4 columns
        col1_bw, col2_mcs, col3_type, col4_rb = fr1_container.columns(4)

        with col1_bw:
            # container
            col1_bw_fr1 = col1_bw.container()

            # text
            col1_bw_fr1.text('BW')

            # bw_fr1
            bw5_fr1_state = col1_bw_fr1.checkbox(
                '5MHz', key=f'bw5_fr1_{specifc_name}')
            bw10_fr1_state = col1_bw_fr1.checkbox(
                '10MHz', key=f'bw10_fr1_{specifc_name}')
            bw15_fr1_state = col1_bw_fr1.checkbox(
                '15MHz', key=f'bw15_fr1_{specifc_name}')
            bw20_fr1_state = col1_bw_fr1.checkbox(
                '20MHz', key=f'bw20_fr1_{specifc_name}')
            bw25_fr1_state = col1_bw_fr1.checkbox(
                '25MHz', key=f'bw25_fr1_{specifc_name}')
            bw30_fr1_state = col1_bw_fr1.checkbox(
                '30MHz', key=f'bw30_fr1_{specifc_name}')
            bw40_fr1_state = col1_bw_fr1.checkbox(
                '40MHz', key=f'bw40_fr1_{specifc_name}')
            bw50_fr1_state = col1_bw_fr1.checkbox(
                '50MHz', key=f'bw50_fr1_{specifc_name}')
            bw60_fr1_state = col1_bw_fr1.checkbox(
                '60MHz', key=f'bw60_fr1_{specifc_name}')
            bw70_fr1_state = col1_bw_fr1.checkbox(
                '70MHz', key=f'bw70_fr1_{specifc_name}')
            bw80_fr1_state = col1_bw_fr1.checkbox(
                '80MHz', key=f'bw80_fr1_{specifc_name}')
            bw90_fr1_state = col1_bw_fr1.checkbox(
                '90MHz', key=f'bw90_fr1_{specifc_name}')
            bw100_fr1_state = col1_bw_fr1.checkbox(
                '100MHz', key=f'bw100_fr1_{specifc_name}')

        with col2_mcs:
            # container
            col2_mcs_fr1 = col2_mcs.container()

            # text
            col2_mcs_fr1.text('MCS')

            # mcs_fr1
            qpsk_fr1_state = col2_mcs_fr1.checkbox(
                'QPSK', key=f'qpdk_fr1_{specifc_name}')
            q16_fr1_state = col2_mcs_fr1.checkbox(
                'Q16', key=f'q16_fr1_{specifc_name}')
            q64_fr1_state = col2_mcs_fr1.checkbox(
                'Q64', key=f'q64_fr1_{specifc_name}')
            q256_fr1_state = col2_mcs_fr1.checkbox(
                'Q256', key=f'q256_fr1_{specifc_name}')
            bpsk_fr1_state = col2_mcs_fr1.checkbox(
                'BPSK', key=f'bpsk_fr1_{specifc_name}')

        with col3_type:
            # container
            col3_type_fr1 = col3_type.container()

            # text
            col3_type_fr1.text('TYPE')

            # mcs_fr1
            dfts_fr1_state = col3_type_fr1.checkbox(
                'DFTS', key=f'dfts_fr1_{specifc_name}')
            cp_fr1_state = col3_type_fr1.checkbox(
                'CP', key=f'cp_fr1_{specifc_name}')

        with col4_rb:
            # container
            col4_rb_fr1 = col4_rb.container()

            # text
            col4_rb_fr1.text('RB SETTING')

            # mcs_fr1
            inner_full_fr1_state = col4_rb_fr1.checkbox(
                'INNER_FULL', key=f'inner_full_fr1_{specifc_name}')
            outer_full_fr1_state = col4_rb_fr1.checkbox(
                'OUTER_FULL', key=f'outer_full_fr1_{specifc_name}')
            inner_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_LEFT', key=f'inner_1rb_left_fr1_{specifc_name}')
            inner_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_RIGHT', key=f'inner_1rb_right_fr1_{specifc_name}')
            edge_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_LEFT', key=f'edge_1rb_left_fr1_{specifc_name}')
            edge_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_RIGHT', key=f'edge_1rb_right_fr1_{specifc_name}')
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_LEFT', key=f'edge_full_left_fr1_{specifc_name}')
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_RIGHT', key=f'edge_full_right_fr1_{specifc_name}')

        # horizontal divider
        fr1_container.divider()
        fr1_container.subheader('FR1')

        col1_lb, col2_mhb, col3_uhb = fr1_container.columns(3)

        with col1_lb:
            # container
            col1_lb_fr1 = col1_lb.container()

            # text
            col1_lb_fr1.text('LB')

            # LB
            lb_all_fr1_state = col1_lb_fr1.checkbox(
                'LB_ALL', key=f'lb_all_fr1_{specifc_name}')
            b5_fr1_state = col1_lb_fr1.checkbox(
                'N5', key=f'b5_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b8_fr1_state = col1_lb_fr1.checkbox(
                'N8', key=f'b8_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b12_fr1_state = col1_lb_fr1.checkbox(
                'N12', key=f'b12_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b13_fr1_state = col1_lb_fr1.checkbox(
                'N13', key=f'b13_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b14_fr1_state = col1_lb_fr1.checkbox(
                'N14', key=f'b14_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b20_fr1_state = col1_lb_fr1.checkbox(
                'N20', key=f'b20_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b24_fr1_state = col1_lb_fr1.checkbox(
                'N24', key=f'b24_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b26_fr1_state = col1_lb_fr1.checkbox(
                'N26', key=f'b26_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28a_fr1_state = col1_lb_fr1.checkbox(
                'N28A', key=f'b28a_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b28b_fr1_state = col1_lb_fr1.checkbox(
                'N28B', key=f'b28b_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b29_fr1_state = col1_lb_fr1.checkbox(
                'N29', key=f'b29_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b32_fr1_state = col1_lb_fr1.checkbox(
                'N32', key=f'b32_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])
            b71_fr1_state = col1_lb_fr1.checkbox(
                'N71', key=f'b71_fr1_{specifc_name}', value=st.session_state[f'lb_all_fr1_{specifc_name}'])

        with col2_mhb:
            # container
            col2_mhb_fr1 = col2_mhb.container()

            # text
            col2_mhb_fr1.text('MHB')

            # MHB
            mhb_all_fr1_state = col2_mhb_fr1.checkbox(
                'MHB_ALL', key=f'mhb_all_fr1_{specifc_name}')
            b1_fr1_state = col2_mhb_fr1.checkbox(
                'N1', key=f'b1_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b2_fr1_state = col2_mhb_fr1.checkbox(
                'N2', key=f'b2_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b3_fr1_state = col2_mhb_fr1.checkbox(
                'N3', key=f'b3_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b7_fr1_state = col2_mhb_fr1.checkbox(
                'N7', key=f'b7_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b30_fr1_state = col2_mhb_fr1.checkbox(
                'N30', key=f'b30_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b25_fr1_state = col2_mhb_fr1.checkbox(
                'N25', key=f'b25_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b66_fr1_state = col2_mhb_fr1.checkbox(
                'N66', key=f'b66_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b70_fr1_state = col2_mhb_fr1.checkbox(
                'N70', key=f'b70_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b40_fr1_state = col2_mhb_fr1.checkbox(
                'N40', key=f'b40_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b38_fr1_state = col2_mhb_fr1.checkbox(
                'N38', key=f'b38_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b41_fr1_state = col2_mhb_fr1.checkbox(
                'N41', key=f'b41_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b34_fr1_state = col2_mhb_fr1.checkbox(
                'N34', key=f'b34_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b75_fr1_state = col2_mhb_fr1.checkbox(
                'N75', key=f'b75_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b76_fr1_state = col2_mhb_fr1.checkbox(
                'N76', key=f'b76_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b255_fr1_state = col2_mhb_fr1.checkbox(
                'N255', key=f'b255_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])
            b256_fr1_state = col2_mhb_fr1.checkbox(
                'N256', key=f'b256_fr1_{specifc_name}', value=st.session_state[f'mhb_all_fr1_{specifc_name}'])

        with col3_uhb:
            # container
            col3_uhb_fr1 = col3_uhb.container()

            # text
            col3_uhb_fr1.text('UHB')

            # UHB
            uhb_all_fr1_state = col3_uhb_fr1.checkbox(
                'UHB_ALL', key=f'uhb_all_fr1_{specifc_name}')
            b48_fr1_state = col3_uhb_fr1.checkbox(
                'N48', key=f'b48_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b77_fr1_state = col3_uhb_fr1.checkbox(
                'N77', key=f'b77_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b78_fr1_state = col3_uhb_fr1.checkbox(
                'N78', key=f'b78_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])
            b79_fr1_state = col3_uhb_fr1.checkbox(
                'N79', key=f'b79_fr1_{specifc_name}', value=st.session_state[f'uhb_all_fr1_{specifc_name}'])

        # horizontal divider
        st.divider()

        # container for LTE
        lte_container = st.container()

        # subheader
        lte_container.subheader('LTE')

        # Seperate 4 columns
        col1_bw, col2_mcs, col3_rb = lte_container.columns(3)

        with col1_bw:
            # container
            col1_bw_lte = col1_bw.container()

            # text
            col1_bw_lte.text('BW')

            # bw_lte
            bw1p4_lte_state = col1_bw_lte.checkbox(
                '1.4MHz', key=f'bw1p4_lte_{specifc_name}')
            bw3_lte_state = col1_bw_lte.checkbox(
                '3MHz', key=f'bw3_lte_{specifc_name}')
            bw5_lte_state = col1_bw_lte.checkbox(
                '5MHz', key=f'bw5_lte_{specifc_name}')
            bw10_lte_state = col1_bw_lte.checkbox(
                '10MHz', key=f'bw10_lte_{specifc_name}')
            bw15_lte_state = col1_bw_lte.checkbox(
                '15MHz', key=f'bw15_lte_{specifc_name}')
            bw20_lte_state = col1_bw_lte.checkbox(
                '20MHz', key=f'bw20_lte_{specifc_name}')

        with col2_mcs:
            # container
            col2_mcs_lte = col2_mcs.container()

            # text
            col2_mcs_lte.text('MCS')

            # mcs_lte
            qpsk_lte_state = col2_mcs_lte.checkbox(
                'QPSK', key=f'qpdk_lte_{specifc_name}')
            q16_lte_state = col2_mcs_lte.checkbox(
                'Q16', key=f'q16_lte_{specifc_name}')
            q64_lte_state = col2_mcs_lte.checkbox(
                'Q64', key=f'q64_lte_{specifc_name}')
            q256_lte_state = col2_mcs_lte.checkbox(
                'Q256', key=f'q256_lte_{specifc_name}')

        with col3_rb:
            # container
            col3_rb_lte = col3_rb.container()

            # text
            col3_rb_lte.text('RB SETTING')

            # mcs_lte
            prb_lte_state = col3_rb_lte.checkbox(
                'PRB', key=f'prb_lte_{specifc_name}')
            frb_lte_state = col3_rb_lte.checkbox(
                'FRB', key=f'frb_lte_{specifc_name}')
            one_rb_0_lte_state = col3_rb_lte.checkbox(
                '1RB_0', key=f'one_rb_0_lte_{specifc_name}')
            one_rb_max_lte_state = col3_rb_lte.checkbox(
                '1RB_MAX', key=f'one_rb_max_lte_{specifc_name}')

        # horizontal divider
        lte_container.divider()
        lte_container.subheader('LTE')

        col1_lb, col2_mhb, col3_uhb = lte_container.columns(3)

        with col1_lb:
            # container
            col1_lb_lte = col1_lb.container()

            # text
            col1_lb_lte.text('LB')

            # LB
            lb_all_lte_state = col1_lb_lte.checkbox(
                'LB_ALL', key=f'lb_all_lte_{specifc_name}')
            b5_lte_state = col1_lb_lte.checkbox(
                'L5', key=f'b5_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b8_lte_state = col1_lb_lte.checkbox(
                'L8', key=f'b8_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b12_lte_state = col1_lb_lte.checkbox(
                'L12', key=f'b12_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b13_lte_state = col1_lb_lte.checkbox(
                'L13', key=f'b13_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b14_lte_state = col1_lb_lte.checkbox(
                'L14', key=f'b14_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b17_lte_state = col1_lb_lte.checkbox(
                'L17', key=f'b17_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b18_lte_state = col1_lb_lte.checkbox(
                'L18', key=f'b18_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b19_lte_state = col1_lb_lte.checkbox(
                'L19', key=f'b19_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b20_lte_state = col1_lb_lte.checkbox(
                'L20', key=f'b20_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b24_lte_state = col1_lb_lte.checkbox(
                'L24', key=f'b24_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b26_lte_state = col1_lb_lte.checkbox(
                'L26', key=f'b26_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b28a_lte_state = col1_lb_lte.checkbox(
                'L28A', key=f'b28a_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b28b_lte_state = col1_lb_lte.checkbox(
                'L28B', key=f'b28b_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b29_lte_state = col1_lb_lte.checkbox(
                'L29', key=f'b29_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b32_lte_state = col1_lb_lte.checkbox(
                'L32', key=f'b32_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])
            b71_lte_state = col1_lb_lte.checkbox(
                'L71', key=f'b71_lte_{specifc_name}', value=st.session_state[f'lb_all_lte_{specifc_name}'])

        with col2_mhb:
            # container
            col2_mhb_lte = col2_mhb.container()

            # text
            col2_mhb_lte.text('MHB')

            # MHB
            mhb_all_lte_state = col2_mhb_lte.checkbox(
                'MHB_ALL', key=f'mhb_all_lte_{specifc_name}')
            b1_lte_state = col2_mhb_lte.checkbox(
                'L1', key=f'b1_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b2_lte_state = col2_mhb_lte.checkbox(
                'L2', key=f'b2_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b3_lte_state = col2_mhb_lte.checkbox(
                'L3', key=f'b3_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b7_lte_state = col2_mhb_lte.checkbox(
                'L7', key=f'b7_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b30_lte_state = col2_mhb_lte.checkbox(
                'L30', key=f'b30_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b25_lte_state = col2_mhb_lte.checkbox(
                'L25', key=f'b25_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b66_lte_state = col2_mhb_lte.checkbox(
                'L66', key=f'b66_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b70_lte_state = col2_mhb_lte.checkbox(
                'L70', key=f'b70_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b39_lte_state = col2_mhb_lte.checkbox(
                'L39', key=f'b39_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b40_lte_state = col2_mhb_lte.checkbox(
                'L40', key=f'b40_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b38_lte_state = col2_mhb_lte.checkbox(
                'L38', key=f'b38_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b41_lte_state = col2_mhb_lte.checkbox(
                'L41', key=f'b41_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b23_lte_state = col2_mhb_lte.checkbox(
                'L23', key=f'b23_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b34_lte_state = col2_mhb_lte.checkbox(
                'L34', key=f'b34_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b75_lte_state = col2_mhb_lte.checkbox(
                'L75', key=f'b75_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])
            b76_lte_state = col2_mhb_lte.checkbox(
                'L76', key=f'b76_lte_{specifc_name}', value=st.session_state[f'mhb_all_lte_{specifc_name}'])

        with col3_uhb:
            # container
            col3_uhb_lte = col3_uhb.container()

            # text
            col3_uhb_lte.text('UHB')

            # UHB
            uhb_all_lte_state = col3_uhb_lte.checkbox(
                'UHB_ALL', key=f'uhb_all_lte_{specifc_name}')
            b42_lte_state = col3_uhb_lte.checkbox(
                'L42', key=f'b42_lte_{specifc_name}', value=st.session_state[f'uhb_all_lte_{specifc_name}'])
            b48_lte_state = col3_uhb_lte.checkbox(
                'L48', key=f'b48_lte_{specifc_name}', value=st.session_state[f'uhb_all_lte_{specifc_name}'])

    with rssiscan_tab:
        pass

    with apt_tab:
        pass


def rx_ue_power_select(*rx_state_arg):
    for rx_state in rx_state_arg:
        if rx_state:
            return True
    return False


def bw_ulca_all_lte_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def mhb_ulca_all_lte_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def lb_all_fr1_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def mhb_all_fr1_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def uhb_all_fr1_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def lb_all_lte_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def mhb_all_lte_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def uhb_all_lte_checked(all_checked):
    if all_checked:
        return True
    else:
        return False


def main():
    # page setting
    st.set_page_config(layout="wide")
    tabs()
    sidebar()


if __name__ == "__main__":
    main()
