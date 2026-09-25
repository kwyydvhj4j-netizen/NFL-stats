import streamlit as st
import pandas as pd

st.title("NFL Stats & Momios")

@st.cache_data
def cargar_datos():
    # Enlace directo al archivo oficial de resultados y líneas de Las Vegas
    url = "https://github.com/nflverse/nflverse-data/releases/download/games/games.csv"
    df = pd.read_csv(url)
    return df

st.write("Conectando con nflverse...")
df = cargar_datos()

st.success(f"¡Base de datos conectada! Total de partidos procesados: {len(df)}")
st.write("El motor está vivo. Si ves este mensaje en tu pantalla, tu app ya tiene los datos reales sin depender de ninguna IA.")
