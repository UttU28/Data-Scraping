import subprocess
import cv2
import numpy as np

def get_live_feed():
    # Start the adb command to get the screen feed
    command = ['adb', 'exec-out', 'screenrecord', '--bit-rate', '6000000', '--time-limit', '60', '/sdcard/screen.mp4']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Start capturing video
    while True:
        # Use adb to get a single frame from the device
        frame = subprocess.run(['adb', 'exec-out', 'screencap', '-p'], stdout=subprocess.PIPE).stdout
        # Convert the frame to a numpy array and then to an image
        img = cv2.imdecode(np.frombuffer(frame, np.uint8), cv2.IMREAD_COLOR)

        if img is not None:
            cv2.imshow('Live Feed', img)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    process.terminate()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    get_live_feed()
