#import statements
from flask import Flask, render_template
from blueprints.characters import character_blueprint
from blueprints.languages import languages_blueprint
#declare flask app instance
app = Flask(__name__)
#Home Page Route
@app.route('/')
def home():
    return render_template('home.html')

#blueprints
app.register_blueprint(character_blueprint)
app.register_blueprint(languages_blueprint)

#Listen on port 5000
if __name__ == '__main__':
    app.run()