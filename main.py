import datetime

import streamlit as st
import cv2
import time

st.title("Web Motion Detector")
start = st.button("Start Camera")

today_time = time.time()

if start:
    start_img = st.image([])
    camera = cv2.VideoCapture(1)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        today_time = datetime.datetime.now().replace(microsecond=0)

        cv2.putText(img=frame,
                    text=f"{today_time}",
                    org=(50,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20,100,200),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        start_img.image(frame)