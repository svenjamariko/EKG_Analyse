import streamlit as st
import numpy as np
import matplotlib as plt

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox, das Ergebnis wird in current_user gespeichert
current_user = st.selectbox(
    'Versuchsperson',
    options = ["Nutzer1", "Nutzer2"], key="sbVersuchsperson")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'
st.write("Der Name ist: ", st.session_state.current_user) 
 