import streamlit as st
import numpy as np
import matplotlib as plt

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox
current_user = st.selectbox(
    'Versuchsperson',
    options = ["Name", "..."], key="sbName")