import cv2
import os

img = cv2.imread("Flower.jpg")  # Replace with your image file

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
for i in range(256):  # Map full range of characters
    d[chr(i)] = i

# Store message length in the first few pixels
msg_length = len(msg)
img[0, 0, 0] = msg_length  # Store length in the first pixel

n, m, z = 0, 1, 0  # Start after the first pixel

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)  # Use PNG to avoid compression
os.system("start encryptedImage.png")  # Open the image

# Save the password for decryption
with open("password.txt", "w") as f:
    f.write(password)
