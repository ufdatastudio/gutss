
import os
import cv2
from cap_from_youtube import cap_from_youtube

## resources:
## https://pythonhosted.org/pafy/ for pafy documentation/ swapped out of this
## https://pypi.org/project/cap-from-youtube/ for cap_from_youtube
## https://realpython.com/run-python-scripts/ for executing python files on terminal
## https://www.geeksforgeeks.org/create-a-directory-in-python/ creating python directories
## https://www.geeksforgeeks.org/extract-images-from-video-in-python/ how to get the frames
## https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/ extract frames
## https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704daf01bc92359d2abc9e6eeb5cbe36d9af2 opencv frame doc
## learning how any works https://www.geeksforgeeks.org/python-any-function/

## a function to try to get the frames of 1 video
def extractFrames(vid, frameDir):
    print("Starting to run")

    counter = 0;
    secCounter = 0;

    fps = vid.get(cv2.CAP_PROP_FPS) ## opencv doc says fps code
    perSecs = 15

    sharkFrameNum = fps * perSecs

    ## numOfFrames = vid.get(cv2.CAP_PROP_FRAME_COUNT) ## opencv doc says total frame count code
    ## vidLength = numOfFrames / fps  
    
    ## print(str(vidLength))

    while(True):
        vid.set(cv2.CAP_PROP_POS_FRAMES, secCounter)

        ret, frame = vid.read()

        if ret:
            name = str(frameDir) + '/frame' + str(counter) + '.jpg'
            cv2.imwrite(name, frame)
            counter += 1
        else:
            break
        secCounter += sharkFrameNum

    vid.release()
    cv2.destroyAllWindows()

sharkVid = cv2.VideoCapture('.mp4')

filesInDir = os.listdir(".")
if any(File.endswith(".mp4") for File in filesInDir): ## thhanks for geeks for geeks for any
    for File in filesInDir:
        if (File.endswith(".mp4")):
            print("works")
            path = os.getcwd() + '\\' + File
            print(path)
            sharkVid = cv2.VideoCapture(path)
else:
    sharkVidURL = 'https://www.youtube.com/watch?v=6GbJWJ3Swsc'
    sharkVid = cap_from_youtube(sharkVidURL, 'best')

## checking if there is a folder in the current directory for the images
if not os.path.isdir('Frames'):
    curr_dir = os.getcwd()
    path = os.path.join(curr_dir, "Frames")
    os.mkdir(path)
## print(curr_dir)
path = os.getcwd() + '\Frames'

if sharkVid.isOpened():
    extractFrames(sharkVid, path)
    print("Done!")
## ret, frame = sharkVid.read()
