import streamlit as st
import pandas as pd
import numpy as np

# ----------------<To run this file use command : streamlit run streamapp.py>---------------



# Title of the application
st.title('Streamlit App')

# display a simple text
st.write("This is a simple Streamlit app.")


# create a dataframe

df=pd.DataFrame({
    'first column': [1, 2, 3],
    'second column': [4, 5, 6],
})

st.write("hey, this is the dataframe")
st.write(df)


# create a line chart

chart_data=pd.DataFrame(
    np.random.rand(20,3), columns=['col 1', 'col 2', 'col 3']
)
st.line_chart(chart_data)