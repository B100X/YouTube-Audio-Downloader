# If you want, you can download the best audio.

import pafy


url = "Put here your YouTube Video URL."
video = pafy.new(url)


bestaudio = video.getbestaudio()
bestaudio.download()
