""" All ui elements """

from dash import html, dcc
import dash_bootstrap_components as dbc

def main():
    # app layout
    return html.Div([
        dbc.Row(         # Top image banner
            [
                dbc.Col(image_banner())
            ],
            # className="h-35",
        ),
        dbc.Row(         # Top banner with input for song name to propose
            [
                dbc.Col(menu())
            ],
            # className="h-35",
        ),
        dbc.Row(html.Div(children=[], id='song-chld')),

        dcc.Interval(id='songs-interval', interval=2000)
    ])

def image_banner():
    # return html.Img(src=r"assets\Autensemble.png", style={'max-width':'100%'})
    return dbc.Card(
        [
            dbc.CardImg(
                src="https://github.com/jordyBonnet/everybodyDJ/blob/main/assets/Autensemble.png?raw=true",
                top=True,
                style={"opacity": 1},
            ),
        ]
    )

def menu():
    return dbc.Card(
        dbc.CardBody(
            dbc.Row([
                dbc.Col(
                    dbc.Input(id="input-song", placeholder="Nom de la musique", type="text", size="lg"),
                    style=style_menu(), xs=10, sm=10, md=4, lg=4, xl=4,
                ),
                dbc.Col(
                    dbc.Button("AJOUTER🎵", id='Add-song_btn', outline=False, color="success", className="me-1", size="lg"),
                    style=style_menu(), xs=10, sm=10, md=4, lg=4, xl=4,
                ),
                dbc.Col(
                    dbc.Button("Autensemble❤️", id='AutEn-calcul', outline=False, color="warning", className="me-1", size="lg"),
                    style=style_menu(), xs=10, sm=10, md=4, lg=4, xl=4,
                ),
            ],justify="center",)
        ),
    )

def style_menu():
    return {'fontSize': 14}

def song_lst_chld(song_list):
    # print(song_list)
    left_col, right_col = [], []
    for i, song in enumerate(song_list):
        mod = i % 2
        # print(i, mod, song[0], song[1])
        if mod == 0:
            left_col.append(song_card(song[0], song[1]))
        elif mod == 1:
            right_col.append(song_card(song[0], song[1]))
    
    out = [dbc.Row(
        [
            dbc.Col(left_col),
            dbc.Col(right_col),
        ]
    )]
    return out


def song_card(name, score):
    return dbc.Card(
        dbc.CardBody(
            dbc.Row(
                [
                    dbc.Col(html.P(name), style={'fontSize': 16},
                        xs=7, sm=7, md=7, lg=7, xl=7), # xs=12, sm=12, md=12, lg=8, xl=8),
                    dbc.Col(html.P(f'{score}', style={'fontSize': 12},),
                        xs=2, sm=2, md=2, lg=2, xl=2), # xs=6, sm=6, md=6, lg=2, xl=2),
                    dbc.Col(dbc.Button("👍", id=f'{name}-Up', outline=True, color="primary", className="me-1", size="sm"),
                        xs=1, sm=1, md=1, lg=1, xl=1), # xs=3, sm=6, md=6, lg=1, xl=1),
                    dbc.Col(dbc.Button("👎", id=f'{name}-Down', outline=True, color="primary", className="me-1", size="sm"),
                        xs=1, sm=1, md=1, lg=1, xl=1), # xs=3, sm=6, md=6, lg=1, xl=1),
                ]
            )
        ), 
        style = {'height': 60}
    )

        




