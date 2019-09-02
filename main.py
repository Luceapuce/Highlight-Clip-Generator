import os
from moviepy.editor import VideoFileClip
from multiprocessing import Process
import ctypes.wintypes
import sys
import json

SHGFP_TYPE_CURRENT = 0   # Current location of Videos folder, even if moved.
CSIDL_ID = 14 # CSIDL ID for the Videos library
GAMELIST_PATH = os.path.join(sys.path[0], 'game_list.json')

# Sets BASE_DIRECTORY as the path to the users Video library
buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(0, CSIDL_ID, 0, SHGFP_TYPE_CURRENT, buf)
BASE_DIRECTORY = buf.value + "\\"

def string_to_tuple(string):
    # Converts time strings in the format "Minutes Seconds" to required tuple (minutes, seconds)
    split_string = string.split(" ")
    int_list = []
    for element in split_string:
        int_list.append(int(element))
    return tuple(int_list)

def clip_video(original_path, start_time, end_time, highlight_name, chosen_game_index):
    # Accesses raw video footage
    original_file = VideoFileClip(original_path)

    # Converts inputed times to tuples
    start_time_tuple = string_to_tuple(start_time) # 1 22 for test
    end_time_tuple = string_to_tuple(end_time) #  2 30 for test

    #Clips file to desired length
    highlight_file = original_file.subclip(start_time_tuple, end_time_tuple)

    # Creates file path and exports video to highlights folder
    highlight_path = BASE_DIRECTORY + game_list[chosen_game_index] + "\\" + "Highlights" + "\\" + highlight_name + ".mp4"

    if not os.path.exists(BASE_DIRECTORY + game_list[chosen_game_index] + "\\" + "Highlights"): # Creates highlight folder inside the game folder if one doesn't already exist
        os.mkdir(BASE_DIRECTORY + game_list[chosen_game_index] + "\\" + "Highlights")
    highlight_file.write_videofile(highlight_path, temp_audiofile="D:\\Users\\lucea\\Videos\\random_name.mp3")

    # Closes both files
    original_file.reader.close()
    original_file.audio.reader.close_proc()
    highlight_file.reader.close()
    highlight_file.audio.reader.close_proc()

def json_to_list():
    global GAMELIST_PATH
    if os.path.exists(GAMELIST_PATH):
        with open(GAMELIST_PATH, "r") as game_list:
            data = json.load(game_list)
            game_list = []
            for element in data:
                game_list.append(element)
            return game_list
    else:
        game_list = []
        return game_list

def list_to_json(game_list):
    global GAMELIST_PATH
    with open(GAMELIST_PATH, 'w') as output_file:
        json.dump(game_list, output_file)

if __name__ == "__main__":
    not_exited = True
    print(GAMELIST_PATH)
    game_list = json_to_list()

    while not_exited:
        # Game Selection
        adding_games = True
        while adding_games:
            print("List of Games Available:\n")
            for i, item in enumerate(game_list,1):
                print(i, '. ' + item + "\n")
            print("A. Add new game" + "\n")
            print("R. Remove game" + "\n")
            chosen_game = input("Enter the number required, A to add a new game or R to remove a game: ")
            if chosen_game.upper() == "A":
                new_game = input("Enter the exact name of the video file for the new game: ")
                game_list.append(new_game)
                print("Game has been added")
            elif chosen_game.upper() == "R":
                delete_index = int(input("Enter the number associate with the game you wish to delete: ")) - 1
                game_list.pop(delete_index)
            else:
                adding_games = False
                chosen_game_index = int(chosen_game) - 1

        # Data Input
        original_name = input("Original name of video: ")
        start_time = input("Start time [minutes seconds]: ")
        end_time = input("End time [minutes seconds]: ")
        highlight_name = input("Name of highlight: ")

        # Adds the file name to the path
        original_path = BASE_DIRECTORY + game_list[chosen_game_index] + "\\" + original_name + ".mp4"

        try:
            file_edit = Process(target=clip_video(original_path, start_time, end_time, highlight_name, chosen_game_index))
            file_edit.start()
            file_edit.join()  # Waits until the clip_video function has finished executing
            os.rename(original_path, BASE_DIRECTORY + game_list[chosen_game_index] + "\\" + original_name + "_EDITED" + ".mp4")
        except Exception as e: print(e) 
        
        finally:
            user_input_continue = input("Video Complete! Press 1 to export another clip or 0 to exit: ")
            if user_input_continue == "0":
                list_to_json(game_list)
                not_exited = False
            print("--------------------------------------")
                
