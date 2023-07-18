import streamlit as st


def keep(key):
    # Copy from temporary widget key to permanent key
    st.session_state[key] = st.session_state[f'_{key}']


def unkeep(key):
    # Copy from permanent key to temporary widget key
    st.session_state[f'_{key}'] = st.session_state[key]


def text_input(label, value, key, args=[], disabled=False):
    if key not in st.session_state:
        st.session_state[key] = str(value)

    # x = 'test', args = ['test']
    args = [key]

    unkeep(key)
    res = st.text_input(
        label, key=f'_{key}', on_change=keep, args=args, disabled=disabled)
    return res


def slider(label, min_value, max_value, step, value, key, args=[], disabled=False):
    if key not in st.session_state:
        st.session_state[key] = value

    # x = 'test', args = ['test']
    args = [key]

    unkeep(key)
    res = st.slider(label, min_value=min_value, max_value=max_value,
                    step=step, key=f'_{key}', on_change=keep, args=args, disabled=disabled)

    return res


def checkbox(label, key, args=[], disabled=False):
    if key not in st.session_state:
        st.session_state[key] = False

    # x = 'test', args = ['test']
    args = [key]

    unkeep(key)
    res = st.checkbox(
        label, key=f'_{key}', on_change=keep, args=args, disabled=disabled)

    return res


def selectbox(label, options, key, args=[], disabled=False):
    if key not in st.session_state:
        st.session_state[key] = options[0]
        st.session_state[f'index_{key}'] = 0

    # x = 'test', args = ['test']
    args = [key]

    unkeep(key)
    res = st.selectbox(label, options=options,
                       key=f'_{key}', on_change=keep, args=args, disabled=disabled)

    return res


def number_input(label, min_value, max_value, step, value, key, args=[], disabled=False):
    if key not in st.session_state:
        st.session_state[key] = value

    # x = 'test', args = ['test']
    args = [key]

    unkeep(key)
    res = st.number_input(label, min_value=min_value, max_value=max_value,
                          step=step, key=f'_{key}', on_change=keep, args=args, disabled=disabled)

    return res


def radio(label, options, key, args=[], disabled=False):
    if key not in st.session_state:
        st.session_state[key] = options[0]
        st.session_state[f'index_{key}'] = 0

    # x = 'test', args = ['test']
    args = [key]

    unkeep(key)
    res = st.radio(label, options=options,
                   key=f'_{key}', on_change=keep, args=args, disabled=disabled)

    return res
