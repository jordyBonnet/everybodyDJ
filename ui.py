""" All ui elements """

from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from datetime import datetime, date
from dash_iconify import DashIconify # https://icon-sets.iconify.design/ ⚠️ does not work on pythoneverywhere

FONT_SIZE = 28

def main():
    # app layout
    return html.Div([
        dmc.Affix(
            [
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
            ],
            position={"top": 0, "right": 0, "right": 0, "left":0},
        ),
        dmc.Space(h=300),
        dbc.Row(html.Div(children=[], id='song-chld')),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dmc.Text(
                    "Calculez votre Autensemble ❤️",
                    variant="gradient",
                    gradient={"from": "yellow", "to": "red", "deg": 45},
                    style={"fontSize": FONT_SIZE+10},
                ))),
                dbc.ModalBody(Aut_modal_body()),
            ],
            id="Auten-modal",
            size="xl",
            fullscreen=True,
            is_open=False,
        ),
        dcc.Interval(id='songs-interval', interval=1000)
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
        [            
            dbc.Row(
                [
                    dbc.Col(
                        # dbc.Input(id="input-song", placeholder="Nom de la musique", type="text", size="lg"),
                        # style=style_menu(), xs=10, sm=10, md=4, lg=4, xl=4,
                        dmc.TextInput(
                            '',
                            id="input-song",
                            # label="Nom de la musique",
                            # style={"width": 200},
                            placeholder="Artiste - Nom de la musique",
                            size='xl',
                            radius="md",
                            style=style_menu(),
                            # fullWidth=True,
                            # icon=DashIconify(icon="material-symbols:search-rounded"),
                        ),
                        width={"size": 5, "offset": 0},
                    ),
                    dbc.Col(
                        # dbc.Button("AJOUTER🎵", id='Add-song_btn', outline=False, color="success", className="me-1", size="xl"),
                        # style=style_menu(), xs=10, sm=10, md=4, lg=4, xl=4,
                        dmc.Button(
                            "ENVOYER 🎵",
                            id='Add-song_btn',
                            variant="gradient",
                            gradient={"from": "teal", "to": "lime", "deg": 45},
                            size="xl",
                            radius="md",
                            fullWidth=True,
                        ),
                        # dmc.ActionIcon(
                        #     DashIconify(icon="material-symbols:library-add"), color="indigo", variant="filled",
                        #     id='Add-song_btn',
                        #     size="xl",
                        #     radius='md',
                        #     style={'fontSize': FONT_SIZE+10},
                        # ),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        # dbc.Button("Autensemble❤️", id='AutEn-calcul', outline=False, color="warning", className="me-1", size="xl"),
                        # style=style_menu(), xs=10, sm=10, md=4, lg=4, xl=4,
                        dmc.Button(
                            "AUTENSEMBLE ❤️",
                            id='AutEn-calcul',
                            variant="gradient",
                            gradient={"from": "orange", "to": "grape", "deg": 45},
                            size="xl",
                            radius="md",
                            fullWidth=True,
                        ),
                        width={"size": 4, "offset": 0},
                    ),
                ],justify="center", className="g-1",
            )
        ]
        ),
        id='forfake'
    )

def style_menu():
    return {'fontSize': FONT_SIZE}

def song_lst_chld(song_list):
    # print(song_list)
    # left_col, right_col = [], []
    one_col = []
    for i, song in enumerate(song_list):
        mod = i % 2
        # print(i, mod, song[0], song[1])
        # if mod == 0:
        #     left_col.append(song_card(song[0], song[1]))
        # elif mod == 1:
        #     right_col.append(song_card(song[0], song[1]))
        one_col.append(song_card(song[0], song[1]))

    # on 1 column
    out = [dbc.Row(
        [
            dbc.Col(one_col),
        ]
    )]
    # on 2 columns
    # out = [dbc.Row(
    #     [
    #         dbc.Col(left_col),
    #         dbc.Col(right_col),
    #     ]
    # )]
    return out

def song_card(name, score):
    return dbc.Card(
        dbc.CardBody(
            dbc.Row(
                [
                    dbc.Col(html.P(name), style={'fontSize': FONT_SIZE},
                        width=9, ), # xs=12, sm=12, md=12, lg=8, xl=8),
                    dbc.Col(html.P(f'{score}', style={'fontSize': FONT_SIZE-8},),
                        width=1), # xs=6, sm=6, md=6, lg=2, xl=2),
                    dbc.Col(dbc.Button("👍", id={'type': f'btn-Up', 'index': name}, outline=True, color="primary",
                            className="me-1", size="md"),
                        width=1), # xs=3, sm=6, md=6, lg=1, xl=1),
                    dbc.Col(dbc.Button("👎", id={'type': f'btn-Down', 'index': name}, outline=True, color="primary",
                            className="me-1", size="md"),
                        width=1), # xs=3, sm=6, md=6, lg=1, xl=1),
                ]
            )
        ), 
        style = {'height': 70}
    )

