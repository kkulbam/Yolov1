import numpy as np

def conv2d(image,kernel):
    
    # 获取图像和卷积核的尺寸
    
    image_height,image_width = image.shape
    kernel_height,kernel_width = kernel.shape

    # 计算输出的尺寸
    
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    # 初始化输出矩阵
    
    output = np.zeros((output_height,output_width))

    # 实行卷积操作
    for i in range(output_height):
        for j in range(output_width):

    # 提取图像的一个区域 和卷积核及逆行元素级乘法并求和
 
            region = image[i:i + kernel_height,j:j + kernel_width]           
            output[i,j] = np.sum(region * kernel)
    return output

# 输入图像和卷积核
image = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],

])

kernel = np.array([
    [0,1,0],
    [1,-4,1],
    [0,1,0],
])

# 执行卷积操作

output = conv2d(image,kernel)

print("卷积结果：/n",output)