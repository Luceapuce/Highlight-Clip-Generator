from moviepy.editor import *
from os import rename
ORIGINAL_DIRECTORY = "D:\\Users\\lucea\\Videos\\Hunt  Showdown\\"
HIGHLIGHT_DIRECTORY = "D:\\Users\\lucea\\Videos\\Hunt  Showdown\\Highlights\\"

# Converts times to required tuple
def string_to_tuple(string):
    split_string = string.split(" ")
    int_list = []
    for element in split_string:
        int_list.append(int(element))
    return tuple(int_list)

# Data Input
original_name = input("Original name of video: ")
start_time = input("Start time [minutes seconds]: ")
end_time = input("End time [minutes seconds]: ")
highlight_name = input("Name of highlight: ")

# Creates file path and accesses original video
original_path = ORIGINAL_DIRECTORY + original_name
original_file = VideoFileClip(original_path)

# Converts inputed times to tuples
start_time_tuple = string_to_tuple(start_time) # 1 22 for test
end_time_tuple = string_to_tuple(end_time) #  2 30 for test

#Clips file to desired length
highlight_file = original_file.subclip(start_time_tuple, end_time_tuple)

# Creates file path and exports video
highlight_path = HIGHLIGHT_DIRECTORY + highlight_name
highlight_file.write_videofile(highlight_path)
