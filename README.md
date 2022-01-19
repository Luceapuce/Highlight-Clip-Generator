# Gameplay Highlight Clip Generator
## Introduction
A basic personal project to export a trimmed gameplay clip, primarily for videos taken using Nvidias instant replay service, to a highlights folder in the same directory. This allows the original clips to be deleted and saves space as they are often much longer than required. The program will append `_EDITED` to the end of the original clip's name to show that it is safe to delete. 

## Instructions
- First save and run the .py file onto your computer. The `game_list.json` will be created automatically.
- The program will have no game locations saved during the first run, press 'A' to add a new game (not case sensitive).
- Insert the exact name of the game as shown in your personal 'Videos' folder. Be careful as sometimes these can be different to what you would expect. For Example, Hunt Showdown in the image below actually has 2 spaces.
![Video Location Screenshot](https://imgur.com/DqNZOBp.png)
- This will add the game location to a file so you don't need to re-add this game each time. You can also remove this by pressing `R` when prompted and typing the number associated with the game you wish to delete. 
- To clip a highlight, press the number of the game folder you wish to access. 
- Type in the exact name of the video file you want to edit, the easiest way to get this is to right click > rename > copy. You do not need to include the file extension. 
- Type in the start time of the subclip you wish to create in the format `mm ss` e.g. 4 32 will begin clipping at 4 minutes and 32 seconds.
- Do the same for the end time of the subclip using the same format.
- Input the name for your subclip to be saved as.
- The program will then process the clip, saving it within the games folder in a folder called 'Highlights' that the program will create if it doesn't already exist. It will also add `_EDITED` to the end of the original file to show that you have already clipped that file.

![Highlight Location Screenshot](https://imgur.com/OZoVELc.png)
- Once this has completed, press `1` to export another clip or press `0` to exit. 


## To-do
- [x] Add a loop to export multiple videos in the same instance of the program.
- [x] Add functionality for multiple games
- [x] Add a feature within the program to add different games without having to edit the constants.py file manually. 
- [x] Automatically detecting the Video libraries location.
- [x] Make inputs not case-sensitive