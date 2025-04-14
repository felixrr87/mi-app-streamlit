
import streamlit as st
import pandas as pd
import numpy as np

# Configuración básica de la página
st.set_page_config(
    page_title="Analizador Deportivo",
    page_icon="🏆",
    layout="centered"
)

# Título principal
st.title("⚽ Análisis Deportivo Interactivo")
st.markdown('''
*Demostración técnica para el trabajo de implementación en Streamlit Community Cloud*
''')

# Sidebar con controles
with st.sidebar:
    st.header("Configuración")
    deporte = st.selectbox(
        "Selecciona un deporte",
        ["Fútbol", "Baloncesto", "Tenis", "Atletismo", "Natación", "Ciclismo"],
        index=0
    )
    nivel = st.slider("Tu nivel de experiencia (1-10)", 1, 10, 5)
    st.info(f"Seleccionado: {deporte} | Nivel: {nivel}/10")

# Sección de estadísticas
st.header(f"📈 Estadísticas de {deporte}")

# Datos simulados
stats = {
    'Metrica': ['Velocidad', 'Fuerza', 'Agilidad', 'Resistencia', 'Precisión'],
    'Valor': np.random.randint(30, 95, size=5)
}
df = pd.DataFrame(stats)

# Visualización
col1, col2 = st.columns(2)
with col1:
    st.dataframe(df, hide_index=True)
with col2:
    st.bar_chart(df.set_index('Metrica'))

# Explicación interactiva
with st.expander("🔍 ¿Cómo interpretar estas métricas?"):
    st.markdown('''
    Estas métricas representan:
    - **Velocidad**: Tiempo de reacción y movimiento
    - **Fuerza**: Capacidad física aplicada
    - **Agilidad**: Cambios de dirección/rítmo
    - **Resistencia**: Mantener el rendimiento
    - **Precisión**: Exactitud en ejecución
    ''')
    st.image("https://valencia90.wordpress.com/wp-content/uploads/2022/11/deporte.jpg", 
             caption=f"Ejemplo de {deporte}")

# Footer
st.divider()
st.caption("Aplicación demo")
