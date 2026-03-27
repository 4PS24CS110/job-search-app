import streamlit as st
from scraper import get_jobs

st.title("💼 Smart AI Job Search App")

# INPUTS
job = st.text_input("Enter job role (python, developer, engineer)")
location = st.text_input("Enter location (India / USA / Remote)")

experience = st.selectbox(
    "Experience Level",
    ["Any", "Junior", "Mid", "Senior"]
)

# SEARCH BUTTON
if st.button("Search"):
    st.write("🔍 Searching jobs...")

    jobs = get_jobs(job, location, experience)

    st.write("### Jobs Found:")

    for j in jobs:
        st.markdown(
            f"""
            <div style="
                padding:15px;
                border-radius:10px;
                background-color:#f5f5f5;
                margin-bottom:10px;
                border:1px solid #ddd;
            ">
                <h4>{j['title']}</h4>
                <p><b>{j['company']}</b></p>
                <p>{j['location']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )