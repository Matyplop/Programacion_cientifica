import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import plotly.express as px

from AnalizadorPacientes import AnalizadorPacientes
from Cargar_datos_csv import cargar_datos_csv
from FrecuenciaConsultas import FrecuenciaConsultas
from MargenGasto import MargenGasto

# Cargar los datos
pacientes, medicos = cargar_datos_csv()

# Preparar DataFrame de pacientes
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

# Top enfermedades
top_enf = AnalizadorPacientes.top_enfermedades(pacientes)
df_top_enf = pd.DataFrame(top_enf, columns=["Enfermedad", "Casos"])

# Indicadores personalizados
indicadores = [MargenGasto(), FrecuenciaConsultas()]
data_indicadores = []
for p in pacientes:
    row = {"Paciente": p.nombre}
    for ind in indicadores:
        row[ind.__class__.__name__] = ind.calcular(p)
    data_indicadores.append(row)
df_indicadores = pd.DataFrame(data_indicadores)

# Gasto total del sistema
gasto_total = AnalizadorPacientes.gasto_total_del_sistema(pacientes)

# App Dash con tema oscuro
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.title = "Sistema de Gestión de Pacientes"

app.layout = dbc.Container([
    html.H1("Sistema de Gestión de Pacientes", className="text-center my-4"),

    dbc.Card([
        dbc.CardHeader("Datos de Pacientes"),
        dbc.CardBody(dbc.Table.from_dataframe(df_pacientes, striped=True, bordered=True, hover=True, responsive=True))
    ], className="mb-4"),

    dbc.Card([
        dbc.CardHeader("Pacientes con gasto alto (>20.000)"),
        dbc.CardBody(dbc.Table.from_dataframe(df_pacientes[df_pacientes["Total Gastado"] > 20000], striped=True, bordered=True, hover=True))
    ], className="mb-4"),

    dbc.Card([
        dbc.CardHeader("Top enfermedades más comunes"),
        dbc.CardBody([
            dcc.Graph(figure=px.bar(df_top_enf, x="Enfermedad", y="Casos", text="Casos", title="Top Enfermedades"))
        ])
    ], className="mb-4"),

    dbc.Card([
        dbc.CardHeader("Indicadores personalizados"),
        dbc.CardBody(dbc.Table.from_dataframe(df_indicadores, striped=True, bordered=True, hover=True))
    ], className="mb-4"),

    dbc.Card([
        dbc.CardHeader("Gasto total del sistema"),
        dbc.CardBody(html.H4(f"${gasto_total:,.2f}", className="text-success"))
    ], className="mb-4"),

    dbc.Card([
        dbc.CardHeader("Costo total por paciente"),
        dbc.CardBody(dcc.Graph(
            figure=px.bar(df_pacientes, x="Nombre", y="Total Gastado", title="Costo total por paciente", text="Total Gastado")
        ))
    ])
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
