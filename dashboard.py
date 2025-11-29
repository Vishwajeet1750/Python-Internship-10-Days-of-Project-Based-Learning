import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("MY PROFILE")
st.text("Welcome to our dashboard")
st.header("I am Vishwajeet")
st.write("You can write", 10 + 5)

name = st.text_input("Enter your name : ")
age = st.number_input("Enter your age : ")
st.write("Your name is :", name, "Your age is : ", age)

# Radio Button
gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
st.write("Selected gender:", gender)

# Date Input
dob = st.date_input("Select your Birth Date:")
st.write("Your Birth Date is:", dob)

st.selectbox("Enter your course : ", ["BCA", "B.TECH", "MCA"])

if st.button("Click ME"):
    st.success("Clicked Button")

# File Upload
file = st.file_uploader("Upload your file")
if file:
    content = file.read()
    st.write("File Uploaded Successfully!")

# Chat Input
message = st.chat_input("Type your message...")
if message:
    st.write("You said:", message)

# HTML Component
st.html("""
<div style="padding:15px; background:#222; border-radius:10px; margin-top:20px;">
    <h3 style="color:#00eaff; text-align:center;">Welcome to the HTML Section</h3>
    <p style="color:white; text-align:center;">This is custom HTML inside Streamlit.</p>
</div>
""")

# DataFrame
data = {"Name": ["Yash", "Aryan", "Vishu", "Ram", "Mayank"], "Marks": [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
st.dataframe(df)

# Charts
data = pd.DataFrame({"Marks": [10, 20, 30, 40, 50]})
st.line_chart(data)
st.bar_chart(data)

# Pie Chart using Matplotlib
subject = ["Python", "C++", "Java"]
Marks = [20, 10, 5]

fig, ax = plt.subplots()
ax.pie(Marks, labels=subject, autopct='%1.1f%%', startangle=90)
ax.axis("equal")
st.pyplot(fig)
