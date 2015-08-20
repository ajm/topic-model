from flask import Flask, request, send_from_directory, render_template, jsonify
import json
import os
from os import path
from src.backend import topic

app = Flask(__name__)
app.debug = True

root_path = '/Users/kalleilv/desktop/topic-model/topic_data'

@app.route('/static/<path:path>')
def send_static_file(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topics_for_years')
def topics_for_years():
    year_from = request.args.get('from')
    year_to = request.args.get('to')

    filename = os.path.join(os.path.dirname(__file__), 'static/data/graph_1993_2002.json')

    data_file = open(filename, 'r')
    data_json = data_file.read()
    data_file.close()

    return data_json

@app.route('/topics_for_year')
def topics_for_year():
    year = request.args.get('year')

    filename = os.path.join(os.path.dirname(__file__), 'static/data/flare.json')

    data_file = open(filename, 'r')
    data_json = data_file.read()
    data_file.close()

    return data_json

@app.route('/topics_for_class')
def topics_for_class():
    class_name = request.args.get('class')

    filename = os.path.join(os.path.dirname(__file__), 'static/data/graph_1993_2002.json')

    data_file = open(filename, 'r')
    data_json = data_file.read()
    data_file.close()

    return data_json

@app.route('/class/<class_mode>')
def classes(class_mode='acm-class'):
    if class_mode == 'acm-class':
        fname = path.join(root_path, 'class_topic', 'acm_class.pkl')
    elif class_mode == 'arxiv-category':
        fname = path.join(root_path, 'class_topic', 'arxiv_category.pkl')

    class_list = topic.get_classes(fname)
    class_arr = []

    for key,value in class_list.iteritems():
        class_arr.append(value)

    return json.dumps({ 'classes': class_arr })

if __name__ == '__main__':
    app.run()