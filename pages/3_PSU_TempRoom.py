import streamlit as st
import numpy as np
import pandas as pd
import time
from setting import *


def main():

    # page config
    st.set_page_config(layout="wide")

    # specific key name for sidebar
    specifc_name_sidebar = 'psu_temp'

    # sidebar
    st.sidebar.success("Select a function you want above.")

    # ht_num, nt_num, lt_num, hv_num, nv_num, lv_num = parameters_load()

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        # arguments for temp and volt
        ht = text_input('HT', value=55, key='ht_text')
        nt = text_input('NT', value=25, key='nt_text')
        lt = text_input('LT', value=-10, key='lt_text')
        hv = slider('HV', min_value=3.6, max_value=4.5,
                    step=0.1, value=4.4, key='hv_num')
        nv = slider('NV', min_value=3.6, max_value=4.5,
                    step=0.01, value=3.85, key='nv_num')
        lv = slider('LV', min_value=3.6, max_value=4.5,
                    step=0.1, value=3.6, key='lv_num')
        therm_wt = slider('Wait Time', min_value=0,
                          max_value=600, step=30, value=0, key='wait_time')
        temp_room_off = st.button('Temp Room off', key='temp_room_off')
        if temp_room_off:
            st.write('temp off activated')
        else:
            st.write('temp off does not be activated')

    with col2:
        # PSU and TempRoom
        st.text('PSU and TempRoom')
        temp_room = checkbox(
            'Temp Room and PSU enabled', key=f'temproom_psu_en')
        hthv = checkbox(
            'HTHV', key='hthv_checked')
        htlv = checkbox(
            'HTLV', key='htlv_checked')
        ntnv = checkbox(
            'NTNV', key='ntnv_checked')
        lthv = checkbox(
            'LTHV', key='lthv_checked')
        ltlv = checkbox(
            'LTLV', key='ltlv_checked')

    with col3:
        # PSU
        st.text('PSU')
        psu_state = checkbox(
            'PSU enabled', key='psu_en')
        hv = checkbox(
            'HV', key='hv_checked')
        nv = checkbox(
            'NV', key='nv_checked')
        lv = checkbox(
            'LV', key='lv_checked')

    with col4:
        # PSU
        st.text('ODPM')
        psu_state = checkbox('ODPM enabled', key=f'odpm_en')

    with col5:
        # PSU
        st.text('ODPM2')
        psu_state = checkbox('ODPM2 enabled', key=f'odpm2_en')

    with col6:
        count = number_input('Count', min_value=1, max_value=20,
                             step=1, value=5, key='temp_psu_count')


if __name__ == "__main__":
    main()
    print(st.session_state)
