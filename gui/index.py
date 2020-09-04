# Third Party Imports
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output 

# Local Imports
from gui.app import app
from gui.views import body
from gui import callbacks

# Layout

app.layout = html.Div([
    body.tabs
], id='main-page')

