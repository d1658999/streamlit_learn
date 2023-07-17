import streamlit as st
import numpy as np
import pandas as pd


def main():
    st.set_page_config(
        page_title="Meta_GUI",
        page_icon="👋",
    )

    st.write("# Welcome to use Meta_GUI! 👋")

    st.sidebar.success("Select a function you want above.")

    st.markdown(
        """
        Meta GUI is friendly interface for those who want to test quickly on some RATs and get basic performance
        **👈 Select a function from the sidebar** to activate the function page you want to use
        ### Want to learn more?
        - Check out []()
        - Jump into our []()
        - Ask a question in our []()
        ### See more complex demos
        - Use a neural net to []()
        - Explore a []()
        """
    )


if __name__ == "__main__":
    main()
