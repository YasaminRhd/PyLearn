from moviepy import editor

video = editor.VideoFileClip('assignment7/Rage_Against.mp4')
video.audio.write_audiofile('assignment7/rage_againt_audio.mp3')