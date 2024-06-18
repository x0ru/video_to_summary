from flask import Flask, render_template, redirect, flash, url_for, session
from wtforms import URLField
from flask_wtf import FlaskForm, CSRFProtect
import ai_functions
import download_subtitles
import secrets
from flask_executor import Executor

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



if __name__ == "__main__":
    app.run(debug=True)
