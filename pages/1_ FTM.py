import streamlit as st
import numpy as np
import pandas as pd
import time


def sidebar():
    # sidebar
    with st.sidebar:

        therm_dis = st.button('Thermal_Charge_Disable',
                              key='therm_dis', use_container_width=True)
        text_suffix = st.text_input('suffix_file_name', "", key='text_suffix')
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
            # container
            col1m_container = col1_m.container()

            # Instrument
            instrument = col1m_container.selectbox(
                'Instrument', ('cmw100',), key='inst_select')

            # Basic items need activating
            genre_state = col1m_container.checkbox('Genre', key='genre')
            volt_mipi_state = col1m_container.checkbox(
                'VoltMipi', key='volt_mipi')
            get_temp_state = col1m_container.checkbox(
                'GetTemp', key='get_temp')
            fd_correct_state = col1m_container.checkbox(
                'FDCorrect', key='fd_correct')

            # horizontal divider
            col1m_container.divider()

            # Tx port setting
            tx_port = col1m_container.number_input(
                'Tx Port', min_value=1, max_value=8, value=1, key='tx_port')
            port_table_state = col1m_container.checkbox(
                'port table', key='port_table')

            # Tx level select except level sweep
            tx_level = col1m_container.slider(
                'Tx level excluding level sweep', min_value=-40, max_value=30, value=27, key='tx_level')

            # Tx level sweep
            tx_level_sweep_start = col1m_container.slider(
                'Tx level sweep start', min_value=-40, max_value=30, value=-20, key='tx_level_sweep_start')
            tx_level_sweep_stop = col1m_container.slider(
                'Tx level sweep stop', min_value=-40, max_value=30, value=27, key='tx_level_sweep_stop')

        with col2_m:
            # container
            col2m_container = col2_m.container()

            # text
            col2m_container.text('Test Items')

            # Tx LMH
            tx_lmh_state = col2m_container.checkbox('Tx_LMH', key='tx_lmh')

            # Rx
            rx_state = col2m_container.checkbox('Rx', key='rx')

            # Rx_quick
            rx_quick_state = col2m_container.checkbox(
                'Rx Quick', key='rx_quick')

            # Tx level sweep
            tx_level_sweep_state = col2m_container.checkbox(
                'Tx level sweep', key='tx_level_sweep')

            # Tx Freq sweep
            tx_freq_sweep_state = col2m_container.checkbox(
                'Tx Freq sweep', key='tx_freq_sweep')

            # Tx 1RB sweep
            tx_1rb_sweep_state = col2m_container.checkbox(
                'Tx 1RB sweep(only for FR1)', key='tx_1rb_sweep')

            # horizontal divider
            col2m_container.divider()

            # text
            col2m_container.text('UE power(only for Rx)')

            # Tx tx_max sweep
            tx_max_state = col2m_container.checkbox(
                'TxMax', key='tx_max', value=rx_ue_power_select(rx_state, rx_quick_state))

            # Tx tx_max sweep
            tx_minus10_state = col2m_container.checkbox(
                'Tx_-10', key='tx_-10', value=rx_ue_power_select(rx_state, rx_quick_state))

        with col3_m:
            # container
            col3m_container = col3_m.container()

            # text
            col3m_container.text('RATs')

            # FR1
            fr1_state = col3m_container.checkbox('FR1', key='fr1')

            # LTE
            lte_state = col3m_container.checkbox('LTE', key='lte')

            # WCDMA
            wcdma_state = col3m_container.checkbox('WCDMA', key='wcdma')

            # GSM
            fsm_state = col3m_container.checkbox('GSM', key='gsm')

            # horizontal divider
            col3m_container.divider()

            # text
            col3m_container.text('Channels')

            # L chan
            lch_state = col3m_container.checkbox('L', key='lch')

            # M chan
            mch_state = col3m_container.checkbox('M', key='mch')

            # H chan
            hch_state = col3m_container.checkbox('H', key='hch')

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
                'TX1(Main)', key='tx1_path')

            # TX2(SUB)
            tx2_state = col1_path_container.checkbox(
                'TX2(Sub)', key='tx2_path')

            # MIMO
            mimo_state = col1_path_container.checkbox('MIMO', key='mimo_path')

        with col2_path:
            # container
            col2_path_container = col2_path.container()

            # text
            col2_path_container.text('Rx Path')

            # RX0
            rx0_state = col2_path_container.checkbox('RX0', key='rx0')

            # RX1
            rx1_state = col2_path_container.checkbox('RX1', key='rx1')

            # RX2
            rx2_state = col2_path_container.checkbox('RX2', key='rx2')

            # RX3
            rx3_state = col2_path_container.checkbox('RX3', key='rx3')

            # RX0+RX1
            rx0rx1_state = col2_path_container.checkbox('RX0RX1', key='rx0rx1')

            # RX2+RX3
            rx2rx3_state = col2_path_container.checkbox('RX2RX3', key='rx2rx3')

            # RX0+RX1+RX2+RX3
            rx0rx1rx2rx3_state = col2_path_container.checkbox(
                'RX0RX1RX2RX3', key='rx0r1rx2rx3')

        with col3_path:
            # container
            col3_path_container = col3_path.container()

            # Sync Path
            sync_path = col3_path_container.selectbox(
                'Sync Path', ('Main', 'CA#1', 'CA#2', 'CA#3'), key='sync_path')

            # AS path
            as_path = col3_path_container.number_input(
                'AS Path', min_value=0, max_value=1, value=0, key='as_path')
            as_path_enable_state = col3_path_container.checkbox(
                'AS enable', key='as_path_eable')

            # SRS path
            as_path = col3_path_container.number_input(
                'SRS Path', min_value=0, max_value=3, value=0, key='srs_path')
            as_path_enable_state = col3_path_container.checkbox(
                'SRS enable', key='srs_path_eable')

        # horizontal divider
        st.divider()

        # container
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
            bw5_fr1_state = col1_bw_fr1.checkbox('5MHz', key='bw5_fr1')
            bw10_fr1_state = col1_bw_fr1.checkbox('10MHz', key='bw10_fr1')
            bw15_fr1_state = col1_bw_fr1.checkbox('15MHz', key='bw15_fr1')
            bw20_fr1_state = col1_bw_fr1.checkbox('20MHz', key='bw20_fr1')
            bw25_fr1_state = col1_bw_fr1.checkbox('25MHz', key='bw25_fr1')
            bw30_fr1_state = col1_bw_fr1.checkbox('30MHz', key='bw30_fr1')
            bw40_fr1_state = col1_bw_fr1.checkbox('40MHz', key='bw40_fr1')
            bw50_fr1_state = col1_bw_fr1.checkbox('50MHz', key='bw50_fr1')
            bw60_fr1_state = col1_bw_fr1.checkbox('60MHz', key='bw60_fr1')
            bw70_fr1_state = col1_bw_fr1.checkbox('70MHz', key='bw70_fr1')
            bw80_fr1_state = col1_bw_fr1.checkbox('80MHz', key='bw80_fr1')
            bw90_fr1_state = col1_bw_fr1.checkbox('90MHz', key='bw90_fr1')
            bw100_fr1_state = col1_bw_fr1.checkbox('100MHz', key='bw100_fr1')

        with col2_mcs:
            # container
            col2_mcs_fr1 = col2_mcs.container()

            # text
            col2_mcs_fr1.text('MCS')

            # mcs_fr1
            qpsk_fr1_state = col2_mcs_fr1.checkbox('QPSK', key='qpdk_fr1')
            q16_fr1_state = col2_mcs_fr1.checkbox('Q16', key='q16_fr1')
            q64_fr1_state = col2_mcs_fr1.checkbox('Q64', key='q64_fr1')
            q256_fr1_state = col2_mcs_fr1.checkbox('Q256', key='q256_fr1')
            bpsk_fr1_state = col2_mcs_fr1.checkbox('BPSK', key='bpsk_fr1')

        with col3_type:
            # container
            col3_type_fr1 = col3_type.container()

            # text
            col3_type_fr1.text('TYPE')

            # mcs_fr1
            dfts_fr1_state = col3_type_fr1.checkbox('DFTS', key='dfts_fr1')
            cp_fr1_state = col3_type_fr1.checkbox('CP', key='cp_fr1')

        with col4_rb:
            # container
            col4_rb_fr1 = col4_rb.container()

            # text
            col4_rb_fr1.text('RB SETTING')

            # mcs_fr1
            inner_full_fr1_state = col4_rb_fr1.checkbox(
                'INNER_FULL', key='inner_full_fr1')
            outer_full_fr1_state = col4_rb_fr1.checkbox(
                'OUTER_FULL', key='outer_full_fr1')
            inner_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_LEFT', key='inner_1rb_left_fr1')
            inner_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'INNER_1RB_RIGHT', key='inner_1rb_right_fr1')
            edge_1rb_left_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_LEFT', key='edge_1rb_left_fr1')
            edge_1rb_right_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_1RB_RIGHT', key='edge_1rb_right_fr1')
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_LEFT', key='edge_full_left_fr1')
            edge_full_fr1_state = col4_rb_fr1.checkbox(
                'EDGE_FULL_RIGHT', key='edge_full_right_fr1')

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
            b5_fr1_state = col1_lb_fr1.checkbox('N5', key='b5_fr1')
            b8_fr1_state = col1_lb_fr1.checkbox('N8', key='b8_fr1')
            b12_fr1_state = col1_lb_fr1.checkbox('N12', key='b12_fr1')
            b13_fr1_state = col1_lb_fr1.checkbox('N13', key='b13_fr1')
            b14_fr1_state = col1_lb_fr1.checkbox('N14', key='b14_fr1')
            b20_fr1_state = col1_lb_fr1.checkbox('N20', key='b20_fr1')
            b24_fr1_state = col1_lb_fr1.checkbox('N24', key='b24_fr1')
            b26_fr1_state = col1_lb_fr1.checkbox('N26', key='b26_fr1')
            b28a_fr1_state = col1_lb_fr1.checkbox('N28A', key='b28a_fr1')
            b28b_fr1_state = col1_lb_fr1.checkbox('N28B', key='b28b_fr1')
            b29_fr1_state = col1_lb_fr1.checkbox('N29', key='b29_fr1')
            b32_fr1_state = col1_lb_fr1.checkbox('N32', key='b32_fr1')
            b71_fr1_state = col1_lb_fr1.checkbox('N71', key='b71_fr1')

        with col2_mhb:
            # container
            col2_mhb_fr1 = col2_mhb.container()

            # text
            col2_mhb_fr1.text('MHB')

            # MHB
            b1_fr1_state = col2_mhb_fr1.checkbox('N1', key='b1_fr1')
            b2_fr1_state = col2_mhb_fr1.checkbox('N2', key='b2_fr1')
            b3_fr1_state = col2_mhb_fr1.checkbox('N3', key='b3_fr1')
            b7_fr1_state = col2_mhb_fr1.checkbox('N7', key='b7_fr1')
            b30_fr1_state = col2_mhb_fr1.checkbox('N30', key='b30_fr1')
            b25_fr1_state = col2_mhb_fr1.checkbox('N25', key='b25_fr1')
            b66_fr1_state = col2_mhb_fr1.checkbox('N66', key='b66_fr1')
            b70_fr1_state = col2_mhb_fr1.checkbox('N70', key='b70_fr1')
            b40_fr1_state = col2_mhb_fr1.checkbox('N40', key='b40_fr1')
            b38_fr1_state = col2_mhb_fr1.checkbox('N38', key='b38_fr1')
            b41_fr1_state = col2_mhb_fr1.checkbox('N41', key='b41_fr1')
            b34_fr1_state = col2_mhb_fr1.checkbox('N34', key='b34_fr1')
            b75_fr1_state = col2_mhb_fr1.checkbox('N75', key='b75_fr1')
            b76_fr1_state = col2_mhb_fr1.checkbox('N76', key='b76_fr1')
            b255_fr1_state = col2_mhb_fr1.checkbox('N255', key='b255_fr1')
            b256_fr1_state = col2_mhb_fr1.checkbox('N256', key='b256_fr1')

        with col3_uhb:
            # container
            col3_uhb_fr1 = col3_uhb.container()

            # text
            col3_uhb_fr1.text('UHB')

            # MHB
            b48_fr1_state = col3_uhb_fr1.checkbox('N48', key='b48_fr1')
            b77_fr1_state = col3_uhb_fr1.checkbox('N77', key='b77_fr1')
            b78_fr1_state = col3_uhb_fr1.checkbox('N78', key='b78_fr1')
            b79_fr1_state = col3_uhb_fr1.checkbox('N79', key='b79_fr1')

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


def rx_ue_power_select(*rx_state_arg):
    for rx_state in rx_state_arg:
        if rx_state:
            return True
    return False


def main():
    # page setting
    st.set_page_config(layout="wide")
    tabs()
    sidebar()


if __name__ == "__main__":
    main()
