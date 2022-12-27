from pytube import YouTube


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")


url = input('Link khod Ra Paste knid: ')
yt = YouTube(url, on_progress_callback=on_progress)

out = yt.streams\
    .filter(progressive=True, file_extension='mp4')\
    .order_by('resolution')\
    .desc()\
    .first()\
    .download()

print(f"Download Shoma Ba Movfaghiyat Anjam Shd: {out}")
