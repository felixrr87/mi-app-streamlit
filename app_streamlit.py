
import streamlit as st

st.title("Mi App de Streamlit para el Trabajo 📊")
st.write("Esta es una app de ejemplo para deportes.")

# Ejemplo interactivo
deporte = st.selectbox("¿Cuál es tu deporte favorito?", ["Fútbol", "Baloncesto", "Tenis", "Otro"])
if deporte:
    st.success(f"¡Genial! Te gusta el {deporte} ⚽🏀🎾")
