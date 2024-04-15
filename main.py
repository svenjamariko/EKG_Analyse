import streamlit as st
import numpy as np
import matplotlib as plt
import read_data as rd
from PIL import Image


person_dict = rd.load_person_data()
person_names = rd.get_person_list(person_dict)
print(person_names)

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")


# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'
else:
    st.write("Der Name ist: ", st.session_state.current_user) 


# Eine Auswahlbox, das Ergebnis wird in current_user gespeichert
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

current_person = find_person_data_by_name(st.session_state.current_user)
current_picture_path = current_person["picture_path"]
 

# Laden eines Bilds
image = Image.open(current_picture_path)
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.current_user)

if __name__ == '__main__':
    current_person = find_person_data_by_name(st.session_state.current_user)
    current_picture_path = current_person["picture_path"]
    print(current_picture_path)