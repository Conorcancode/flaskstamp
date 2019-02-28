import os

from flask import Flask, jsonify, redirect


def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    
    from . import timestamp
    parse = timestamp.parse

    @app.after_request
    def addCors(response):
        response.headers['Access-Control-Allow-Origin'] = 'https://conorcancode.com'
        return response

    @app.route('/')
    def hello():
        return redirect("./api/timestamp/", code=302)

    @app.route('/api/timestamp/', defaults={'time': None})
    def timestampNow(time):
        data = parse(time)
        return jsonify({'timestamps': data})

    @app.route('/api/timestamp/<time>')
    def timestamp(time):
        data = parse(time)
        return jsonify({'timestamps': data})


    return app