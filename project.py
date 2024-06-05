import streamlit as st

st.set_page_config(
    page_title="Website Portofolio",
    layout="wide"
)

linkedInURL = "www.linkedin.com/in/ricky-andriadi"

st.markdown("<h1 style='text-align: center; color: black;'>PORTOFOLIO PAGE</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")

cols_first = st.columns([0.17, 0.05, 0.2, 0.8])
with cols_first[0]:
    st.image("Foto_Pajang.jpg")
with cols_first[2]:
    st.subheader("Name :")
    st.subheader("Email :")
    st.subheader("LinkedIn :")
with cols_first[3]:
    st.subheader("Ricky Andriadi S.")
    st.subheader("rickyandriadi12@gmail.com")
    st.subheader("[Ricky Andriadi](%s)" % linkedInURL)

st.write("")
st.write("")    
st.header("About Me :")
st.write("My name is Ricky Andriadi Sembiring. A graduate of Nutrition Feed from Animal Husbandry Faculty, Padjadjaran University 2022. Expertise in SQL database, Excel, Python, and Streamlit. Familiar with Tableau and Looker.")
st.write("I love learning everyday, upgrading and adding skills to my arsenal. Moreover those related to Data. Searching and gaining insights from a database are like solving a puzzle and it's fun!")

pr1 = "https://amtiss-project-3qwanqydsz7wadvng9xgtm.streamlit.app/"
pr2 = "https://capstone-project-dqlab-wa5at5toyaq4wzrv3suabl.streamlit.app/"
pr3 = "https://dashboardsalesdairy-ras.streamlit.app/"
pr4 = "https://deploysuperstoredashboard-7jkm6qburkjwbxdj7m7wh8.streamlit.app/"
pr5 = "https://salesanalystproject-ras.streamlit.app/"

st.write("")    
st.write("")    
st.header("Projects :")
st.write("[LMA Asset Productivity and Maintenance Monitoring Dashboard](%s)"%pr1)
st.write("[Chicken Meat Sufficiency in Indonesia Report](%s)"%pr2)
st.write("[Dashboard Sales](%s)"%pr3)
st.write("[Dashboard Superstore](%s)"%pr4)
st.write("[Sales Analyst](%s)"%pr5)