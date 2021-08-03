
from flask import Flask, render_template, Response
import cv2
import numpy as np
app=Flask(__name__)




def gen():
    camera = cv2.VideoCapture(0)  
    while True:
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        if ret == False:
            continue
        # encode the frame in JPEG format
        encodedImage = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + bytearray(np.array(encodedImage)) + b'\r\n')

@app.route('/')
def index():
    # return the rendered template
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
   app.run(debug = True)