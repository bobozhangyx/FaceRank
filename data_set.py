# coding=utf-8

import os
import csv
import numpy
import decimal
from PIL import Image
from decimal import Decimal


context=decimal.getcontext()# 获取decimal现在的上下文
context.rounding = decimal.ROUND_05UP


rankMap = {}
with open("data/pic_label.CSV") as f:
    reader = csv.reader(f)
    for line in reader:
        rank = int(round(float(line[1])*2, 0))
        rankMap[line[0]] = str(rank)
pic_list = os.listdir("data/Data_Collection/")

for line in pic_list:
    img = Image.open("data/Data_Collection/"+line)
    pic_id = line.split('-')[2].split('.')[0]
    f_name = pic_id+'-'+rankMap[pic_id]+'.jpg'
    img.resize((128, 128)).save(os.path.join("data/resize_image/", f_name), "JPEG")

