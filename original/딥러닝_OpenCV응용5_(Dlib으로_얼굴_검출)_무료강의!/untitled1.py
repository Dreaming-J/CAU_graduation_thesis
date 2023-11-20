import dlib
import cv2
import imutils
import numpy as np
from imutils import face_utils
import matplotlib.pyplot as plt

# dlib 얼굴 추출기 초기화
detector = dlib.get_frontal_face_detector()
# 얼굴 랜드마크 예측기 생성
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

image = cv2.imread("face.jpg")
# 이미지 크기 변경
image = imutils.resize(image, width=500)

# 얼굴 영역 및 랜드마크 추출
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 얼굴 영역 검출
# 두번째 파라미터는 업샘플링 수로 더 많은 인식을 하지만 느려지고 메모리 소모 심함
rects = detector(gray, 1)

# 검출된 얼굴들에 대해 반복 (얼굴 인덱스, 얼굴 좌표)
for (i, rect) in enumerate(rects):
    # 얼굴 영역의 랜드마크를 찾고 랜드마크 좌표를 배열로 변환
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)
    
    # 좌상단좌표(x, y), 너비와 높이(w, h)를 가져와서 얼굴영역을 그림
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # 얼굴의 인덱스를 표시
    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # 원본 이미지에 랜드마크를 점으로 표시
    for (x, y) in shape:
        cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
        
    print("얼굴 수 : {} (Left: {} Top: {} Right: {} Bottom: {}".format(
        i + 1, rect.left(), rect.top(), rect.right(), rect.bottom()))
    
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
plt.xticks([]), plt.yticks([])
plt.imshow(image)
plt.show()
