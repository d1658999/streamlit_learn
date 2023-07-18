import streamlit as st
import numpy as np
import pandas as pd
import time
from setting import keep, unkeep, checkbox, selectbox, number_input


def main():
    # if 'test1_checkbox' not in st.session_state:
    #     st.session_state.test1_checkbox = False

    # unkeep('test1_checkbox')
    # st.checkbox('test', key='_test1_checkbox', on_change=keep, args=['test1_checkbox'])
    selectbox('Inst', options=['cmw100', 'cmw200'],
              key='inst_test')
    # st.selectbox('Inst', options=['cmw100', 'cmw200'], key='aaa')
    number_input('num_input_test', min_value=0.0, max_value=5.0,
                 step=0.5, value=1.5, key='num_inp')
    print(st.session_state)


if __name__ == "__main__":
    main()
