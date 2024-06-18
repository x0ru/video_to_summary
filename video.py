from pytube import YouTube


def video(link):
    yt = YouTube(link , on_progress_callback=on_progress)
    title = yt.title
    captions = yt.captions.keys()
    print(captions)
    print('executing download')
    yt.streams.filter(only_audio=True).first().download()
    print('finishing download')
    return title


def on_progress(stream, chunk, bytes_remaining):
    print(bytes_remaining)
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    per = str(int(percentage)) + '%'
    print(bytes_remaining)
    print(per)


if __name__ == "__video.py__":
    print('hi')
