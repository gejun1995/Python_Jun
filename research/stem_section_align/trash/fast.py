from PIL import Image, ImageChops
import cv2

img_pre=cv2.imread("70.tif")
img_current = cv2.imread("71.tif")

fast = cv2.FastFeatureDetector_create()

kp_pre = fast.detect(img_pre,None)
kp_current = fast.detect(img_current,None)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img_pre, None)
kp2, des2 = orb.detectAndCompute(img_current, None)
print(kp1)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.match(des1, des2, k=2)
print(matches)
good = [m for (m, n) in matches if m.distance < 0.5 * n.distance]
similary = len(good) / len(matches)
print("Current good  number is: " + str(len(good)))
print("Current matches number is: " + str(len(matches)))
print("Current similarity is: %s" % similary)

'''
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.knnMatch(kp_pre, kp_current,k=0)
good = [m for (m, n) in matches if m.distance < 0.5 * n.distance]
similary = len(good) / len(matches)
print("Current good  number is: " + str(len(good)))
print("Current matches number is: " + str(len(matches)))
print("Current similarity is: %s" % similary)
img_points = cv2.drawKeypoints(img_current,kp_pre,img_current,color=(255,0,0))



print(kp_pre[0])

cv2.imwrite('test.tif', img_points)
'''