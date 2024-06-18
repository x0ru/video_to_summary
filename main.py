from flask import Flask, render_template, redirect,url_for, session, request
import secrets
from wtforms import URLField
from flask_wtf import FlaskForm, CSRFProtect
from flask_executor import Executor
import ai_functions
import download_subtitles

app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = 'gmbnvmmvm'
csrf = CSRFProtect(app)
executor = Executor(app)


class PasteVideo(FlaskForm):
    video_link = URLField("Please paste your video link")



@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasteVideo()
    if form.validate_on_submit():
        download_subtitles.download_sub(form.video_link.data)
        summary = ai_functions.summary()
        return render_template('ulala.html', summary=summary)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
