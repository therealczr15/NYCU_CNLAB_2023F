# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
@app.route('/pages')
def index():
    # 此處會用到的 function
    #   1. render_template('index.html', ID = ....)
    ''' start of you code '''
    ID = '109511207'
    return render_template('index.html', ID = ID)
    ''' end of you code '''

if __name__ == '__main__':
    app.run(host = '192.168.0.167', port = 9808, debug = False)