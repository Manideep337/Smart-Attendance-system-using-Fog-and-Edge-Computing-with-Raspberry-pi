import cv2
# import dlib
import os

cam = cv2.VideoCapture("student_capture.mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):

    # reading from frame
    ret,frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)

        # writing the extracted images
        if currentframe %8 == 0:
            cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
# For static images:
IMAGE_FILES1 = os.listdir(os.getcwd()+'/data')
IMAGE_FILES = []
for i in IMAGE_FILES1:
    if i[-1] =='g':
        IMAGE_FILES.append("data/"+i)
print(IMAGE_FILES)
for i in range(len(IMAGE_FILES)):
    img = cv2.imread(IMAGE_FILES[i])

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]
        faces = cv2.resize(faces, (100, 100))
        cv2.imshow("face"+str(i),faces)
        faces = cv2.cvtColor(faces, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('Recognition/faces/video/face'+str(i)+'.jpg', faces)
        print("faces"+str(i)+'.jpg done')



#%%
