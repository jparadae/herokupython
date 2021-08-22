import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

app = dash.Dash(__name__)
server = app.server

#bases utilizadas para trabajar
df_ocupados = pd.read_excel("estadisticas_rps.xlsx", sheet_name="Ocupados")
df_cobertura = pd.read_excel("estadisticas_rps.xlsx", sheet_name="Cobertura_Promedio")
df_ingresos_laborales = pd.read_excel("estadisticas_rps.xlsx", sheet_name="Ingresos_Laborales")
df_esfuerzo_fiscal = pd.read_excel("estadisticas_rps.xlsx", sheet_name="Esfuerzo_Fiscal")
df_rps = pd.read_excel("estadisticas_rps.xlsx", sheet_name="RPS")

#gráficos
figura_ocupados = px.line(df_ocupados, x="Periodo", y="Ocupados (miles)", title="Número de ocupados (miles). 2010 - 2021" )
figura_ingresos_laborales = px.line(df_ingresos_laborales, x="Periodo", y="Ingreso Laboral", title="Ingreso laboral del hogar promedio (moneda 2020). 2010 - 2021" )
figura_esfuerzo_fiscal = px.bar(df_esfuerzo_fiscal, x="Paises", y="Subtotal (% PIB)", title="Esfuerzo fiscal para enfremtar la pandemia sobre la línea (% del PIB)" )
figura_rps = px.bar(df_rps, x="Periodo", y=["Préstamo Solidario", "prestaciones del SC", "Bono Covid-19", "IFE", "Bono Clase Media", "Bono a los transportistas", "Bono de $200 mil AFP" ], title="Monto total de transferencias directas a nivel país. 1980 - 2021" )
figura_poblacion_cuarentena = px.line(df_rps, x="Periodo", y="% de la población en cuarentena", title="Población en cuarentena (%). 2020 - 2021" )
figura_cobertura = px.bar(df_cobertura, y="Paises", x="Cobertura promedio (% de la población)", title="Cobertura promedio (% de la población*)", orientation="h")


#-----------------------------------------------------------------------------------------------------#
#código para creación de página
colors = {
    'background': '#111111',
    'text': '#000000'
}

app.layout = html.Div(children=[
    html.H1(children='Cinco claves sobre las ayudas entregadas por el Gobierno a los hogares en pandemia',
           style={
            'textAlign': 'center',
            'color': colors['text']
        }

           ),
  
    html.Div(children='''
        El Covid-19 llegó a Chile en marzo 2020 afectando directamente los trabajos debido a las medidas
sanitarias que tuvieron como consecuencias la paralización total o parcial de las actividades
económicas. Según la Encuesta Nacional de Empleo (ENE) entre el trimestre antes de la llegada de
la pandemia a Chile (dic-feb 2020) y el punto más bajo (may-jul 2020) se perdieron 1.990.181
empleos, equivalente al 22% de los empleos pre-pandemia.
    '''),
       
    html.Div(children='''
             La única encuesta que mide ingresos durante la pandemia a nivel de hogar es la Encuesta de Ocupación y Desocupación 
de la U. de Chile (EOD), representativa para el Gran Santiago. Según la EOD, el ingreso laboral promedio de los hogares 
llegó a su punto más bajo en junio 2020, con una caída del 32% respecto al nivel pre-pandemia. De esta forma, la ENE y la EOD muestran que en sólo 4 meses el número de ocupados e ingreso laboral de los hogares 
retrocedió al nivel de hace 10 años, dando cuenta del fuerte impacto de la pandemia sobre el mercado laboral.
 
    '''),

    dcc.Graph(
        id='example-graph-1',
        figure=figura_ocupados,
    ),
      
    dcc.Graph(
        id='example-graph-2',
        figure=figura_ingresos_laborales,
    ),
    
    dcc.Graph(
        id='example-graph-3',
        figure=figura_esfuerzo_fiscal,
    ),

    dcc.Graph(
        id='example-graph-4',
        figure=figura_rps,
    ),
    
    dcc.Graph(
        id='example-graph-5',
        figure=figura_poblacion_cuarentena,
    ),
    
    dcc.Graph(
        id='example-graph-6',
        figure=figura_cobertura,
    ),
    
    html.Button("Descargar estudio completo", id="btn_pdf"), dcc.Download(id="download-pdf"),
        
])

@app.callback(
    Output("download-pdf", "data"),
    Input("btn_pdf", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "210702 Cinco claves de las ayudas a los hogares del Gobierno durante la Pandemia.pdf"
    )

if __name__ == '__main__':
    app.run_server(debug=True)