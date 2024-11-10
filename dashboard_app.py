import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Función para cargar y mostrar cada gráfico Matplotlib
def show_chart(file_path, title, chart_type="bar", x_col=None, y_col=None):
    data = pd.read_csv(file_path)

    # Crear gráfico usando Matplotlib según el tipo de gráfico especificado
    fig, ax = plt.subplots()

    if chart_type == "bar" and x_col and y_col:
        ax.bar(data[x_col], data[y_col], color="skyblue")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{title}")
    elif chart_type == "line" and x_col and y_col:
        ax.plot(data[x_col], data[y_col], marker="o", color="green")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{title}")
    elif chart_type == "pie" and x_col and y_col:
        ax.pie(data[y_col], labels=data[x_col], autopct="%1.1f%%", startangle=90)
        ax.set_title(f"{title}")
        ax.axis("equal")  # Asegurar que el gráfico de pastel sea circular

    st.pyplot(fig)

    # Mostrar la tabla de datos al hacer clic en el botón
    if st.button(f"Mostrar datos para {title}"):
        st.write(f"**Datos del Dashboard: {title}**")
        st.dataframe(data)

# Título de la aplicación
st.title("Tableros de Control y OKRs de Huawei")

# Tablero 1: Fortalecer la inteligencia de mercado
st.header("1. Fortalecer la inteligencia de mercado")
okr_1 = "Incrementar el número de insights accionables de mercado en un 25% en el próximo año."
desc_1 = "Este tablero permite a Huawei anticipar necesidades de los clientes al monitorear los insights generados en cada región."
st.write(f"### OKR: {okr_1}")
st.write(desc_1)
show_chart("intelligence_market_data.csv", "Insights Generados por Región", chart_type="bar", x_col="Region", y_col="Insights_Generated")

# Tablero 2: Monitorear innovaciones tecnológicas de la competencia
st.header("2. Monitorear innovaciones tecnológicas de la competencia")
okr_2 = "Aumentar la frecuencia de informes sobre tecnología emergente en un 40% para el fin del año fiscal."
desc_2 = "Este tablero facilita el monitoreo de innovaciones tecnológicas y la velocidad de respuesta estratégica."
st.write(f"### OKR: {okr_2}")
st.write(desc_2)
show_chart("tech_innovation_data.csv", "Tiempo de Respuesta por ID de Innovación", chart_type="line", x_col="Innovation_ID", y_col="Time_To_Response_Days")

# Tablero 3: Incrementar la captación de datos externos en mercados clave
st.header("3. Incrementar la captación de datos externos en mercados clave")
okr_3 = "Alcanzar un 90% de cobertura de datos de mercado clave en regiones objetivo."
desc_3 = "Este tablero ayuda a Huawei a comprender mejor los datos del mercado y mejorar la calidad de la información obtenida."
st.write(f"### OKR: {okr_3}")
st.write(desc_3)
show_chart("data_capture_data.csv", "Cobertura de Datos por Mercado", chart_type="pie", x_col="Market", y_col="Coverage_Percentage")

# Tablero 4: Expandir la cartera de productos personalizados
st.header("4. Expandir la cartera de productos personalizados")
okr_4 = "Aumentar la cantidad de productos personalizados en un 30% dentro de 18 meses."
desc_4 = "Este tablero permite visualizar el progreso en el desarrollo de productos personalizados para satisfacer demandas locales."
st.write(f"### OKR: {okr_4}")
st.write(desc_4)
show_chart("custom_products_data.csv", "Satisfacción del Cliente por Mercado", chart_type="bar", x_col="Market", y_col="Customer_Satisfaction_Score")

# Tablero 5: Mejorar la eficiencia en la toma de decisiones de inversión en nuevas tecnologías
st.header("5. Mejorar la eficiencia en la toma de decisiones de inversión en nuevas tecnologías")
okr_5 = "Reducir el tiempo de evaluación de nuevas inversiones tecnológicas en un 20%."
desc_5 = "Este tablero muestra los tiempos de decisión para nuevas inversiones y su retorno sobre la inversión."
st.write(f"### OKR: {okr_5}")
st.write(desc_5)
show_chart("investment_decision_data.csv", "Tiempo Promedio de Decisión por ID de Inversión", chart_type="line", x_col="Investment_ID", y_col="Average_Decision_Time_Days")

# Tablero 6: Ampliar las colaboraciones estratégicas para acelerar la innovación
st.header("6. Ampliar las colaboraciones estratégicas para acelerar la innovación")
okr_6 = "Establecer cinco nuevas colaboraciones estratégicas con centros de investigación en un año."
desc_6 = "Este tablero detalla las colaboraciones activas y su impacto en la innovación de Huawei."
st.write(f"### OKR: {okr_6}")
st.write(desc_6)
show_chart("collaborations_data.csv", "Impacto de la Innovación por Institución", chart_type="bar", x_col="Institution", y_col="Innovation_Impact")

# Tablero 7: Optimizar la estructura organizativa
st.header("7. Optimizar la estructura organizativa para mejorar la flexibilidad y descentralización")
okr_7 = "Aumentar el nivel de autonomía en subsidiarias clave en un 50% dentro de 2 años."
desc_7 = "Este tablero muestra el índice de autonomía y su impacto financiero por subsidiaria."
st.write(f"### OKR: {okr_7}")
st.write(desc_7)
show_chart("organizational_structure_data.csv", "Índice de Autonomía por Subsidiaria", chart_type="pie", x_col="Subsidiary", y_col="Autonomy_Index")

# Tablero 8: Integrar sistemas digitales para mejorar la colaboración
st.header("8. Integrar sistemas digitales para mejorar la colaboración interdepartamental")
okr_8 = "Implementar una plataforma de colaboración interdepartamental en toda la empresa en un año."
desc_8 = "Este tablero muestra el nivel de uso y la satisfacción de los empleados con la plataforma colaborativa."
st.write(f"### OKR: {okr_8}")
st.write(desc_8)
show_chart("collaboration_system_data.csv", "Frecuencia de Uso por Departamento", chart_type="bar", x_col="Department", y_col="Usage_Frequency")

# Tablero 9: Fortalecer la cultura de innovación y colaboración
st.header("9. Fortalecer la cultura de innovación y colaboración")
okr_9 = "Incrementar la participación en programas de innovación en un 40% para el próximo año."
desc_9 = "Este tablero muestra la cantidad de proyectos de innovación iniciados y su alineación estratégica."
st.write(f"### OKR: {okr_9}")
st.write(desc_9)
show_chart("innovation_culture_data.csv", "Proyectos de Innovación por Departamento", chart_type="bar", x_col="Department", y_col="Innovation_Projects")
