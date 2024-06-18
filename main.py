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
    form = PasteVideo()
    if form.validate_on_submit():
        try:
            download_subtitles.download_sub(form.video_link.data)
            summary = ai_functions.summary().split('\n')
            summary2 = ai_functions.summary_2()
        except FileNotFoundError:
            return render_template('fail.html')
        return render_template('ulala.html', summary=summary, summary2=summary2)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
