import time
from flask import Flask, render_template, redirect, flash, url_for, session, request
from wtforms import URLField, SubmitField
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import InputRequired
import ai_functions
import download_subtitles
import secrets
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = 'gmbnvmmvm'
csrf = CSRFProtect(app)
socket = SocketIO(app)


class PasteVideo(FlaskForm):
    video_link = URLField('here link please', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasteVideo()
    if request.method == 'POST' and form.validate_on_submit():
        session['data'] = form.video_link.data
        return redirect(url_for('result'))
    return render_template('index.html', form=form)



@app.route('/result')
def result():
    try:
        download_subtitles.download_sub(session["data"])
        session.pop('data', None)
        summary = ai_functions.summary().split('\n')
        summary2 = ai_functions.summary_2()
    except FileNotFoundError:
        return render_template('fail.html')
    return render_template('ulala.html', summary=summary, summary2=summary2)

i= 0

somelist = ['apple','nana', 'czort']
@socket.on('message')
def handlemsg(msg):
    global i
    if i < len(somelist):
        send(somelist[i])
        i += 1


if __name__ == "__main__":
    socket.run(app, allow_unsafe_werkzeug=True, port=5555, debug=True)
