import streamlit as st
import pandas as pd
import plotly.express as px
from AnalizadorPacientes import AnalizadorPacientes
from Cargar_datos_csv import cargar_datos_csv
from Dinero import Dinero
from FrecuenciaConsultas import FrecuenciaConsultas
from IndicadorPaciente import IndicadorPaciente
from MargenGasto import MargenGasto
from MetaIndicador import MetaIndicador
from Paciente import Paciente

def run_app(): 
    """
    Función principal que orquesta la ejecución de la aplicación web utilizando Streamlit.
    Realiza la carga de datos, análisis y generación de visualizaciones.
    """
    st.title("Sistema de Gestión de Pacientes")
    
    # Cargar datos desde el CSV único
    pacientes, medicos = cargar_datos_csv()
    
    # Crear un DataFrame con información resumida de pacientes
    data_pacientes = []
    for i, p in enumerate(pacientes):
        st.write(f"Paciente {i}: {p}, tipo: {type(p)}")
        if not hasattr(p, 'nombre'):
            st.error(f"❌ El objeto en la posición {i} no tiene atributo 'nombre'")
            break
    
    for p in pacientes:
        data_pacientes.append({
            "Nombre": p.nombre,
            "RUT": p.rut,
            "Total Gastado": p.total_gastado(),
            "Cantidad Consultas": p.cantidad_consultas(),
            "Diagnósticos": ", ".join(p.enfermedades())
        })
    df_pacientes = pd.DataFrame(data_pacientes)
    
    st.subheader("Datos de Pacientes")
    st.dataframe(df_pacientes)
    
    st.subheader("Pacientes con gasto alto (>20.000)")
    df_high_spenders = df_pacientes[df_pacientes["Total Gastado"] > 20000]
    st.dataframe(df_high_spenders)
    
    st.subheader("Top enfermedades más comunes")
    top_enf = AnalizadorPacientes.top_enfermedades(pacientes)
    df_top_enf = pd.DataFrame(top_enf, columns=["Enfermedad", "Casos"])
    st.dataframe(df_top_enf)
    
    # Gráfico: Top enfermedades (usando Plotly)
    fig1 = px.bar(df_top_enf, x="Enfermedad", y="Casos", title="Top Enfermedades Más Comunes", text="Casos")
    st.plotly_chart(fig1)
    
    st.subheader("Indicadores personalizados")
    indicadores = [MargenGasto(), FrecuenciaConsultas()]
    data_indicadores = []
    for p in pacientes:
        row = {"Paciente": p.nombre}
        for ind in indicadores:
            row[ind.__class__.__name__] = ind.calcular(p)
        data_indicadores.append(row)
    df_indicadores = pd.DataFrame(data_indicadores)
    st.dataframe(df_indicadores)
    
    st.subheader("Gasto total del sistema")
    gasto_total = AnalizadorPacientes.gasto_total_del_sistema(pacientes)
    st.write(f"${gasto_total:,.2f}")
    
    st.subheader("Costo total por paciente")
    fig2 = px.bar(df_pacientes, x="Nombre", y="Total Gastado", title="Costo total por paciente", text="Total Gastado")
    st.plotly_chart(fig2)
    
    

if __name__ == "__main__":
    run_app()
