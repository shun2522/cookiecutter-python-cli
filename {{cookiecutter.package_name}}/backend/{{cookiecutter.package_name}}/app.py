#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from os import path


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.update(dict(
    SECRET_KEY='development_key',
    TEMPLATES_AUTO_RELOAD=True,
    SEND_FILE_MAX_AGE_DEFAULT=0,
    JSON_AS_ASCII=False
))
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', message='Hello World!', content_id_name='js', js_file='js/index_bundle.js')
