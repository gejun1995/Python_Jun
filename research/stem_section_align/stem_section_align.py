from PIL import Image, ImageChops
import os
import torch


def open_image(image_folder_path, i):
    image_name = str(i) + ".tif"
    image_complete_path = image_folder_path + "\\" + image_name
    image = Image.open(os.path.join(image_complete_path))
    print(image_complete_path, image.format, image.size, image.mode)
    return image

class DHash(object):
    @staticmethod
    def calculate_hash(image):
        """
        计算图片的dHash值
        :param image: PIL.Image
        :return: dHash值,string类型
        """
        difference = DHash.__difference(image)
        # 转化为16进制(每个差值为一个bit,每8bit转为一个16进制)
        decimal_value = 0
        hash_string = ""
        for index, value in enumerate(difference):
            if value:  # value为0, 不用计算, 程序优化
                decimal_value += value * (2 ** (index % 8))
            if index % 8 == 7:  # 每8位的结束
                hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))  # 不足2位以0填充。0xf=>0x0f
                decimal_value = 0
        return hash_string

    @staticmethod
    def hamming_distance(first, second):
        """
        计算两张图片的汉明距离(基于dHash算法)
        :param first: Image或者dHash值(str)
        :param second: Image或者dHash值(str)
        :return: hamming distance. 值越大,说明两张图片差别越大,反之,则说明越相似
        """
        # A. dHash值计算汉明距离
        if isinstance(first, str):
            return DHash.__hamming_distance_with_hash(first, second)

        # B. image计算汉明距离
        hamming_distance = 0
        image1_difference = DHash.__difference(first)
        image2_difference = DHash.__difference(second)
        for index, img1_pix in enumerate(image1_difference):
            img2_pix = image2_difference[index]
            if img1_pix != img2_pix:
                hamming_distance += 1
        return hamming_distance

    @staticmethod
    def __difference(image):
        """
        *Private method*
        计算image的像素差值
        :param image: PIL.Image
        :return: 差值数组。0、1组成
        """
        resize_width = 9
        resize_height = 8
        # 1. resize to (9,8)
        smaller_image = image.resize((resize_width, resize_height))
        # 2. 灰度化 Grayscale
        grayscale_image = smaller_image.convert("L")
        # 3. 比较相邻像素
        pixels = list(grayscale_image.getdata())
        difference = []
        for row in range(resize_height):
            row_start_index = row * resize_width
            for col in range(resize_width - 1):
                left_pixel_index = row_start_index + col
                difference.append(pixels[left_pixel_index] > pixels[left_pixel_index + 1])
        return difference

    @staticmethod
    def __hamming_distance_with_hash(dhash1, dhash2):
        """
        *Private method*
        根据dHash值计算hamming distance
        :param dhash1: str
        :param dhash2: str
        :return: 汉明距离(int)
        """
        difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
        return bin(difference).count("1")

def compare_images(image_pre, image_current):
    xoff = 0
    yoff = 0
    rotate = 0
    pass
    for xoff in range(-image_x_size, image_x_size):
        for yoff in range(-image_y_size, image_x_size):
            for rotate in range(0, 360):
                image_temp = image_current
                #得到比较结果
                current_diff =
                lowest_diff = 0
                if lowest_diff > current_diff:
                    lowest_diff = current_diff
                    xoff_best = xoff
                    yoff_best = yoff
                    rotate_best = rotate
                    print("xoff_best is "+ str(xoff_best))
                    print("yoff_best is "+ str(yoff_best))
                    print("rotate_best is "+ str(rotate_best))
    return xoff_best, yoff_best, rotate_best


def save_aligned_image(xoff_best, yoff_best, rotate_best, i, image_current):
    new_image_name = "new" + str(i + 1) + ".tif"
    image_current = ImageChops.offset(image_current, xoff_best, yoff_best)
    image_current.rotate(rotate_best).save(new_image_name)


def process_image(image_folder_path, image_start_number, image_end_number, image_x_size, image_y_size):
    for i in range(image_start_number, image_end_number):
        image_pre = open_image(image_folder_path, i)
        image_current = open_image(image_folder_path, i + 1)
        xoff, yoff, rotate = compare_images(image_pre, image_current,  image_x_size, image_x_size)
        save_aligned_image(xoff, yoff, rotate, i, image_current)


if __name__ == "__main__":
    image_folder_path = r"E:\OneDrive\Temp\Subject\Nano-3D"
    image_start_number = 70
    image_end_number = 87
    image_x_size = 450
    image_y_size = 450
    process_image(image_folder_path, image_start_number, image_end_number, image_x_size, image_x_size)






