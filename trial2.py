from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Predefined questions and choices for each option
questions_mapping = {
    'option1': [
        {'question': 'Do your teachers complain that you are hyperactive?', 'choices': ['no', 'a little', 'a lot']},
        {'question': 'Do your parents complain that you are hyperactive?', 'choices': ['no', 'a little', 'a lot']},
        {'question': 'Do you think that you are hyperactive?', 'choices': ['no', 'a little', 'a lot']},
    ],
    'option2': [
        {'question': 'Do you experience Insomnia?', 'choices': ['no', 'yes']},
        {'question': 'Have you experienced a change in apetite?', 'choices': ['no', 'yes']},
        {'question': 'Have you experienced feelings of worthlessness?', 'choices': ['no', 'yes']}
    ],
    'option3': [
        {'question': 'Do you experience intense irritability?', 'choices': ['no', 'a little', 'a lot']},
        {'question': 'What is the frequency of your angry/irritable mood?', 'choices': ['never', 'occasionally', 'once or twice a week', 'three or more times a week', 'every day']},
        {'question': 'Are you easily irritated?', 'choices': ['no', 'a little', 'a lot']}
    ],
    'option4': [
        {'question': 'When worried, is it difficult to control?', 'choices': ['no', 'yes']},
        {'question': 'How does your worry of school work compare to others', 'choices': ['no more than others', 'a little more than others', 'a lot more than others']},
        {'question': 'How does your worry of your appearance compare to others?', 'choices': ['no more than others', 'a little more than others', 'a lot more than others']}
    ],
    'option5': [
        {'question': 'What was your longest episode in the last 4 weeks', 'choices': ['less than an hour', 'less than 24 hours', '1-3 days','4-6 days', 'one week or more']},
        {'question': 'How many times have you experienced a depressive episode', 'choices': ['never', 'once', '2-4 times', '5 or more times']},
        {'question': 'Do you feel like a burden to those around you?', 'choices': ['not at all', 'a little', 'a medium amount','a great deal']},

    ]
}

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children='Trial Questionnaire',
                    style={'textAlign': 'center', 'backgroundColor': '#f2f2f2', 'padding': '20px'}
                ),
                html.Div(
                    children=[
                        html.P(
                            "Questionnaire Description",
                            style={'fontSize': 14,'backgroundColor': '#f2f2f1', 'marginBottom': '30px'}
                        )
                    ],
                    style={'textAlign': 'center'}
                    ),
                dcc.Dropdown(
                    id='dropdown-options',
                    options=[
                        {'label': 'ADHD', 'value': 'option1'},
                        {'label': 'Depression', 'value': 'option2'},
                        {'label': 'DMDD', 'value': 'option3'},
                        {'label': 'Generalized Anxiety', 'value': 'option4'},
                        {'label': 'Mania', 'value': 'option5'}
                    ],
                    value='option1',  # Default selected option
                    style={'width': '200px', 'margin': '20px', 'marginLeft': '10%'}
                ),
                html.P(
                    "Select the answers that best reflect you. Once  completed, click 'Generate Prompt' to recieve your prompt for the current section.",
                    style={'fontSize': 14, 'margin': '20px', 'marginLeft': '12%'}
                )
            ],
            style={'width': '100%', 'boxSizing': 'border-box'}
        ),
        html.Div(
            id='question-container',
            style={'padding': '2rem', 'textAlign': 'left', 'width': '80%', 'margin': 'auto'}
        ),
        html.Button('Generate Prompt', id='generate-prompt-button', n_clicks=0, style={'margin': '20px'}),
        html.Div(id='prompt-output', style={'margin': '20px'})
    ],
    style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'height': '100vh'}
)

@app.callback(
    Output('question-container', 'children'),
    [Input('dropdown-options', 'value')]
)
def update_questions(selected_option):
    # Get the corresponding questions for the selected option
    questions = questions_mapping.get(selected_option, [])

    # Create radio button components for each question
    radio_buttons = []
    for question_info in questions:
        question_text = question_info['question']
        choices = question_info['choices']

        radio_buttons.append(html.Div([
            html.Label(question_text),
            dcc.RadioItems(
                id=f"{selected_option}_{question_text}",
                options=[{'label': choice, 'value': choice} for choice in choices],
                value=None  # Initialize as None
            )
        ], style={'margin-bottom': '10px'}))  # Add margin-bottom for spacing

    return radio_buttons

@app.callback(
    Output('prompt-output', 'children'),
    [Input('generate-prompt-button', 'n_clicks')],
    [Input('dropdown-options', 'value')],
    [Input('question-container', 'children')]
)
def generate_prompt(n_clicks, selected_option, question_components):
    # Check if the button is clicked
    if n_clicks > 0:
        # Get the selected answers for each question
        selected_answers = {}
        for question_component in question_components:
            question_text = question_component['props']['children'][0]['props']['children']
            selected_answer = question_component['props']['children'][1]['props']['value']
            selected_answers[question_text] = selected_answer

        # Generate prompt based on selected answers
        prompt_lines = [
            f"When asked '{question}', they responded with '{answer}'. "
            for question, answer in selected_answers.items()
        ]
        prompt = '\n'.join(prompt_lines)

        return html.Div([
            html.H3('Generated Prompt:'),
            html.P(prompt)
        ])
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)
