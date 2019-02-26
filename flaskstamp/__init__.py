import os

from flask import Flask, jsonify


def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    
    from . import timestamp
    parse = timestamp.parse

    @app.route('/')
    def hello():
        return "Hello World!"

    @app.route('/api/timestamp/', defaults={'time': None})
    def timestampNow(time):
        data = parse(time)
        return jsonify({'timestamps': data})

    @app.route('/api/timestamp/<time>')
    def timestamp(time):
        data = parse(time)
        return jsonify({'timestamps': data})

    return app