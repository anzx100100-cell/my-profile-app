import streamlit as sl
conn=sl.connection("gsheets",type=GSheetsConnection)
with sl.form("your profile"):
    name=sl.text_input("what is your name")
    age=sl.number_input("Age",min_value=1 ,max_value=120,value=16)
    bio=sl.text_area("short bio")
    submitted=sl.form_submit_button("save profile")
if submitted:
    sl.session_state.profile={
    "name":name,
    "age":age,
    "bio":bio

    }
    sl.success("profile saves successfully")
    sl.balloons()
if "profile" in sl.session_state:
    sl.divider()
    sl.subheader(f"profile card :{sl.session_state.profile["name"]}")
    sl.write(f"**Age**: {sl.session_state.profile["age"]}")
    sl.write(f"**bio**:{sl.session_state.profile["bio"]}")
