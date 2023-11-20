from scipy.spatial import distance as dist


def eye_aspect_ratio(shape_eye):
    A = dist.euclidean(shape_eye[1], shape_eye[5])
    B = dist.euclidean(shape_eye[2], shape_eye[4])
    C = dist.euclidean(shape_eye[0], shape_eye[3])
    ear = (A + B) / (2.0 * C)
    return ear * 100


def getEAR(shape_eyes):
    for (i, shape_eye) in enumerate(shape_eyes):
        shape_eyes[i] = eye_aspect_ratio(shape_eye)
    return shape_eyes
