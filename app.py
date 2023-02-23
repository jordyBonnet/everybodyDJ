import dash
from dash import Input, Output, State, ctx
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import ui
import sqlite3

app = dash.Dash(
    external_stylesheets=[dbc.themes.DARKLY]
)
server = app.server

app.layout = ui.main()

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
def display_value(n, song_name):
    # button_id = ctx.triggered_id
    # print(ctx.triggered)
    if ctx.triggered[0]['value'] == None:
        print('\nnew connexion')
        raise PreventUpdate
    
    con = sqlite3.connect("songs.db")
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
    
    con = sqlite3.connect("/home/jordyB/everybodyDJ/songs.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM songs ORDER BY score DESC")
    song_list = res.fetchall()
    con.close()
    out = ui.song_lst_chld(song_list)
    return out




if __name__ == "__main__":
    app.run_server(debug=False)