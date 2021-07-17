from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    var = st.slider("Varianza", 0, 10, 1)

    arr = np.random.normal(1, var, size=1000)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig, width=20)  