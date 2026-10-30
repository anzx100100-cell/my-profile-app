import pandas as pd
import streamlit as sl
from streamlit_gsheets import GSheetsConnection
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
    existing_data=conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/19ZlE_OhH57PgoH5j_4eJ6-QWxxh7JRKB6ea8F_47gAk/edit?gid=0#gid=0",ttl=0)
    new_entry={
        "name":[name],
        "age":[age],"bio":[bio]}
    new_df=pd.DataFrame(new_entry)
    updated_df=pd.concat([existing_data,new_df],ignore_index=True) if not existing_data.empty else new_df
    conn.update(spreadsheet="https://docs.google.com/spreadsheets/d/19ZlE_OhH57PgoH5j_4eJ6-QWxxh7JRKB6ea8F_47gAk/edit?gid=0#gid=0",worksheet="اsheet1",data=updated_df)
if "profile" in sl.session_state:
    sl.divider()
    sl.subheader(f"profile card :{sl.session_state.profile["name"]}")
    sl.write(f"**Age**: {sl.session_state.profile["age"]}")
    sl.write(f"**bio**:{sl.session_state.profile["bio"]}")
