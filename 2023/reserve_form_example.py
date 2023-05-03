import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import requests
from sqlalchemy import create_engine
import psycopg2

st.set_page_config(
    page_title="The warung",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.google.com",
        'About': "THANKS..!!"
    }
)

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(https://i.im.ge/2022/12/08/SH9b7h.bckgrnd.png);
             background-repeat: no-repeat;
             background-size: 1340px 1120px;
             background-position: center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

st.title('WARUNG KANG OJON')

col1, col2, col3 = st.columns(3)
with col1:
#    st.header("A cat")
   st.image("https://i.im.ge/2022/12/08/SHfBPm.abc.jpg")

with col2:
#    st.header("A dog")
   st.image("https://i.im.ge/2022/12/08/SHkXQc.bcd.jpg")

with col3:
   st.write("""Warung Kang Ojon telah berdiri sejak 1976 hingga saat ini. 
                Kami bergerak dibidang mengelolah makanan yang spesifik 
                yaitu Minang dan Melayu, dimana alasan untuk mendirikan 
                rumah makan ini adalah merupakan hasil survey bahwa masih 
                kurangnya sarana rumah makan terutama yang menyediakan makanan 
                spesifik Minang dan Melayu dikota Medan.""")

st.subheader('Our Best Menu')
col11, col22, col33 = st.columns(3)
with col11:

    st.subheader('MegalUDON')
    st.image("https://i.im.ge/2022/12/08/SHBcxz.images-mancanegara-udon-udon-kuah.jpg")
    with st.expander("Info detail:"):
         st.write("""
         Udon gurih dan pedas seperti omongan tetangga
        """)
with col22:
    st.subheader('TOASTimoni')
    st.image("https://i.im.ge/2022/12/08/SHBZk9.roti-bakar-sederhana.jpg")
    with st.expander("Info detail:"):
         st.write("""
         Roti dibakar dengan amarahmu
        """)
with col33:
    st.subheader('COFFEEkirin')
    st.image("https://i.im.ge/2022/12/08/SHBVFX.resep-es-kopi-susu-img.jpg")
    with st.expander("Info detail:"):
         st.write("""
         Kopi dari atlantis dengan susu yg manis seperti senyumanmu
        """)
with st.expander("want to reserve?"):
    st.subheader ('Reservation form')
    nama = st.text_input('Nama pemesan')
    email = st.text_input('alamat email pemesan')
    telp = st.text_input('nomor HP pemesan')
    anggota =  st.radio('jumlah tamu',
                          ('1-2', '3-4', '5-6','lebih dari 6'))
    tanggal = st.date_input('tanggal reservasi')
    
    data = {'nama': nama,
        'email' : email,
        'telp':telp,
        'anggota' :anggota,
        'tanggal' : tanggal
          }

    if st.button('submit'):
        my_conn = create_engine("postgresql+psycopg2://postgres:irfan12345@localhost:5432/store")
        dbConnection    = my_conn.connect()
        data = pd.DataFrame([data])
        data.to_sql(con=my_conn,name='KTR_2',if_exists='append')
        st.text('Data sudah disimpan')
    else:
        st.write('click to submit')

data = {'nama': nama,
        'email' : email,
        'telp':telp,
        'anggota' :anggota,
        'tanggal' : tanggal
          }


col111, col222, col333 = st.columns(3)
with col111:
    st.subheader('Warung Kang Ojon')
    st.write("""
         Warung Kang Ojon telah berdiri sejak 1976 hingga saat ini. 
         Kami bergerak dibidang mengelolah makanan yang spesifik yaitu Minang dan Melayu
        """)
with col222:
    st.subheader('Open Hours')
    st.write("""
        Senin-Jumat: 09.00-22.00  
        Sabtu-Minggu: 08.00-23.00   
        """)
with col333:
    st.subheader('Our location')
    st.write("""
        Ruko Dinosaurus Jalan Gunung Purba No.69, Amazon, Wakanda
        (81)-987654
        warungkangojon@gmail.com   
        """)



