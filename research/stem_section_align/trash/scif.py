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
        if m.distance < 0.75 * n.distance:
            good.append(m)
    return good


def siftImageAlignment(img1, img2):
    _, kp1, des1 = sift_kp(img1)
    _, kp2, des2 = sift_kp(img2)
    goodMatch = get_good_match(des1, des2)
    print('goodMatch is: ' + str(goodMatch))

    if len(goodMatch) > 4:
        ptsA = np.float32([kp1[m.queryIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
        ptsB = np.float32([kp2[m.trainIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
        ransacReprojThreshold = 0.02
        H, status = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, ransacReprojThreshold)
        img3 = cv2.warpPerspective(img2, H, (img1.shape[1], img1.shape[0]),
                                   flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
    return img3, H, status


for i in range(70, 87):
    file_lolcation = r"E:\OneDrive\Temp\Subject\Nano-3D"
    img1 = cv2.imread(file_lolcation + r"\\" + str(i) + '.tif')
    img2 = cv2.imread(file_lolcation + r"\\" + str(i + 1) + '.tif')
    img3, _, _ = siftImageAlignment(img1, img2)
    cv2.imwrite('scf1_' + str(i + 1) + '.tif', img3)
