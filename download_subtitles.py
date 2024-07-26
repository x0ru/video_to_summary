import yt_dlp
import srt


def download_sub(url):
    url = f"{url}"
    ydl_opts = {
      'writeautomaticsub': True,
      'subtitlesformat': 'srt',
      'skip_download': True,
      'outtmpl': 'sub.srt'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except:
            return False


def give_me_subs():
    with open('sub.srt.en.vtt') as f:
        new_text = ""
        all_text = []
        for i in range(3):
            next(f)
        subtitle_generator = srt.parse(f)
        subtitles = list(subtitle_generator)
        for sub in subtitles:
            if "<" not in sub.content:
                new_text += sub.content
                if len(new_text) > 50000:
                    all_text.append(new_text)
                    new_text = ''
        all_text.append(new_text)

    return all_text, len(all_text)


