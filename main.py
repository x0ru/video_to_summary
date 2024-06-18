from flask import Flask, render_template
import secrets
from wtforms import URLField
from flask_wtf import FlaskForm, CSRFProtect
import ai_functions
import download_subtitles


app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = 'gmbnvmmvm'
csrf = CSRFProtect(app)


class PasteVideo(FlaskForm):
    video_link = URLField("Please paste your video link")



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
