import cv2

img = cv2.imread("encryptedImage.png")  # Read the encrypted image

c = {}
for i in range(256):  # Map full range of characters
    c[i] = chr(i)

# Retrieve stored message length
msg_length = img[0, 0, 0]  # Read length from first pixel

n, m, z = 0, 1, 0  # Start after the first pixel
message = ""

# Read stored password
with open("password.txt", "r") as f:
    saved_password = f.read().strip()

pas = input("Enter passcode for Decryption: ")

if saved_password == pas:
    for i in range(msg_length):  # Read only the stored message length
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption successful! Message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
