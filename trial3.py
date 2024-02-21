from dash import html, dcc, Dash
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv('final_project_dataset.csv')

app = Dash(__name__)
app.suppress_callback_exceptions = True

app.layout = html.Div([
    html.H1("Trial Prompt Generator", style={'text-align': 'center', 'background-color': 'lightgrey', 'padding': '20px'}),

    dcc.Checklist(
        id='category-checklist',
        options=[
            {'label': 'Sex', 'value': 'SEX'},
            {'label': 'Age', 'value': 'AGE'},
            {'label': 'Attention Deficit Hyperactivity Disorder [ADHD]', 'value': 'adhd'},
            {'label': 'Depression', 'value': 'dep'},
            {'label': 'Disruptive Mood Dysregulation Disorder [DMDD]', 'value': 'dmdd'},
            {'label': 'Generalized Anxiety', 'value': 'gad'},
            {'label': 'Mania', 'value': 'mania'}
        ],
        value=[],
        style={'display': 'flex', 'flexDirection': 'row', 'padding': '10px'}
    ),

    dcc.Dropdown(
        id='sdan-dropdown',
        options=[],  
        value=df['SDAN'].unique()[0],  
        style={'width': '50%', 'margin-left': '20px', 'margin-right': '20px', 'float': 'right'}
    ),

    html.Button('Reset Radio Buttons', id='reset-button', n_clicks=0, style={'margin-left': '20px'}),

    html.Div(id='selected-variables-output', style={'margin-left': '20px'})
])

@app.callback(
    [Output('selected-variables-output', 'children'),
     Output('sdan-dropdown', 'options')],
    [Input('category-checklist', 'value'),
     Input('sdan-dropdown', 'value'),
     Input('reset-button', 'n_clicks')]
)
def update_selected_variables(selected_categories, selected_sdan, reset_button_clicks):
    if not selected_sdan:
        return [], []

    selected_variables = [
        col for col in df.columns if any(category in col for category in selected_categories)
    ]

    output_rows = []

    for category in selected_categories:
        variables_in_category = [variable for variable in selected_variables if category in variable]
        if variables_in_category:
            output_rows.append(html.Div([
                html.H3(category, style={'margin-bottom': '10px'}),
                *[html.Div([
                    html.Label(variable, style={'margin-left': '10px', 'font-size': '14px', 'white-space': 'nowrap'}),
                    dcc.RadioItems(
                        id=f'radio-buttons-{variable}',
                        options=[
                            {'label': 'Not Used', 'value': f'not_used_{variable}'},
                            {'label': 'Given as Info', 'value': f'given_as_info_{variable}'},
                            {'label': 'Query', 'value': f'query_{variable}'},
                        ],
                        value=None if reset_button_clicks > 0 else None,
                        labelStyle={'display': 'block'},
                        inline=False
                    ),
                ]) for variable in variables_in_category]
            ]))

    valid_sdans = df.dropna(subset=selected_variables)['SDAN'].unique()
    sdan_options = [{'label': sdan, 'value': sdan} for sdan in valid_sdans]

    return output_rows, sdan_options


if __name__ == '__main__':
    app.run_server(debug=True)
