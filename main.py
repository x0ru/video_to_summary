import time
from flask import Flask, render_template, redirect, flash, url_for, session, request
from wtforms import SubmitField, StringField
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import InputRequired
import ai_functions
import download_subtitles
import secrets


# TODO: 1. Create history of searches. Last 3 searches can be stored in memory. << this maybe with point 5
#       2. Do example so people can see random links for video.
#       3. Embedd video.
#       4. Progress bar.
#       5. Account handling + db wit last searches ? So this way we can see history.

app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = 'gmbnvmmvm'
csrf = CSRFProtect(app)


class PasteVideo(FlaskForm):
    video_link = StringField('here link please', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasteVideo()
    if request.method == 'POST' and form.validate_on_submit():
        session['data'] = form.video_link.data
        return redirect(url_for('result'))
    return render_template('index.html', form=form)



@app.route('/result', methods=['GET', 'POST'])
def result():
    if "data" in session.keys():
        try:
            time_start = time.time()
            download_subtitles.download_sub(session["data"])
            session.pop('data', None)
            summary, summary2 = ai_functions.splitting_tasks(download_subtitles.give_me_subs())
            session['summary'] = summary
            session['summary2'] = summary2
            time_stop = time.time()
            time_diff = time_stop - time_start
            print(time_diff)
            if time_diff < float(13.8):
                print(13.8 - time_diff, "sleeping")
                time.sleep(13.8 - time_diff)
        except FileNotFoundError:
            return render_template('fail.html')
        return render_template('result.html', summary=summary, summary2=summary2)
    if "summary" in session.keys():
        return render_template('result.html', summary=session['summary'], summary2=session['summary2'])
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
