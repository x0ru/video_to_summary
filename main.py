from flask import Flask, render_template, redirect,url_for, session, request
import secrets
from wtforms import URLField
from flask_wtf import FlaskForm, CSRFProtect
import video
from flask_executor import Executor
import time
import ai_functions
import os
import threading

app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = 'gmbnvmmvm'
csrf = CSRFProtect(app)
executor = Executor(app)


class PasteVideo(FlaskForm):
    video_link = URLField("Please paste your video link")


def check_if_file_downloaded(title):
    print(title, "calling function")
    if os.path.isfile(f"{title}.mp4"):
        transcription, summary = ai_functions.start_ai_transcription(title)
        return transcription, summary
    return "Problem with chatgpt", "Problem"


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasteVideo()
    if form.validate_on_submit():
        title = threading.Thread(target=video.video, args=(form.video_link.data,))
        time.sleep(20)
        check_if_file_downloaded(title)
        return render_template('ulala.html')
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
