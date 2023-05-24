import cv2

video = cv2.VideoCapture('ATLAEPS/ATLAS1EP1.mp4')

if (video.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (video.isOpened()):
    # Capture frame-by-frame
    ret, frame = video.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
video.release()

# Closes all the frames
cv2.destroyAllWindows()
