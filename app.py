import dash
from dash import Input, Output, State, ctx, ALL
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import ui
import sqlite3
from datetime import datetime, timedelta
import math

app = dash.Dash(
    external_stylesheets=[dbc.themes.DARKLY],
    # suppress_callback_exceptions=True
)
server = app.server

app.layout = ui.main()

DEPLOYED = True
DEPLOYED_HOME_PATH = '/home/jordyB/everybodyDJ/'
ASSETS_PATH = 'assets/'
DEPLOYED_ASSETS_PATH = DEPLOYED_HOME_PATH + 'assets/'
SONGSDB_NAME = 'songs.db'
SONGSDB_PATH = SONGSDB_NAME
if DEPLOYED:
    SONGSDB_PATH = DEPLOYED_HOME_PATH + SONGSDB_NAME

#################
### CALLBACKS ###
#################

## button to add a new song to the list
@app.callback(
    [
        Output('Add-song_btn', 'color'),
    ],
    [
        Input('Add-song_btn', 'n_clicks'),
    ],
    [
        State('input-song', 'value')
    ]
)
def display_value(_, song_name):
    # button_id = ctx.triggered_id
    # print(ctx.triggered)
    if ctx.triggered[0]['value'] == None:
        print('\nnew connexion')
        raise PreventUpdate
    
    if song_name == '':
        raise PreventUpdate
    
    con = sqlite3.connect(SONGSDB_PATH)
    cur = con.cursor()
    data =[(str(song_name), 1)]
    cur.executemany("INSERT INTO songs VALUES(?, ?)", data)
    con.commit()
    con.close()
    raise PreventUpdate

## interval
@app.callback(
    [
        Output('song-chld', 'children'),
    ],
    [
        Input('songs-interval', 'n_intervals'),
    ],
)
def display_value(n):
    # button_id = ctx.triggered_id
    
    if ctx.triggered[0]['value'] == None:
        raise PreventUpdate
    
    con = sqlite3.connect(SONGSDB_PATH)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM songs ORDER BY score DESC")
    song_list = res.fetchall()
    con.close()
    out = ui.song_lst_chld(song_list)
    return out

## Up vote
@app.callback(
    Output('forfake', 'children'),      # NOT USED
    Input({'type': 'btn-Up', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def display_value(values):
    if any(values):
        for inp in ctx.inputs_list[0]:
            if 'value' in inp.keys():
                song = inp['id']['index']
                con = sqlite3.connect(SONGSDB_PATH)
                cur = con.cursor()
                cur.execute(f'UPDATE songs SET score = score + 1 WHERE title = "{song}"')
                con.commit()
                con.close()
        # print(ctx.inputs_list)
        # print(values, ctx.triggered)
    raise PreventUpdate

## Down vote
@app.callback(
    Output('forfake', 'color'),       # NOT USED
    Input({'type': 'btn-Down', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def display_value(values):
    if any(values):
        for inp in ctx.inputs_list[0]:
            if 'value' in inp.keys():
                song = inp['id']['index']
                con = sqlite3.connect(SONGSDB_PATH)
                cur = con.cursor()
                cur.execute(f'UPDATE songs SET score = score - 1 WHERE title = "{song}"')
                con.commit()
                con.close()
        # print(ctx.inputs_list)
        # print(values, ctx.triggered)
    raise PreventUpdate

## Autensemble calcul modal opening
@app.callback(
    [
        Output('Auten-modal', 'is_open'),
    ],
    [
        Input('AutEn-calcul', 'n_clicks'),
    ],
)
def display_value(n):
    # button_id = ctx.triggered_id
    
    if ctx.triggered[0]['value'] == None:
        raise PreventUpdate
    
    return True,

## Autensemble calcul btn clicked
@app.callback(
    [
        Output('Aut-fade', 'is_in'),
        Output('row-Aut-calc', 'children')
    ],
    [
        Input('Aut-calc-btn', 'n_clicks'),
    ],
    [
        State('input-nameC1', 'value'),
        State('C1-date', 'value'),
        State('input-nameC2', 'value'),
        State('C2-date', 'value'),
        State('kiss-date', 'value'),
    ]
)
def display_value(n, name1, date1, name2, date2, kiss_date):
    # button_id = ctx.triggered_id
    if not ctx.triggered:
        raise PreventUpdate
    
    # dates given in str with format YYYY-MM-DD
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')
    date_kiss_obj = datetime.strptime(kiss_date, '%Y-%m-%d')
    
    age_at_kiss1_sec = (date_kiss_obj - date1_obj).total_seconds()
    age_at_kiss2_sec = (date_kiss_obj - date2_obj).total_seconds()
    age_at_kiss1_year = round(age_at_kiss1_sec / 60 / 60 / 24 / 365.25)
    age_at_kiss2_year = round(age_at_kiss2_sec / 60 / 60 / 24 / 365.25)

    Aut1 = date_kiss_obj + timedelta(seconds=round(age_at_kiss1_year) * 60*60*24*365.265)
    Aut2 = date_kiss_obj + timedelta(seconds=round(age_at_kiss2_year) * 60*60*24*365.265)
    Aut1_str = Aut1.strftime('%d/%m/%Y')
    Aut2_str = Aut2.strftime('%d/%m/%Y')
    
    poire_en_2_diff_sec = (max(Aut1, Aut2) - min(Aut1, Aut2)).total_seconds()/2
    Aut_commun_obj = (min(Aut1, Aut2) + timedelta(seconds=poire_en_2_diff_sec)).date()
    Aut_commun = Aut_commun_obj.strftime('%d/%m/%Y')

    now = datetime.now().date()
    when = timedelta_to_years_days(now - Aut_commun_obj)

    out_child = ui.Aut_calculated(name1, Aut1_str, name2, Aut2_str, Aut_commun, when)
    return True, out_child

def timedelta_to_years_days(delta):
    if delta.days < 0:
        fut_pass = 'futur'
    else:
        fut_pass = 'past'
    years = math.floor(abs(delta.days / 365.25))
    if years == 0:
        year_or_days = 'jours'
        val = abs(delta.days)
    else:
        year_or_days = 'ans'
        val = years
    return fut_pass, val, year_or_days 

if __name__ == "__main__":
    app.run_server(debug= not DEPLOYED)