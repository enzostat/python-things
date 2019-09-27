from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from models.index import db
from bson.objectid import ObjectId

character_blueprint = Blueprint('characters',__name__, url_prefix='/characters')

@character_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        characters = list(db.characters.find())
        print(characters, len(characters))
        return render_template('characters/index.html', characters=characters)
    elif request.method == 'POST':
        name = request.form['name']
        print('You typed the name:', name)
        # langs = request.form['languages'].split(',')
        langs = [x.strip() for x in request.form['languages'].split(',')]
        if request.form['birthday']:
            date = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
        else:
            date = None
        db.characters.insert_one({
            'name': request.form['name'],
            'image': request.form['image'],
            'languages': langs,
            'birthday': date,
            'bio': request.form['bio']
        })
        # print(formatted_date)
        return redirect('/characters')

@character_blueprint.route('/<char_id>')
def show(char_id):
    character = db.characters.find_one({'_id': ObjectId(char_id)})
    return render_template('characters/show.html', character=character)