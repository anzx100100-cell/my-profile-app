import streamlit as sl
from streamlit-gsheets import GSheetsConnection
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
    existing_data=conn.read(ttl=0)
    new_entry={
        "name":[name],
        "age":[age],"bio":[bio]}
    updated_df=existing_date._append(new_entry,ignore_index=True) if not existing_date.empty else new_entry
    conn.update(data=updated_df)
 if "profile" in sl.session_state:
    sl.divider()
    sl.subheader(f"profile card :{sl.session_state.profile["name"]}")
    sl.write(f"**Age**: {sl.session_state.profile["age"]}")
    sl.write(f"**bio**:{sl.session_state.profile["bio"]}")
