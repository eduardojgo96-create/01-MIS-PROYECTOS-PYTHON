import streamlit as st

# 1. Configuración de la pestaña del navegador
st.set_page_config(
    page_title="Portafolio Profesional | Ingeniero Industrial, Desarrollador Python", 
    page_icon="💻", 
    layout="centered"
)

# 2. Encabezado Principal y Perfil Profesional
st.title("¡Hola! 👋 Soy Eduardo Gutiérrez Olavarría")
st.subheader("Ingeniero Civil Industrial, Desarrollador Python enfocado en Soluciones Eficientes")

st.write("""
Apasionado por la resolución de problemas a través del código y la automatización. 
Actualmente enfocado en el desarrollo de software limpio, análisis de datos y creación 
de aplicaciones web interactivas utilizando el ecosistema de Python.
""")

# 3. Canales oficiales de Contacto Directo
st.markdown("### 📬 Conectemos")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("📧 **Correo:** [eduardo.jgo96@email.com](mailto:eduardo.jgo96@email.com)")
with col2:
    st.markdown("🔗 **LinkedIn:** [Mi Perfil Profesional](https://www.linkedin.com/in/eduardogutierrezolavarria/)")
with col3:
    st.markdown("🐙 **GitHub:** [Mis Repositorios](https://github.com)")

st.markdown("---")

# 4. Habilidades Técnicas Organizadas por Categorías
st.markdown("### 🛠️ Tecnologías y Herramientas")
st.write("**Lenguajes:** Python, SQL")
st.write("**Frameworks y Librerías:** Streamlit, Pandas, NumPy, FastAPI")
st.write("**Herramientas:** Microsoft Excel, Microsoft Power BI, VS Code")

st.markdown("---")

# 5. Sección de Proyectos Destacados (Estructura STAR: Situación, Tarea, Acción, Resultado)
st.markdown("### 🚀 Proyectos Destacados")

# Proyecto 1
st.markdown("#### 📦 1. Sistema de Automatización de Datos")
st.write("""
**Descripción:** Script optimizado que procesa grandes volúmenes de datos comerciales. 
Automatiza reportes semanales reduciendo errores manuales.
""")
st.caption("🔧 **Tecnologías:** Python, Pandas, OpenPyXL, Git")
st.markdown("[🔗 Ver Código en GitHub](https://github.com/proyecto-1)")

st.write("") # Espacio en blanco

# Proyecto 2
st.markdown("#### 📊 2. Dashboard Interactivo de Visualización")
st.write("""
**Descripción:** Aplicación web que permite a usuarios no técnicos cargar archivos CSV 
y visualizar gráficos métricos en tiempo real de forma intuitiva.
""")
st.caption("🔧 **Tecnologías:** Python, Streamlit, Plotly, CSS")
st.markdown("[🔗 Ver Código en GitHub](https://github.com/proyecto-2)")

st.markdown("---")

# 6. Información adicional relevante
st.markdown("### 🎓 Educación y Logros")
st.write("• **Ingeniería Civil Industrial mención Bioprocesos** - Universidad de La Frontera, 2026")
st.write("• Certificación en Python Avanzado / Análisis de Datos - [Plataforma de cursos]")
