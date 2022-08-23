import fitz

# 安装PyMuPDF 1.18.14版本
# pip install PyMuPDF==1.18.14
# 将PDF转化为图片
# pdfPath pdf文件的路径
# imgPath 图像要保存的文件夹
# zoom_x x方向的缩放系数
# zoom_y y方向的缩放系数
# rotation_angle 旋转角度

def pdf_image(pdfPath, imgPath, start_page, end_page, zoom_x, zoom_y, rotation_angle):
    # 打开pdf文件
    pdf = fitz.open(pdfPath)
    # print(dir(pdf))
    # 逐页读取pdf
    start = start_page or 0
    end = end_page or pdf.pageCount
    for pg in range(start, min([end, pdf.pageCount])):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.getPixmap(matrix = trans, alpha = False)
        # 开始写图像
        pm.writePNG(imgPath+str(pg)+".png")
    pdf.close()

pdfPath = '/Users/yisha/Desktop/培训项目计划书.pdf'
imgPath = 'py4office/py-tutorial/result'
pdf_image(pdfPath, imgPath, 10, 12, 10, 10, 0)
