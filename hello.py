import streamlit as st
from ultralytics import YOLO
import cv2

st.title('This is a title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')


picture = st.camera_input("Take a picture")
model = YOLO('../Yolo-Weights/yolov8l.pt')

results = model(picture, show=True)

cv2.waitKey(0)
st.image(results)