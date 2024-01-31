import streamlit as st
import pandas as pd
import numpy as np
from utils_data import *
st.set_page_config(
    page_title="📊 Transformateur de données",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
)
if "file" not in st.session_state :
    st.session_state.file = None
st.title("📊 Transformateur de données")

formats = ["csv","xlsx"]

selected_format = st.radio('\n \nFormat', formats, horizontal=True)
file = st.file_uploader("Importer vos données ici", type=[selected_format])

if file is not None:
    df = load_data(file,selected_format)
    df.dropna(inplace=True)
    with st.expander("Afficher les données"):
        st.dataframe(df)
   
    with st.sidebar: 
        st.header("Choisir les données à transformer")
        station = st.selectbox("Station",df.station.unique())
        param = st.selectbox("Paramètre",df.drop(['code', 'station', 'annee', 'mois', 'jours'], axis=1).columns)
        entete = st.text_input("Entête",value="Entête")
        submit_button = st.button(label='Valider')
    if submit_button :
        df = get_data(df,station,param)
        data = transform_data(df)
        with st.expander("Afficher les données transformées"):
            st.dataframe(data)
        st.sidebar.header("Enregistrer les données transformées")
        name = st.sidebar.text_input("Nom du fichier",value=f"{station}_{param}")
        data.to_csv(f"{name}.txt", sep="\t",index=False)
        with open(f"{name}.txt", 'r+') as f: 
            contenu_initial = f.read()
            f.seek(0, 0)
            f.write(f"{str(entete)}\n" + contenu_initial)
        f_mod = contenu_initial.replace('.0', '')
        with open(f"{name}.txt", 'w') as f: 
            f.write(f_mod)
        with open(f"{name}.txt", 'r+') as f:
            st.session_state.file = f"{name}.txt"
            st.sidebar.download_button('Télecharger', f, file_name=st.session_state.file )
            st.success("Données enregistrées avec succès")
            f.close()
        
