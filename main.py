import tkinter as tk
from PIL import ImageTk, Image
from pytube import YouTube
from pytube import Playlist
import os


def convert(textbox):
    try:
        yt_playlist = Playlist(str(textbox))
        for yt_playlist in yt_playlist.videos:
            mp3 = yt_playlist.streams.filter(only_audio=True).first()
            out_file = mp3.download(output_path=f'{os.path.expanduser("~")}\Music')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

    except KeyError:
        try:
            yt = YouTube(str(textbox))
            mp3 = yt.streams.filter(only_audio=True).first()
            out_file = mp3.download(output_path=f'{os.path.expanduser("~")}\Music')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        except Exception:
            error = tk.Label(frame, text="invalid link", font='Calibre 13', fg='white', bg='#202021')
            error.place(relx=0.18, rely=0.55, relwidth=0.65)


root = tk.Tk()
root.title('Youtube 2 Spotify Converter')


canvas = tk.Canvas(root, height=260, width=530)
canvas.pack()

frame = tk.Frame(root, bg='#202021')
frame.place(relheight=1, relwidth=1)

title = tk.Label(frame, text="Youtube 2 Spotify\nConverter", font='Calibre 18', fg='white', bg='#202021')
title.place(relx=0.28, rely=0, relwidth=0.45, relheight=0.25)

youtube_img = ImageTk.PhotoImage(Image.open('./assets/youtube.png'))
youtube_label = tk.Label(image=youtube_img, bg='#202021')
youtube_label.place(relx=0.1, rely=0.26)

arrow = tk.Label(frame, text="➜", font='Calibre 35', fg='white', bg='#202021')
arrow.place(relx=0.28, rely=0.28, relwidth=0.45, relheight=0.25)

spotify_img = ImageTk.PhotoImage(Image.open('./assets/spotify.png'))
spotify_label = tk.Label(image=spotify_img, bg='#202021')
spotify_label.place(relx=0.75, rely=0.2)

textbox = tk.Entry(frame)
textbox.place(relx=0.18, rely=0.67, relwidth=0.65)

convert_button = tk.Button(frame, text="convert", font='Calibre 15', bg='#7BD373', command=lambda: convert(textbox.get()))
convert_button.place(relx=0.325, rely=0.8, relwidth=0.35, relheight=0.12)

if __name__ == '__main__':
    root.mainloop()