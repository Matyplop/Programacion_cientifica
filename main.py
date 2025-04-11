import streamlit as st
import pandas as pd
import plotly.express as px
import traceback
 
from AnalizadorPacientes import AnalizadorPacientes
from Cargar_datos_csv import cargar_datos_csv
from MetaIndicador import FrecuenciaConsultas, MargenGasto
from MetaIndicador import MargenGasto, FrecuenciaConsultas
 

def run_app():
     try:
         st.title("Sistema de Gestión de Pacientes")
         # resto del código
         st.title("🩺 Sistema de Gestión de Pacientes")
         st.write("⏳ Iniciando app...")
 
         # Cargar datos
         st.write("📥 Cargando datos desde CSV...")
         pacientes, medicos = cargar_datos_csv()
         st.write(f"✅ Se cargaron {len(pacientes)} pacientes y {len(medicos)} médicos.")
 
         # Mostrar pacientes
         data_pacientes = []
         for p in pacientes:
             data_pacientes.append({
                 "Nombre": p.nombre,
                 "RUT": p.rut,
                 "Total Gastado": p.total_gastado(),
                 "Cantidad Consultas": p.cantidad_consultas(),
                 "Diagnósticos": ", ".join(p.enfermedades())
             })
         df_pacientes = pd.DataFrame(data_pacientes)
 
         st.subheader("📋 Datos de Pacientes")
         st.dataframe(df_pacientes)
 
         # Pacientes con gasto alto
         st.subheader("💸 Pacientes con gasto alto (>20.000)")
         df_high_spenders = df_pacientes[df_pacientes["Total Gastado"] > 20000]
         st.dataframe(df_high_spenders)
 
         # Enfermedades más comunes
         st.subheader("🦠 Top enfermedades más comunes")
         top_enf = AnalizadorPacientes.top_enfermedades(pacientes)
         df_top_enf = pd.DataFrame(top_enf, columns=["Enfermedad", "Casos"])
         st.dataframe(df_top_enf)
 
         fig1 = px.bar(df_top_enf, x="Enfermedad", y="Casos",
                       title="Top Enfermedades Más Comunes", text="Casos")
         st.plotly_chart(fig1)
 
         # Indicadores personalizados
         st.subheader("📊 Indicadores personalizados")
         indicadores = [MargenGasto(), FrecuenciaConsultas()]
         data_indicadores = []
         for p in pacientes:
             row = {"Paciente": p.nombre}
             for ind in indicadores:
                 row[ind.__class__.__name__] = ind.calcular(p)
             data_indicadores.append(row)
         df_indicadores = pd.DataFrame(data_indicadores)
         st.dataframe(df_indicadores)
 
         # Gasto total
         st.subheader("🧾 Gasto total del sistema")
         gasto_total = AnalizadorPacientes.gasto_total_del_sistema(pacientes)
         st.write(f"💰 ${gasto_total:,.2f}")
 
         # Costo por paciente
         st.subheader("📈 Costo total por paciente")
         fig2 = px.bar(df_pacientes, x="Nombre", y="Total Gastado",
                       title="Costo total por paciente", text="Total Gastado")
         st.plotly_chart(fig2)
 
         st.success("✅ App cargada completamente.")
 
     except Exception as e:
         st.error(f"❌ Error al ejecutar la app: {e}")
         import traceback
         st.error("❌ Error durante la ejecución de la app:")
         st.text(traceback.format_exc())
   
     st.title("Sistema de Gestión de Pacientes")
     
     # Cargar datos desde el CSV único
     pacientes, medicos = cargar_datos_csv()
     
     # Crear un DataFrame con información resumida de pacientes
     data_pacientes = []
     
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