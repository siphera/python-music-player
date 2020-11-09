from tkinter import *
import pygame
from pygame import mixer

root = Tk()
root.title('MP3 Player')
root.geometry("806x230")

# Initialze Pygame Mixer
pygame.mixer.init()


def play():
    mixer.music.load('Inkedama1.wav')
    mixer.music.play()


def pause():
	mixer.music.pause()


def unpause():
	mixer.music.unpause()


def stop():
	mixer.music.stop()


label_frame1 = LabelFrame(root, text="Song Playing", font=("arial", 10, "bold"), pady=8, padx=8)
label_frame1.place(x=10, y=10)
song_box = Listbox(label_frame1, bg="brown", fg="green", width=43, height=5, selectbackground="green", selectforeground="black")
song_box.grid(row=0, column=0)

controls = LabelFrame(root, text="Controls", font=("arial", 10, "bold"), pady=10, padx=10)
controls.place(x=10, y=140)

play_button = Button(controls, text="Play", borderwidth=1, command=play)
pause_button = Button(controls, text="pause", borderwidth=1, command=pause)
stop_button = Button(controls, text="stop", borderwidth=1, command=stop)
unpause_button = Button(controls, text="Unpause", borderwidth=1, command=unpause)

play_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
stop_button.grid(row=0, column=3, padx=10)
unpause_button.grid(row=0, column=2, padx=10)


playlist_frame = LabelFrame(root, text="playlist", font=("arial", 10, "bold"), pady=8, padx=8)
playlist_frame.place(x=400, y=10)
playlist = Listbox(playlist_frame, bg="brown", fg="green", width=47, height=9, selectbackground="green", selectforeground="black")
playlist.grid(row=0, column=0)

root.mainloop()
