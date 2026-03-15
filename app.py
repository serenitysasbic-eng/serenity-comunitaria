import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

# Configuración de la página
st.set_page_config(page_title="Serenity Nexus Comunitaria", layout="wide")

# Título y Estilo
st.title("🌱 Red Comunitaria: Felidia - Dagua")
st.markdown("### Conectando Sabores, Saberes y Turismo")

# 1. Base de datos simulada (Luego la pasaremos a un Google Sheet o JSON)
data = {
    'Zona': ['Felidia', 'La Leonera', 'Tocota', 'El Carmen', 'Dagua', 'San Bernardo', 'Alto Dagua', 'Hacienda Monte Guadua'],
    'Tipo': ['Turismo', 'Agro', 'Servicios', 'Agro', 'Turismo', 'Servicios', 'Agro', 'Proyecto Serenity'],
    'Nombre': ['Cascadas del Pato', 'Café Orgánico Familiar', 'Mecánico de Motos', 'Cosecha de Mora', 'Hotel Campestre', 'Construcciones Locales', 'Piña de Exportación', 'SNG Hub'],
    'Lat': [3.45, 3.44, 3.50, 3.55, 3.60, 3.58, 3.62, 3.48],
    'Lon': [-76.60, -76.62, -76.65, -76.68, -76.70, -76.72, -76.75, -76.63]
}
df = pd.DataFrame(data)

# 2. Barra Lateral - Filtros
st.sidebar.header("Filtros de Búsqueda")
zona_seleccionada = st.sidebar.selectbox("Selecciona una localidad:", ["Todas"] + list(df['Zona'].unique()))
tipo_seleccionado = st.sidebar.multiselect("¿Qué buscas?", df['Tipo'].unique(), default=df['Tipo'].unique())

# Filtrado de datos
df_filtrado = df[df['Tipo'].isin(tipo_seleccionado)]
if zona_seleccionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado['Zona'] == zona_seleccionada]

# 3. Diseño de la Interfaz Principal
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"📍 Resultados en {zona_seleccionada}")
    for i, row in df_filtrado.iterrows():
        with st.expander(f"{row['Nombre']} ({row['Tipo']})"):
            st.write(f"Ubicado en: **{row['Zona']}**")
            st.button(f"Contactar por WhatsApp", key=f"btn_{i}")

with col2:
    st.subheader("Mapa de la Región")
    m = folium.Map(location=[3.5, -76.6], zoom_start=10)
    for i, row in df_filtrado.iterrows():
        folium.Marker([row['Lat'], row['Lon']], popup=row['Nombre']).add_to(m)
    st_folium(m, width=500, height=400)

# 4. Pie de página y Moneda SNG
st.divider()
st.info("💡 Recuerda que puedes usar tus tokens **SNG** en comercios aliados.")