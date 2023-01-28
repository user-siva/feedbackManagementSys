import socket
import streamlit as st


def submit_form(name, reg, dept, year, feedback):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostname(), 8000))

    li = str([name, reg, dept, year, feedback])

    client.send(li.encode())

    client.close()


st.title("Feedback Management")
st.subheader("Enter Details below:")

with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter your Name:")
    register = st.text_input("Enter your Register Number:")
    dept = st.text_input("Enter your Department:")
    year = st.text_input("Enter your Year:")
    feedback = st.text_area("Enter your feedback:")
    submit = st.form_submit_button("Submit")

if submit:
    submit_form(name, register, dept, year, feedback)
