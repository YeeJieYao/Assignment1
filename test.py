from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'
data_path = 'https://raw.githubusercontent.com/YeeJieYao/Assignment1/main/population.csv'
data_path2 = 'https://raw.githubusercontent.com/YeeJieYao/Assignment1/main/Number_of_Prisoners_by_Gender_by_State_2016-2019.csv'
data_path3 = 'https://raw.githubusercontent.com/YeeJieYao/Assignment1/main/mcd_locations_in_malaysia.csv'

df = pd.read_csv(data_path)
df2= df.iloc[1:]

fig = px.pie(df2, values='pop',names='state', title='Malaysia Population') .update_layout(xaxis_title="State", yaxis_title="Index")

df = pd.read_csv(data_path2)
df2 = df.set_index('State')
df2 = df2.transpose()

fig2 = px.line(df2,title='Prisoners in Malaysia') .update_layout(xaxis_title="State", yaxis_title="Index")

df = pd.read_csv(data_path3)
fig3 = px.bar(df, x='State', y=['Number of Locations'], title='McDonalds Location in Malaysia') .update_layout(xaxis_title="State", yaxis_title="Index")

app.layout = html.Div(
    [html.Img(src=image_path),	                
    html.H1("Data Visualization"),
    html.H2("Dashboard showing graphs"),
    dcc.Graph(figure = fig),
    dcc.Graph(figure = fig2),
    dcc.Graph(figure = fig3)]
)

if __name__ == '__main__':
    app.run_server(debug=True)
