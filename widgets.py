import streamlit as st
import pandas as pd

st.title('Streamlit App with Text Input')

name=st.text_input('Enter your name')

if name:
    st.write(f"Hello, {name}!")

age=st.slider('Select your age',0,100,25)
st.write(f"Your age is {age}")

options=["Python","C++","Java","C","C++","Java"]
choice=st.selectbox('Select your option',options)
st.write(f"Your option is {choice}")

data={
    "Name":["John", "Jane","Jake","Jilli"],
    "Age":[20,30,54,78],
    "City":["New York","Loss Angeles","PandeyPur","Usari"]
}

df=pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)

uploaded_file = st.file_uploader("Upload your file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)