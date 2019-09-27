from flask import Blueprint, redirect, render_template, request
from models.index import db

languages_blueprint = Blueprint('languages', __name__, url_prefix="/languages")

@languages_blueprint.route('/')
def index():
    langs = {}
    characters = list(db.characters.find())
    for c in characters:
        for l in c['languages']:
            if l in langs:
                langs[l].append(c['name'])
            else:
                #make a list w/ character name in it. assign to langs at key l (language name)
                langs[l] = [c['name']]
        print(c['name'])
    return render_template('languages/index.html', langs=langs)