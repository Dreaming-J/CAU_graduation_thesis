import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from trainer import Model
import dlib
import cv2
import torch
import time

# dlib 얼굴 추출기 및 랜드마크 예측기
print("loading face landmarks predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/shape_predictor_68_face_landmarks.dat")

# 웹캠 변수
print("loading camera...")
webcam = cv2.VideoCapture(0)

# 학습 모델 변수
print("loading model...")
model = Model.MyModel()
model.load_state_dict(torch.load("./model/detect_eye_blink_model.pth"))
model.eval()

# 변수 초기값
isclosed = None
