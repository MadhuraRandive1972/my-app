import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("my first app")
st.write("Hello Madhura, welcome to streamlit")
st.text("Let us begin")

df = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")
st.image(
    "https://imgs.search.brave.com/NXuxZwUXwmweFJFG-_a_jtdbqcu4BQCgLTUBcfVQHjc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9oaXBz/LmhlYXJzdGFwcHMu/Y29tL2htZy1wcm9k/L2ltYWdlcy8yMDI1/LWJtdy1tNC1jb3Vw/ZS1mcm9udC10aHJl/ZS1xdWFydGVycy1t/b3Rpb24tNjViOTM1/ZWE1ZGRlNi5qcGc_/Y3JvcD0wLjg4OHh3/OjAuNzUyeGg7MC4w/ODgxeHcsMC4wODY1/eGgmcmVzaXplPTcw/MDoq",
    caption="BMW M4")
upload_file = st.file_uploader("annual-enterprise-survey-2024-financial-year-provisional.csv", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)

    name = st.text_input("enter Name: ")
    if st.button("welcome"):
        st.success(f"hello,{name}")

st.header("this is a Header")
st.subheader("this is a subheader")

st.markdown("*Bold,*Italic,'code', [link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("what is your name?")
st.text_area("write something.....")
st.number_input("pick a number", min_value=0, max_value=10)
st.slider("choose a range", 0, 100)
st.selectbox("select a car", ["m4", "verna", "falcon"])
st.multiselect("choose color", ["red", "green", "blue"])
st.radio("pick One", ["option A", "Option B"])
st.checkbox("i agree to the terms and conditions")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)