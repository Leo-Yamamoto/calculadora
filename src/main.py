from dash import Dash, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from math import sqrt

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


teclas = ["BS", "%", "√", "=",
          "7", "8", "9", "/",
          "4", "5", "6", "*",
          "1", "2", "3", "-",
          "0", "C", ",", "+",
          ]

botoes = []
for i in range(0, len(teclas), 4):
    linha = dbc.Row([
        dbc.Col(
            html.Button(teclas[i+j], id=f"btn-{teclas[i+j]}", className="btn btn-secondary", style={"width": "60px", "height": "60px"}),
            width="auto"
        )
        for j in range(4)
    ], className="gx-1 mb-2 justify-content-center")
    botoes.append(linha)

app.layout = dbc.Container([
    html.H2("Calculadora", className="text-center my-4"),

    dbc.Card([
        dbc.CardBody([
            html.Div("0", id="visor", className="mb-3 p-3 border rounded bg-light text-end", style={
                "fontSize": "32px",
                "minHeight": "60px",
                "backgroundColor": "#98f5bb",
            }),

            *botoes
        ])
    ], style={"maxWidth": "320px", "margin": "0 auto", "boxShadow": "0 0 10px rgba(0,0,0,0.1)"})
], className="my-5")

@app.callback(
    Output("visor", "children"),
    [Input(f"btn-{tecla}", "n_clicks") for tecla in teclas],
    State("visor", "children")
)
def atualizar_visor(*args):
    botao_clicado = ctx.triggered_id
    visor_atual = args[-1]

    if botao_clicado is None:
        return visor_atual

    tecla = botao_clicado.replace("btn-", "")

    if tecla == "C":
        return "0"
    elif tecla == "BS":
        return visor_atual[:-1] if len(visor_atual) > 1 else "0"
    elif tecla == "=":
        try:
            resultado = str(eval(visor_atual))
            return resultado
        except:
            return "Erro"
    elif tecla == "%":
        try:
            resultado = str(eval(visor_atual) / 100)
            return resultado
        except:
            return "Erro"
    elif tecla == "√":
        try:
            resultado = str(sqrt(eval(visor_atual)))
            return resultado
        except:
            return "Erro"
    else:
        operadores = {"+", "-", "*", "/", "%"}
        if visor_atual == "0" and tecla not in operadores and tecla != "," and tecla != "√":
            return tecla
        elif tecla in operadores and visor_atual[-1] in operadores:
            return visor_atual[:-1] + tecla
        else:
            return visor_atual + tecla


if __name__ == "__main__":
    app.run(debug=True)
