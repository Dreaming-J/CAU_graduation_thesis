from imutils import face_utils

ESC = 27
RED = (0, 0, 255)
GREEN = (0, 255, 0)

# 귀의 인덱스 번호
idx_eyes = [face_utils.FACIAL_LANDMARKS_IDXS["left_eye"], face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]]
