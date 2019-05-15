from __future__ import print_function
import cv2
import numpy as np

MAX_FEATURES = 1000
GOOD_MATCH_PERCENT = 0.01


def alignImages(im1, im2):
    # Convert images to grayscale


    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    cv2.imwrite("matches.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography

    height, width, chanels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h


if __name__ == '__main__':
    refFilename = r"E:\OneDrive\Documents\Python_Jun\research\stem_section_align\71.jpg"
    imFilename = r"E:\OneDrive\Documents\Python_Jun\research\stem_section_align\72.jpg"
    imReference = cv2.imread(refFilename, 1)
    im = cv2.imread(imFilename, 1)

    imReg, h = alignImages(im, imReference)
    cv2.imwrite("scf3.jpg", imReg)
    print("Estimated homography : \n", h)
