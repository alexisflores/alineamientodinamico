import streamlit as st
import pandas as pd

# Función para cargar y mostrar cada tablero junto con su OKR
def load_dashboard(file_path, okr, description):
    data = pd.read_csv(file_path)
    st.write(f"### OKR: {okr}")
    st.write(description)
    st.write("**Datos del Dashboard:**")
    st.dataframe(data)

# Título de la aplicación
st.title("Tableros de Control y OKRs de Huawei")

# Tablero 1: Fortalecer la inteligencia de mercado
st.header("1. Fortalecer la inteligencia de mercado")
okr_1 = "Incrementar el número de insights accionables de mercado en un 25% en el próximo año."
desc_1 = "Este tablero permite a Huawei anticipar necesidades de los clientes al monitorear los insights generados en cada región."
load_dashboard("intelligence_market_data.csv", okr_1, desc_1)

# Tablero 2: Monitorear innovaciones tecnológicas de la competencia
st.header("2. Monitorear innovaciones tecnológicas de la competencia")
okr_2 = "Aumentar la frecuencia de informes sobre tecnología emergente en un 40% para el fin del año fiscal."
desc_2 = "Este tablero facilita el monitoreo de innovaciones tecnológicas y la velocidad de respuesta estratégica."
load_dashboard("tech_innovation_data.csv", okr_2, desc_2)

# Tablero 3: Incrementar la captación de datos externos en mercados clave
st.header("3. Incrementar la captación de datos externos en mercados clave")
okr_3 = "Alcanzar un 90% de cobertura de datos de mercado clave en regiones objetivo."
desc_3 = "Este tablero ayuda a Huawei a comprender mejor los datos del mercado y mejorar la calidad de la información obtenida."
load_dashboard("data_capture_data.csv", okr_3, desc_3)

# Tablero 4: Expandir la cartera de productos personalizados
st.header("4. Expandir la cartera de productos personalizados")
okr_4 = "Aumentar la cantidad de productos personalizados en un 30% dentro de 18 meses."
desc_4 = "Este tablero permite visualizar el progreso en el desarrollo de productos personalizados para satisfacer demandas locales."
load_dashboard("custom_products_data.csv", okr_4, desc_4)

# Tablero 5: Mejorar la eficiencia en la toma de decisiones de inversión
st.header("5. Mejorar la eficiencia en la toma de decisiones de inversión")
okr_5 = "Reducir el tiempo de evaluación de nuevas inversiones tecnológicas en un 20%."
desc_5 = "Este tablero muestra los tiempos de decisión para nuevas inversiones y su retorno sobre la inversión."
load_dashboard("investment_decision_data.csv", okr_5, desc_5)

# Tablero 6: Ampliar colaboraciones estratégicas
st.header("6. Ampliar colaboraciones estratégicas")
okr_6 = "Establecer cinco nuevas colaboraciones estratégicas con centros de investigación en un año."
desc_6 = "Este tablero detalla las colaboraciones activas y su impacto en la innovación de Huawei."
load_dashboard("collaborations_data.csv", okr_6, desc_6)

# Tablero 7: Optimizar la estructura organizativa
st.header("7. Optimizar la estructura organizativa")
okr_7 = "Aumentar el nivel de autonomía en subsidiarias clave en un 50% dentro de 2 años."
desc_7 = "Este tablero muestra el índice de autonomía y su impacto financiero por subsidiaria."
load_dashboard("organizational_structure_data.csv", okr_7, desc_7)

# Tablero 8: Integrar sistemas digitales para mejorar la colaboración
st.header("8. Integrar sistemas digitales para mejorar la colaboración")
okr_8 = "Implementar una plataforma de colaboración interdepartamental en toda la empresa en un año."
desc_8 = "Este tablero muestra el nivel de uso y la satisfacción de los empleados con la plataforma colaborativa."
load_dashboard("collaboration_system_data.csv", okr_8, desc_8)

# Tablero 9: Fortalecer la cultura de innovación y colaboración
st.header("9. Fortalecer la cultura de innovación y colaboración")
okr_9 = "Incrementar la participación en programas de innovación en un 40% para el próximo año."
desc_9 = "Este tablero muestra la cantidad de proyectos de innovación iniciados y su alineación estratégica."
load_dashboard("innovation_culture_data.csv", okr_9, desc_9)
