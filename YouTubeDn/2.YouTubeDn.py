import pytube
from pytube import YouTube
from pytube.extract import ProgressBar

yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
video = yt.streams.first()

# Create a progress bar object
pb = ProgressBar(video)

# Download the video and display the progress bar
video.download("/path/to/save/location", on_progress=pb.on_progress)

# Select the video with 720p resolution
video = yt.streams.filter(resolution="720p").first()
video.download("/path/to/save/location")
