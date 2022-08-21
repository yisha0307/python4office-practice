import os
import pandas as pd
import numpy as np
import sys
sys.path.append('/Users/yisha/Documents/python4office-practice/py4office/py-tutorial')
from py_image import read_img

dir_path = '/Users/yisha/Desktop/2022年一季度上海市级医院综合绩效简报'
files = os.listdir(dir_path)
ss = os.path.splitext(dir_path+'/'+files[0])

# print(os.path.splitunc(dir_path+'/'+files[0]))

out_path = 'py4office/py-tutorial/result/result2.xlsx'

def isimg(pp):
    ss = os.path.splitext(pp)
    suf = ss[1]
    img_list = ['.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff']
    try:
        a = img_list.index(suf)
    except ValueError:
        return False
    else:
        return True


with pd.ExcelWriter(out_path) as writer:
    for file in files:
        path = dir_path + '/' + file
        if isimg(path):
            result = read_img(dir_path + '/' + file)
            df = result[0]
            title = result[1][-15:]
            df.to_excel(writer, sheet_name=title)
