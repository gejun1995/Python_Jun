from PIL import Image, ImageChops
import os
import cv2
import time
import numpy as np

def open_image(image_folder_path, i):
    image_name = str(i) + ".tif"
    image_complete_path = image_folder_path + "\\" + image_name
    image = Image.open(os.path.join(image_complete_path))
    print(image_complete_path, image.format, image.size, image.mode)
    return image

def compare_images(image_pre, image_current,i):
    xoff_best = 0
    yoff_best = 0
    rotate_best = 0
    similary = 0

    for xoff in range(0,1):
        for yoff in range(0, 1):
            print("xoff is " + str(xoff) + "\tyoff is " + str(yoff))
            for rotate in np.arange(-45,45,2):
                print("rotate is " + str(rotate))
                # change image
                image_temp = image_current
                image_temp = ImageChops.offset(image_temp, xoff, yoff)
                try:
                    image_temp.rotate(rotate).save("temp.tif")
                    #time.sleep(0.1)
                except:
                    time.sleep(5)
                    image_temp.rotate(rotate).save("temp.tif")
                # read image for openCV
                image_pre_opencv = image_pre
                image_current_opencv = cv2.imread("temp.tif")
                # compare image
                sift = cv2.xfeatures2d_SIFT.create()
                kp1, des1 = sift.detectAndCompute(image_pre_opencv, None)
                kp2, des2 = sift.detectAndCompute(image_current_opencv, None)
                bf = cv2.BFMatcher(cv2.NORM_L2)
                matches = bf.knnMatch(des1, des2,k=2)
                good = [m for (m, n) in matches if m.distance < 0.7* n.distance]
                current_similary = len(good) / len(matches)
                print("Current good  number is: " + str(len(good)))
                print("Current matches number is: " + str(len(matches)))
                print("Current similarity is: %s" % similary)

                if current_similary > similary:
                    similary = current_similary
                    xoff_best = xoff
                    yoff_best = yoff
                    rotate_best = rotate
                    print("Fow now, the best align fit is:")
                    print("xoff_best is " + str(xoff_best))
                    print("yoff_best is " + str(yoff_best))
                    print("rotate_best is " + str(rotate_best))
                    print("Best similary is " + str(similary))
                    print("----------")
                    image_current = ImageChops.offset(image_current, xoff_best, yoff_best)
                    image_current.rotate(rotate_best).save("temp_best.tif")
    return xoff_best, yoff_best, rotate_best

def save_aligned_image(xoff_best, yoff_best, rotate_best, i, image_current):
    new_image_name = str(i) + ".tif"
    image_current = ImageChops.offset(image_current, xoff_best, yoff_best)
    image_current.rotate(rotate_best).save(new_image_name)

def process_image(image_folder_path, image_start_number, image_end_number, image_x_size, image_y_size):
    for i in range(image_start_number + 1, image_end_number):
        print("--------------------------------------------------------------------------------")
        print("Comparing the following two files......")
        image_pre = cv2.imread(str(i - 1) + ".tif")
        image_current = open_image(image_folder_path, i)
        xoff, yoff, rotate = compare_images(image_pre, image_current,i)
        save_aligned_image(xoff, yoff, rotate, i, image_current)
        print("The best file is saved.")
        print("There are %d more files to be aligned." % (image_end_number - i))
        print("\n")

if __name__ == "__main__":
        for j in range(0,1):
            image_folder_path = r"E:\OneDrive\Documents\Python_Jun\research\stem_section_align"
            image_start_number = 70
            image_end_number = 87
            image_x_size = 450
            image_y_size = 450
            process_image(image_folder_path, image_start_number, image_end_number, image_x_size, image_y_size)
