

import os
import shutil
import pandas as pd
from PIL import Image
# 读取Excel表格
df = pd.read_excel('train.xlsx')

for index, row in df.iterrows():
    # folder =str(row[0])
    # filename = str(row[1])
    folder = str(row.iloc[0])
    filename = str(row.iloc[1])


    def save_file(filename, folder=None):  # str2 str1
        # 获取当前工作目录
        current_folder = os.getcwd()

        if folder is None:
            # 如果未指定文件夹，则使用当前工作目录
            folder = current_folder
            # folder = os.path.join(current_folder, 'images')
        else:
            # 如果指定了文件夹，则将文件夹路径与当前工作目录拼接
            folder = os.path.join(current_folder, folder)

        # 确保目标文件夹存在，如果不存在则创建
        os.makedirs(folder, exist_ok=True)

        # 拼接完整的文件路径
        file_path = os.path.join(folder, filename)
        img_folder  = 'C:/Users/Kelun/Desktop/crops/AgriculturalDisease_trainingset/images'
        img_path =os.path.join(img_folder,filename)
        img =Image.open(img_path)
        img.save(file_path)
        # 进行文件保存操作，这里使用一个示例，将文件内容写入文件
        # with open(file_path, 'w') as file:
        #
        #     pass
            # file.write("This is a test file.")

        # print(f"文件已保存至：{file_path}")

    # 示例用法
    save_file(filename, folder)  # 存储到指定文件夹
