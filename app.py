from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)

app.config['SECRET_KEY'] = "CATS"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_handler():
    return render_template("views/index.html", prompt=story.prompts)


@app.route('/story', methods=["POST"])
def generated_story():
    gen_words = {}
    for val in request.form:
        gen_words[val] = request.form[val]

    return render_template("views/results.html",
                           generated_story=story.generate(gen_words))
