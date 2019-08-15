import os
from moviepy.editor import VideoFileClip
from multiprocessing import Process
from constants import *

# Converts time strings in the format "Minutes Seconds" to required tuple (minutes, seconds)
def string_to_tuple(string):
    split_string = string.split(" ")
    int_list = []
    for element in split_string:
        int_list.append(int(element))
    return tuple(int_list)

def clip_video(original_path, start_time, end_time, highlight_name, chosen_game):
    # Accesses raw video footage
    original_file = VideoFileClip(original_path)

    # Converts inputed times to tuples
    start_time_tuple = string_to_tuple(start_time) # 1 22 for test
    end_time_tuple = string_to_tuple(end_time) #  2 30 for test

    #Clips file to desired length
    highlight_file = original_file.subclip(start_time_tuple, end_time_tuple)

    # Creates file path and exports video to highlights folder
    highlight_path = BASE_DIRECTORY + GAME_LIST[chosen_game] + "\\" + "Highlights" + "\\" + highlight_name + ".mp4"
    highlight_file.write_videofile(highlight_path, temp_audiofile="D:\\Users\\lucea\\Videos\\random_name.mp3")

    # Closes both files
    original_file.reader.close()
    original_file.audio.reader.close_proc()
    highlight_file.reader.close()
    highlight_file.audio.reader.close_proc()

if __name__ == "__main__":

    not_exited = True

    while not_exited:
        # Game Selection
        print("List of Games Available:\n")
        for i, item in enumerate(GAME_LIST,1):
            print(i, '. ' + item + "\n")
        chosen_game = int(input("Enter the number required: ")) - 1

        # Data Input
        original_name = input("Original name of video: ")
        start_time = input("Start time [minutes seconds]: ")
        end_time = input("End time [minutes seconds]: ")
        highlight_name = input("Name of highlight: ")

        # Adds the file name to the path
        original_path = BASE_DIRECTORY + GAME_LIST[chosen_game] + "\\" + original_name + ".mp4"

        try:
            file_edit = Process(target=clip_video(original_path, start_time, end_time, highlight_name, chosen_game))
            file_edit.start()
            file_edit.join()  # Waits until the clip_video function has finished executing
            os.rename(original_path, BASE_DIRECTORY + GAME_LIST[chosen_game] + "\\" + original_name + "_EDITED" + ".mp4")
        except Exception as e: print(e) 
        
        finally:
            user_input_continue = input("Video Complete! Press 1 to export another clip or 0 to exit: ")
            if user_input_continue == "0":
                not_exited = False
            print("--------------------------------------")
                
