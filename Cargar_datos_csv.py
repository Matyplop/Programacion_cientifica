from Medico import Medico
from Paciente import Paciente
from Consulta import Consulta
import pandas as pd


def cargar_datos_csv():
    """
    Lee el archivo 'pacientes_medicos.csv' y procesa los datos para generar listas de
    objetos 'Medico', 'Paciente' y las correspondientes 'Consulta'.
    """
    
   
    df = pd.read_csv('pacientes_medicos.csv')
    df.columns = [col.strip().lower() for col in df.columns]
    
    medicos = []
    pacientes = []

    
    for _, row in df.iterrows():
        
        if not any(medico.nombre == row['medico'] for medico in medicos):
            medico = Medico(row['medico'], row['especialidad'])
            medicos.append(medico)
        
       
        paciente = next((p for p in pacientes if p.rut == row['rut']), None)
        if not paciente:
            paciente = Paciente(row['nombre'], row['rut'])
            pacientes.append(paciente)
        
       
        medico_obj = next(m for m in medicos if m.nombre == row['medico'])
        consulta = Consulta(medico_obj, row['costo'], row['diagnostico'])
        paciente.agregar_consulta(consulta)

        

    return pacientes, medicos
