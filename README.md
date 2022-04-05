# A simple automation for my media server for downloading seasonals

This is something I made to learn python, and I gotta say, not to bad for my first script. 
*I think* 
The script gets the latest file from the desired show folder per week, makes a new folder in your media server folder with the show name, and finally copies the file over for your plex/jellyfin to pick up.

### Make sure to have the desired GDrive folder mounted with rclone or raidrive

To run the automation you need to add a `queue.txt` file, this will be a list of directories that the script will watch. Make sure to change the `target_dirloc` and `queue.txt` filepaths respectively in `main.py`

Now to make it an automation: you have to create a `automation.bat` (to make it an executable) file that looks like this:
```
"C:\Python310\python.exe" "C:\Code Projects\jellyfin-scheduler\main.py" 
pause
```
And finally add the `.bat` file to windows task scheduler to have your seasonals download automatically!

### The script's a little more useful now after the recent update :)
