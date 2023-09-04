from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'
data_path = 'https://raw.githubusercontent.com/YeeJieYao/Assignment1/main/population.csv'

df = pd.read_csv(data_path)
df2= df.iloc[1:]

fig = px.pie(df2, values='pop',names='state', title='Malaysia Population') .update_layout(xaxis_title="State", yaxis_title="Index")

df = px.data.iris()
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

app.layout = html.Div(
    [html.Img(src=image_path),	                
    html.H1("Data Visualization"),
    html.H2("Dashboard showing graphs"),
    dcc.Graph(figure = fig),
    dcc.Graph(figure = fig2)]
)

if __name__ == '__main__':
    app.run_server(debug=True)
