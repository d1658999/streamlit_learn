import streamlit as st
import numpy as np
import pandas as pd
import time
from setting import *


def main():

    # specific key name for sidebar
    specifc_name_sidebar = 'signaling'

    # sidebar
    with st.sidebar:

        therm_dis = st.button('Thermal_Charge_Disable',
                              key='therm_dis', use_container_width=True)
        st.session_state.text_suffix = st.text_input('suffix_file_name', "")
        run_signaling = st.button('Run', key=f'run_{specifc_name_sidebar}', use_container_width=True)

        try:
            with st.spinner("Running..."):
                if run_signaling:
                    time.sleep(1)
                    # placeholder for the real main function

            st.success("Done!")

        except:
            st.error('Absorted')


if __name__ == "__main__":
    main()
