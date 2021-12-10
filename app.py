from flask import Flask,render_template

from libs.widget_tiempo import widget_tiempo


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('general/general.html')
@app.route('/tiempo/')
def tiempo():
    wtiempo=widget_tiempo('tiempo')
    dev=wtiempo.view()
    return dev
@app.route('/strava/')
def strava():
    return '<h1>strava datos</h1>'