from moviepy.editor import *
from os import rename
from multiprocessing import Process

# Directory Constants
ORIGINAL_DIRECTORY = "D:\\Users\\lucea\\Videos\\Hunt  Showdown\\"
HIGHLIGHT_DIRECTORY = "D:\\Users\\lucea\\Videos\\Hunt  Showdown\\Highlights\\"

# Converts time strings in the format "Minutes Seconds" to required tuple (minutes, seconds)
def string_to_tuple(string):
    split_string = string.split(" ")
    int_list = []
    for element in split_string:
        int_list.append(int(element))
    return tuple(int_list)

def clip_video(original_path, start_time, end_time, highlight_name):
    # Accesses raw video footage
    original_file = VideoFileClip(original_path)

    # Converts inputed times to tuples
    start_time_tuple = string_to_tuple(start_time) # 1 22 for test
    end_time_tuple = string_to_tuple(end_time) #  2 30 for test

    #Clips file to desired length
    highlight_file = original_file.subclip(start_time_tuple, end_time_tuple)

    # Creates file path and exports video to highlights folder
    highlight_path = HIGHLIGHT_DIRECTORY + highlight_name + ".mp4"
    highlight_file.write_videofile(highlight_path, temp_audiofile="D:\\Users\\lucea\\Videos\\Hunt  Showdown\\tmp\\random_name.mp3")

    # Closes both files
    original_file.reader.close()
    original_file.audio.reader.close_proc()
    highlight_file.reader.close()
    highlight_file.audio.reader.close_proc()

if __name__ == "__main__":

    try:
        # Data Input
        original_name = input("Original name of video: ")
        start_time = input("Start time [minutes seconds]: ")
        end_time = input("End time [minutes seconds]: ")
        highlight_name = input("Name of highlight: ")

        # Adds the file name to the path
        original_path = ORIGINAL_DIRECTORY + original_name + ".mp4"

        #Hunt  Showdown 2019.07.03 - 21.54.55.07.DVR
        file_edit = Process(target=clip_video(original_path, start_time, end_time, highlight_name))
        file_edit.start()
        file_edit.join()  # Waits until the clip_video function has finished executing
        rename(original_path, ORIGINAL_DIRECTORY + original_name + "_EDITED" + ".mp4")
    except Exception as e: print(e) 
    
    finally:
        input("Press enter to continue")