def Aut_modal_body():
    return [
        dbc.Row(
            dmc.Text(
                "L'Autensemble c'est une date. Une date personnelle mais que l'on doit à notre moitié.\n \
                C'est la date à partir de laquelle vous avez passé autant de temps avec votre moitié que sans elle dans votre vie.",
                variant="gradient",
                gradient={"from": "yellow", "to": "pink", "deg": 180},
                style={"fontSize": FONT_SIZE},
            )
        ),
        
        # Conjoint 1
        dmc.Space(h=30),
        dmc.Divider(label="Conjoint 1", labelPosition="center", variant="dashed", 
                    style={"fontSize": FONT_SIZE}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        # dbc.Input(id="input-nameC1",
                        #     placeholder="Prénom conjoint n°1", type="text", size="xl",
                        # ),
                        dmc.TextInput(
                            id="input-nameC1",
                            # label="Nom de la musique",
                            # style={"width": 200},
                            placeholder="Prénom conjoint n°1",
                            # icon=DashIconify(icon="material-symbols:search-rounded"),
                            size='xl',
                            radius="md",
                            style=style_menu(),
                            # fullWidth=True,
                        ),
                    ],
                    xs=6, sm=6, md=6, lg=6, xl=6,
                ),
                dbc.Col(
                    [
                        dmc.Text(
                            "Date de naissance:",
                            align='right',
                            size='xl',
                            style={"fontSize": FONT_SIZE-6},
                        )
                    ],
                    xs=2, sm=2, md=2, lg=2, xl=2,
                ),
                dbc.Col(
                    [
                        dmc.DatePicker(
                            id="C1-date",
                            value=date(1990, 1, 1),      # datetime.now().date(),
                            inputFormat="DD / MM / YYYY",
                            clearable=False,
                            size='xl',
                            radius='md',
                        ),
                    ],
                    xs=4, sm=4, md=4, lg=4, xl=4,
                ),
            ]
        ),

        # Conjoint 2
        dmc.Space(h=30),
        dmc.Divider(label="Conjoint 2", labelPosition="center", variant="dashed", 
                    style={"fontSize": 16}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        # dbc.Input(id="input-nameC2",
                        #     placeholder="Prénom conjoint n°2", type="text", size="lg",
                        # ),
                        dmc.TextInput(
                            id="input-nameC2",
                            # label="Nom de la musique",
                            # style={"width": 200},
                            placeholder="Prénom conjoint n°2",
                            # icon=DashIconify(icon="material-symbols:search-rounded"),
                            size='xl',
                            radius="md",
                            style=style_menu(),
                            # fullWidth=True,
                        ),
                    ],
                    xs=6, sm=6, md=6, lg=6, xl=6,
                ),
                dbc.Col(
                    [
                        dmc.Text(
                            "Date de naissance:",
                            align='right',
                            size='xl',
                            style={"fontSize": FONT_SIZE-6},
                        )
                    ],
                    xs=2, sm=2, md=2, lg=2, xl=2,
                ),
                dbc.Col(
                    [
                        dmc.DatePicker(
                            id="C2-date",
                            value=date(1990, 1, 1),      # datetime.now().date(),
                            inputFormat="DD / MM / YYYY",
                            clearable=False,
                            size='xl',
                            radius='md',
                        ),
                    ],
                    xs=4, sm=4, md=4, lg=4, xl=4,
                ),
            ]
        ),

        # First kiss
        dmc.Space(h=30),
        dmc.Divider(label="Premier bisous 👄", labelPosition="center", variant="dashed", 
            style={"fontSize": FONT_SIZE}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dmc.Text(
                            "Date de premier bisous / Mise en couple:",
                            align='right',
                            style={"fontSize": 20},
                        )
                    ],
                    xs=6, sm=6, md=6, lg=6, xl=6,
                ),
                dbc.Col(
                    [
                        dmc.DatePicker(
                            id="kiss-date",
                            value=date(2005, 1, 1),      # datetime.now().date(),
                            inputFormat="DD / MM / YYYY",
                            clearable=False,
                        ),
                    ],
                    xs=4, sm=4, md=4, lg=4, xl=4,
                ),
            ]
        ),
    
        dmc.Space(h=30),
        dmc.Center(
            dmc.Button("Calculer", id='Aut-calc-btn', variant="gradient", size='xl',
                gradient={"from": "grape", "to": "pink", "deg": 35}),
        ),

        dmc.Space(h=30),
        dbc.Fade(
            dbc.Row(id='row-Aut-calc', children=Aut_calculated()),
            id="Aut-fade",
            is_in=False,
            # appear=False,
            style={"transition": "opacity 2000ms ease"},
            timeout=4000, 
        ),
    ]

def Aut_calculated(name1=None, Aut1=None, name2=None, Aut2=None, Aut_commun=None, when=None):
    # when is a tuple with the time to Aut (past or futur)
    txt = ''
    if when:
        if when[0] == 'futur':
            sera_etait = 'sera dans'
            end = 'On le fête 😲 ? Sérieux !'
        else:
            sera_etait = 'était il y a'
            end = "C'est beau le 'vrai' amour 😉 !"
        txt = f'Votre Autensemble {sera_etait} {when[1]} {when[2]}. {end}'
    out = [
        dmc.Text(
                f"L'Autensemble de {name1} est le {Aut1}",
                variant="filled",
                color="pink",
                style={"fontSize": FONT_SIZE},
        ),
        dmc.Text(
                f"L'Autensemble de {name2} est le {Aut2}",
                variant="filled",
                color="pink",
                style={"fontSize": FONT_SIZE},
        ),
        dmc.Text(
                f"Et si on coupe la poire en deux c'est le : {Aut_commun}",
                variant="filled",
                color="red",
                style={"fontSize": FONT_SIZE},
        ),
        dmc.Text(
                txt,
                variant="filled",
                color="orange",
                style={"fontSize": FONT_SIZE},
        ),
    ]
    return out


