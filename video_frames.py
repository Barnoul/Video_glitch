import cv2
import os

def frames(video_name):
    cap = cv2.VideoCapture(video_name)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Saves image of the current frame in jpg file
        name = 'frame' + str(currentFrame) + '.jpg'
        print(f'Creating...{name}')
        cv2.imwrite(f"./data/{name}", frame)
        currentFrame += 1

        if not ret: break

    cap.release()
    cv2.destroyAllWindows()