import streamlit as st

st.header('Lanzar una moneda')
# Widget control deslizante para seleccionar el número de intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# Botón para iniciar el experimento
start_button = st.button('Ejecutar')

# Lógica para ejecutar cuando se presiona el botón
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    
st.write('Esta aplicación aún no es funcional. En construcción.')
