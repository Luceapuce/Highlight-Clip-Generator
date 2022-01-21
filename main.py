import configparser
from tkinter import *
from tkinter.messagebox import showinfo
from moviepy.editor import VideoFileClip
from tkinter.filedialog import askopenfilename
import os

config = configparser.ConfigParser()


def setup_ui():
    global filename, start_time, end_time, highlight_name, error_label, highlight_location
    window = Tk()
    window.geometry("600x250")

    title = Label(text="Nvidia Instant Replay Clip Trimmer",
                  font=("Arial", 14), padx=5, pady=10)
    title.grid(column=0, row=0, columnspan=3)

    # Labels
    highlight_location_label = Label(text="Highlight Folder:")
    highlight_location_label.grid(column=0, row=1)

    select_file_label = Label(text="Video file:")
    select_file_label.grid(column=0, row=2)

    start_time_label = Label(text="Start time [mm ss]:")
    start_time_label.grid(column=0, row=3)

    end_time_label = Label(text="End time [mm ss]:")
    end_time_label.grid(column=0, row=4)

    highlight_name_label = Label(text="Name of highlight:")
    highlight_name_label.grid(column=0, row=5)

    # Inputs
    highlight_location = Entry(width=55)
    if os.path.exists('config.ini'):
        config.read('config.ini')
        highlight_location.insert(END, config.get('File Paths', 'highlights'))

    highlight_location.grid(column=1, row=1, sticky="W")

    save_location_button = Button(
        text="Save Location", command=lambda: write_config(highlight_location.get()))
    save_location_button.grid(column=2, row=1, sticky="W", padx=10)

    select_file_button = Button(
        text="Select file", command=select_file, width=60)
    select_file_button.grid(column=1, row=2, columnspan=2, sticky="W")

    start_time = Entry(width=70)
    start_time.grid(column=1, row=3, columnspan=2, sticky="W")

    end_time = Entry(width=70)
    end_time.grid(column=1, row=4, columnspan=2, sticky="W")

    highlight_name = Entry(width=70)
    highlight_name.grid(column=1, row=5, columnspan=2, sticky="W")

    clip_video_button = Button(
        text="Clip video", command=clip_video, width=78)
    clip_video_button.grid(column=0, row=6, columnspan=3, sticky="W", padx=20)

    col_count, row_count = window.grid_size()

    for col in range(col_count):
        window.grid_columnconfigure(col, minsize=150)

    for row in range(row_count):
        window.grid_rowconfigure(row, minsize=30)

    window.mainloop()


def select_file():
    global filename
    filename = askopenfilename(
        title='Open a video file',
        initialdir='/',
        filetypes=[("MP4 files", "*.mp4")])


def string_to_tuple(string):
    # Converts time strings in the format "Minutes Seconds" to required tuple (minutes, seconds)
    split_string = string.split(" ")
    int_list = []
    for element in split_string:
        int_list.append(int(element))
    return tuple(int_list)


def clip_video():
    global filename, start_time, end_time, highlight_name

    # Accesses raw video footage
    original_file = VideoFileClip(filename)

    # Converts times to tuples
    start_time_tuple = string_to_tuple(start_time.get())
    end_time_tuple = string_to_tuple(end_time.get())

    # Clips file to desired length
    highlight_file = original_file.subclip(start_time_tuple, end_time_tuple)

    # Creates file path and exports video to highlights folder
    game_name = filename.split("/")[-2]
    game_path = highlight_location.get() + "\\" + game_name

    # Creates highlight folder inside the game folder if one doesn't already exist
    if not os.path.exists(game_path):
        os.mkdir(game_path)
    clip_path = game_path + "\\" + highlight_name.get() + ".mp4"
    highlight_file.write_videofile(
        clip_path, temp_audiofile=game_path + "\\random_name.mp3")

    # Closes both files
    original_file.reader.close()
    original_file.audio.reader.close_proc()
    highlight_file.reader.close()
    highlight_file.audio.reader.close_proc()

    # Renames video
    os.rename(filename, filename.replace(".mp4", "_EDITED.mp4"))


def write_config(value):
    config['File Paths'] = {'Highlights': value}
    config.write(open('config.ini', 'w'))


setup_ui()
