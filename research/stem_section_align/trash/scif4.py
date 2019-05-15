#!/usr/bin/python

import glob
import os
import sys

from PIL import Image
from functools import reduce

# EXTS = 'jpg', 'jpeg', 'JPG', 'JPEG', 'gif', 'GIF', 'png', 'PNG'
#注意：在进行图像格式查找时'JPG'与'jpg'查找到的结果相同，故只使用其中一种格
#式
EXTS = 'jpg', 'jpeg', 'gif', 'png'

def avhash(im):
    if not isinstance(im, Image.Image):
        im = Image.open(im)
    im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
    # print("im.getdata:" + str(im.getdata))
    avg = reduce(lambda x, y: x + y, im.getdata()) / 64.
    return reduce(lambda x, y_z : x | y_z[1] << y_z[0], enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())), 0)

def hamming(h1, h2):
    h, d = 0, h1 ^ h2
    while d:
        h += 1
        d &= d - 1
    return h

if __name__ == '__main__':
    print("图片配准格式：'jpg', 'jpeg', 'JPG', 'JPEG', 'gif', 'GIF', 'png', 'PNG'")
    file_object = open('C:/Users/SHQ/Desktop/CheckResult.txt', 'w')
    im = input("请输入基准图片IMG_1： ")
    wd = input("请输入配准图片文件夹目录： ")
    # if im is None or len(im) == 0:
    #     print("基准图片为空")
    # if wd is None or len(wd) == 0:
    #     print("配准图片为空")
    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print ("Usage: %s image.jpg [dir]" % sys.argv[0])
    else:
        im, wd = sys.argv[1], '.' if len(sys.argv) < 3 else sys.argv[2]
        h = avhash(im)
        #改变当前工作目录到指定的路径
        os.chdir(wd)
        images = []
        for ext in EXTS:
            print("ext:" + str(ext))
            print("glob.glob('*.%s' % ext):" + str(glob.glob('*.%s' % ext)))
            images.extend(glob.glob('*.%s' % ext))

        seq = []
        print(len(images))
        print("images:" + str(images))
        prog = int(len(images) > 50 and sys.stdout.isatty())
        for f in images:
            seq.append((f, hamming(avhash(f), h)))
            # print(prog)
            #若图片对比数量多于50，则以百分比形式显示对比进度
            if prog:
                perc = 100. * prog / len(images)
                x = int(2 * perc / 5)
                print ('\rCalculating... [' + '#' * x + ' ' * (40 - x) + ']',)
                print ('%.2f%%' % perc, '(%d/%d)' % (prog, len(images)))
                sys.stdout.flush()
                prog += 1

        if prog: print
        print("seq:" + str(seq))
        for f, ham in sorted(seq, key=lambda i: i[1]):
            print ("%d\t%s" % (ham, f))
            file_object.write("%d\t%s\n" % (ham, f))
    file_object.close()