import yt_dlp
import srt

url = "https://www.youtube.com/watch?v=w5Wr3j4h_1I"

ydl_opts = {
  'writeautomaticsub': True,
  'subtitlesformat': 'srt',
  'skip_download': True,
  'outtmpl': 'sub.srt'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download([url])


with open('sub.srt.en.vtt') as f:
    for i in range(3):
        next(f)
    for line in f:
        subtitle_generator = srt.parse(f)
        subtitles = list(subtitle_generator)
        for sub in subtitles:
            if "<" not in sub.content:
                print(sub.content)
