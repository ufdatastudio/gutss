
import os
import cv2
from cap_from_youtube import cap_from_youtube

## resources:
## https://pythonhosted.org/pafy/ for pafy documentation/ swapped out of this
## https://pypi.org/project/cap-from-youtube/ for cap_from_youtube
## https://realpython.com/run-python-scripts/ for executing python files on terminal
## https://www.geeksforgeeks.org/create-a-directory-in-python/ creating python directories

sharkVidURL = 'https://www.youtube.com/watch?v=6GbJWJ3Swsc'
sharkVid = cap_from_youtube(sharkVidURL, 'best')

## should print true if it works
if (sharkVid.isOpened()):
    print(sharkVid.isOpened()) 

## checking if there is a folder in the current directory for the images
curr_dir = os.getcwd()
