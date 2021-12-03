import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
data0 = pd.read_csv('data/sample2.csv')
d = data0.copy()
# d = d['seed'].replace(0, "No Seed")
d = d.replace(1, "Seed")
fig = px.bar(d, x="name", y="grade", color="seed", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig2 = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)
app.layout = html.Div(children=[
    html.H1(children='Hello Dancers',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
        ),

    html.Div(children='''
        This is a web application framework for making multiple groups.
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='countries-graph',
        figure=fig2
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    
    # html.H4(children='Tournaments details (2021)'),
    generate_table(d)
])

if __name__ == '__main__':
    app.run_server(debug=True)