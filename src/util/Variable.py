import dlib
import cv2

print("loading face landmarks predictor...")
detector = dlib.get_frontal_face_detector()  # dlib 얼굴 추출기 초기화
predictor = dlib.shape_predictor("./data/shape_predictor_68_face_landmarks.dat")  # 얼굴 랜드마크 예측기 생성

# 웹캠 관련 변수들
print("starting camera...")
webcam = cv2.VideoCapture(0)
