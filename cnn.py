import numpy as np

def conv2d(image,kernel):
    # 获取图像和卷积核的尺寸
    image_height,image_width = image.shape
    kernel_height,kernel_width = kernel.shape

    # 计算输出的尺寸
    output_height = 

