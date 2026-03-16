from supabase import create_client, Client

# Inicializar conexión con Supabase usando los Secretos
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# Función para guardar una publicación
def guardar_publicacion(nombre, zona, descripcion, url_imagen, whatsapp):
    data = {
        "nombre": nombre,
        "zona": zona,
        "descripcion": descripcion,
        "url_imagen": url_imagen,
        "whatsapp": whatsapp,
        "fecha": str(datetime.now())
    }
    supabase.table("publicaciones").insert(data).execute()



import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN DE MARCA ---
st.set_page_config(page_title="Serenity Nexus - Comunidad", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f1; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFAZ DE USUARIO ---
st.title("🏔️ Serenity Nexus: La Red de nuestra Tierra")
st.sidebar.image("https://via.placeholder.com/150", caption="Serenity S.A.S BIC") # Aquí irá tu logo

menu = ["Ver Muro Comunitario", "Publicar mi Servicio/Producto", "Mapa de la Zona"]
choice = st.sidebar.selectbox("Menú", menu)

if choice == "Publicar mi Servicio/Producto":
    st.header("📸 Crea tu publicación")
    st.info("Sube tu contenido para que el mundo conozca lo que ofreces en Felidia, Dagua y alrededores.")
    
    with st.form("form_publicacion", clear_on_submit=True):
        nombre = st.text_input("¿Cómo se llama tu negocio/servicio?")
        zona = st.selectbox("¿En qué zona estás?", ["Felidia", "La Leonera", "Tocota", "El Carmen", "Dagua", "San Bernardo", "Alto Dagua"])
        descripcion = st.text_area("Cuéntanos más (detalles, precios, historia)")
        
        # Carga de Archivos
        foto = st.file_uploader("Sube una foto o video corto", type=["jpg", "png", "mp4"])
        whatsapp = st.text_input("Tu número de WhatsApp (ej: 57311...)")
        
        submit = st.form_submit_button("Publicar al Mundo")
        
        if submit:
            if nombre and foto:
                st.success(f"¡Gracias {nombre}! Tu publicación está siendo procesada para el muro de {zona}.")
                # AQUÍ CONECTAREMOS LA BASE DE DATOS EN EL SIGUIENTE PASO
            else:
                st.error("Por favor sube al menos una foto y el nombre.")

elif choice == "Ver Muro Comunitario":
    st.header("📰 Muro de la Comunidad")
    # Simulando el "Feed" tipo Instagram
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://via.placeholder.com/600x400", caption="Ejemplo: Café en El Carmen")
        st.subheader("Café Altura Real")
        st.write("Producido a 1800msnm. ¡Pide el tuyo!")
        st.button("Contactar por WhatsApp", key="1")

    with col2:
        st.image("https://via.placeholder.com/600x400", caption="Ejemplo: Turismo en Felidia")
        st.subheader("Senderos del Pato")
        st.write("Guianza especializada por el río. $20.000 por persona.")
        st.button("Contactar por WhatsApp", key="2")
        
