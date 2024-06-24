import time
from flask import Flask, render_template, redirect, flash, url_for, session, request
from wtforms import SubmitField, StringField
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import InputRequired
import ai_functions
import download_subtitles
import secrets


# TODO: 1. Create history of searches. Last 3 searches can be stored in memory. << this maybe with point 5
#       2. translate ? should be easy


app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = 'gmbnvmmvm'
csrf = CSRFProtect(app)


class PasteVideo(FlaskForm):
    video_link = StringField('here link please', validators=[InputRequired()])
    submit = SubmitField('Submit')


all_text =[]

def extracting_yt_link(link):
    if 'https://www.youtube.com/watch?v=' in link:
        end_for_embed = link.split('=')[1]
    elif 'https://youtu.be/' in link:
        end_for_embed = link.split('.be/')[1].split('?')[0]
    else:
        end_for_embed = "dQw4w9WgXcQ"
    return end_for_embed

@app.route('/', methods=['GET', 'POST'])
def index():
    global all_text
    session['len_all_text'] = 1
    form = PasteVideo()
    if request.method == 'POST' and form.validate_on_submit():
        session['data'] = form.video_link.data
        session['end_for_embed'] = extracting_yt_link(session['data'])
        download_subtitles.download_sub(session["data"])
        all_text, session['len_all_text'] = download_subtitles.give_me_subs()
        return redirect(url_for('result'))
    return render_template('index.html', form=form)


@app.route("/track", methods=["GET"])
def track():
    print(session['len_all_text'], "this is one returning from function track")
    return str(session['len_all_text'])


@app.route('/result', methods=['GET', 'POST'])
def result():
    global all_text
    if "data" in session.keys():
        try:
            print(session['len_all_text'], "this is one returning from function result at the beginning of try")
            time_start = time.time()
            end_for_embed = session['end_for_embed']
            summary, summary2 = ai_functions.splitting_tasks(all_text)
            session['summary'] = summary
            session['summary2'] = summary2
            time_stop = time.time()
            time_diff = time_stop - time_start
            print(time_diff)
        except FileNotFoundError:
            return render_template('fail.html')
        return render_template('result.html', summary=summary, summary2=summary2, end_for_embed=end_for_embed)
    if "summary" in session.keys():
        end_for_embed = session['end_for_embed']
        return render_template('result.html', summary=session['summary'], summary2=session['summary2'],
                               end_for_embed=end_for_embed)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
