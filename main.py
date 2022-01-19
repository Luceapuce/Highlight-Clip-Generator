from tkinter import *
from tkinter.filedialog import askopenfilename


def clip_video():
    pass


def setup_ui():
    window = Tk()

    title = Label(text="Nvidia Instant Replay Clip Trimmer")
    title.grid(column=0, row=0)

    # Labels
    select_file_label = Label(text="Video file:")
    select_file_label.grid(column=0, row=1)

    start_time_label = Label(text="Start time [mm ss]:")
    start_time_label.grid(column=0, row=2)

    end_time_label = Label(text="End time [mm ss]:")
    end_time_label.grid(column=0, row=3)

    highlight_name_label = Label(text="Name of highlight:")
    highlight_name_label.grid(column=0, row=4)

    # Inputs
    # select_file_input = Button(command=askopenfilename())
    start_time_input = Entry()
    end_time_input = Entry()
    highlight_name_input = Entry()

    clip_video_button = Button(command=clip_video())

    window.mainloop()


def select_file():
    filename = askopenfilename(
        title='Open a video file',
        initialdir='/',
        filetypes=("mp4 video files", ".mp4"))


setup_ui()
