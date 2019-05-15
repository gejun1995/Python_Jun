import numpy as np
import cv2


def sift_kp(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d_SIFT.create()
    kp, des = sift.detectAndCompute(image, None)
    kp_image = cv2.drawKeypoints(gray_image, kp, None)
    return kp_image, kp, des


def get_good_match(des1, des2):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.001 * n.distance:
            good.append(m)
    return good


def siftImageAlignment(img1, img2):
    _, kp1, des1 = sift_kp(img1)
    _, kp2, des2 = sift_kp(img2)
    goodMatch = get_good_match(des1, des2)
    print('goodMatch is: ' + str(goodMatch))
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, goodMatch[:10], None, flags=0)
    return img3


for i in range(70, 87):
    file_lolcation = r"E:\OneDrive\Temp\Subject\Nano-3D"
    img1 = cv2.imread(file_lolcation + r"\\" + str(i) + '.tif')
    img2 = cv2.imread(file_lolcation + r"\\" + str(i + 1) + '.tif')
    img3 = siftImageAlignment(img1, img2)
    cv2.imwrite('sicf2_matches' + str(i + 1) + '.tif', img3)
