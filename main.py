import time
from flask import Flask, render_template, redirect, flash, url_for, session, request
from wtforms import SubmitField, StringField, SelectField
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import InputRequired
import ai_functions
import download_subtitles
import secrets
from icecream import ic

app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = secrets.token_urlsafe()
csrf = CSRFProtect(app)


class PasteVideo(FlaskForm):
    video_link = StringField('here link please', validators=[InputRequired()])
    submit = SubmitField('Submit')


class Languages(FlaskForm):
    languages = SelectField(choices=["Choose language ▼",
                                     "Afrikaans",
                                       "Arabic",
                                       "Bengali",
                                       "Bulgarian",
                                       "Catalan",
                                       "Cantonese",
                                       "Croatian",
                                       "Czech",
                                       "Danish",
                                       "Dutch",
                                       "Lithuanian",
                                       "Malay",
                                       "Malayalam",
                                       "Panjabi",
                                       "Tamil",
                                       "English",
                                       "Finnish",
                                       "French",
                                       "German",
                                       "Greek",
                                       "Hebrew",
                                       "Hindi",
                                       "Hungarian",
                                       "Indonesian",
                                       "Italian",
                                       "Japanese",
                                       "Javanese",
                                       "Korean",
                                       "Norwegian",
                                       "Polish",
                                       "Portuguese",
                                       "Romanian",
                                       "Russian",
                                       "Serbian",
                                       "Slovak",
                                       "Slovene",
                                       "Spanish",
                                       "Swedish",
                                       "Telugu",
                                       "Thai",
                                       "Turkish",
                                       "Ukrainian",
                                       "Vietnamese",
                                       "Welsh",
                                       "Sign language",
                                       "Algerian",
                                       "Aramaic",
                                       "Armenian",
                                       "Berber",
                                       "Burmese",
                                       "Bosnian",
                                       "Brazilian",
                                       "Bulgarian",
                                       "Cypriot",
                                       "Corsica",
                                       "Creole",
                                       "Scottish",
                                       "Egyptian",
                                       "Esperanto",
                                       "Estonian",
                                       "Finn",
                                       "Flemish",
                                       "Georgian",
                                       "Hawaiian",
                                       "Indonesian",
                                       "Inuit",
                                       "Irish",
                                       "Icelandic",
                                       "Latin",
                                       "Mandarin",
                                       "Nepalese",
                                       "Sanskrit",
                                       "Tagalog",
                                       "Tahitian",
                                       "Tibetan",
                                       "Gypsy",
                                       "Wu"])
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
        try:
            all_text, session['len_all_text'] = download_subtitles.give_me_subs()
        except FileNotFoundError:
            flash("We can't process this video. Try different one.")
            return redirect(url_for('index'))
        return redirect(url_for('result'))
    return render_template('index.html', form=form)


@app.route("/track", methods=["GET"])
def track():
    return str(session['len_all_text'])


@app.route('/result', methods=['GET', 'POST'])
def result():
    global all_text
    translate = Languages()

    # This part is responsible for translation
    if request.method == 'POST' and translate.validate_on_submit():
        summary = ai_functions.translate(translate.languages.data, session['summary'])
        summary2 = ai_functions.translate_summary2(translate.languages.data, session['summary2']).split('\n')
        return render_template('result.html', summary=summary, summary2=summary2,
                               end_for_embed=session['end_for_embed'], translate=translate)

    # This part is responsible for fetching data from index and sending them to ai api
    if "data" in session.keys():
        try:
            summary, summary2 = ai_functions.splitting_tasks(all_text)
            session['summary'] = summary
            session['summary2'] = summary2
            ic(summary2)
            session.pop('data', None)
        except FileNotFoundError:
            flash("We can't process this video. Try different one.")
            return redirect(url_for('index'))
        return render_template('result.html', summary=summary, summary2=summary2,
                               end_for_embed=session['end_for_embed'], translate=translate)

    # This part is when we have results and only refresh the page
    if "summary" in session.keys():
        print(session['summary2'])
        return render_template('result.html', summary=session['summary'], summary2=session['summary2'],
                               end_for_embed=session['end_for_embed'], translate=translate)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)