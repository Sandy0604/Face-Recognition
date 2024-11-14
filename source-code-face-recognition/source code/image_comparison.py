import cv2
import face_recognition

# Load and check the first image
img = cv2.imread("source code\Messi1.webp")
if img is None:
    raise FileNotFoundError("Check the file path.")

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

# Load and check the second image
img2 = cv2.imread("source code\images\Elon Musk.jpg")
if img2 is None:
    raise FileNotFoundError("Check the file path.")

rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

# Compare the faces
result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)

# Display the images
cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
