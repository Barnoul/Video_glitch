from image_processing import *
from video_frames import frames
from moviepy.editor import *
import cv2
import os
import math
in_name = input('Video name: ').split('.')
f = open('path.txt')
initial = VideoFileClip('.'.join(in_name))
project = f.readline()
target = project + '.'.join(in_name)
base = project + '\\data' #change here
destination = project + '\\glitch_data' #change here
videos = []

try:
    if not os.path.exists('glitch_data'):
        os.makedirs('glitch_data')
except OSError:
    print('Error: Creating directory of data')

frames(target)

for i in range(len(list(os.listdir(base)))-1):
    try:
        filename = 'frame' + str(i) + '.jpg'
        path = base + '\\' + filename
        save_as = destination + '\\' + 'glitch_' + filename
        x = col(path)
        y = row(path)
        building(sorting(perception(path), x, y), x, y, pixelmap(path), save_as)
        #redo
        print(f'Glitching...{filename}')
    except OSError:
        break

length = len(list(os.listdir(destination)))
for j in range(math.ceil(length/1000)):
    img_array = []
    if j == math.ceil(length/1000) - 1:
        cap = length % 1000
    else:
        cap = 1000
    for i in range(cap):
        filename = 'glitch_frame' + str(i+j*1000) + '.jpg'
        img = cv2.imread(destination + '\\' + filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
        out_name = 'glitch_' + in_name[0] + str(j) + '.' + in_name[1]
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(out_name, fourcc, initial.fps, size)
        print(f'Combining...{filename}')

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print(f'Completed section {str(j)}')
    videos.append(out_name)

clips = [VideoFileClip(x) for x in videos]
audio = AudioFileClip('.'.join(in_name))
final_video = concatenate_videoclips(clips)
try:
    result = final_video.set_audio(audio)
    result.write_videofile(f"final_{in_name[0]}.mp4")
except:
    final_video.write_videofile(f"final_{in_name[0]}.mp4")

os.system(f'cd {base}')
os.system('cd ..')
for i in videos:
    os.system(f'del {i}')
os.system('del data /Q')
os.system('del glitch_data /Q')
f.close()
