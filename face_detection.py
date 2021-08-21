import cv2

cap = cv2.VideoCapture(0)  # Read the video from computer camera
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:   # Infinite loop
    ret, frame = cap.read();  # if "cap" is able to rea the video then ret wil be true and frame is the matrix of the image
    if ret:
        faces = detector.detectMultiScale(frame)
        for face in faces:
            (x, y, w, h) = face
            print((x, y, w, h))
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            #cut = frame[]
        cv2.imshow("My Screen", frame)  # Display the images

    key = cv2.waitKey(1)  # taking 1 milli seconds to grab the data
    if key == ord("q"):  # Unicode of q
        break
cap.release()
cv2.destroyAllWindows()