import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileCilp(video)
audio = video.audio

audio.write_audiofile("video")
print("Completed!..")