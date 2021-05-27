# # Image path, number of rows
# # and number of columns
# # should be provided as an arguments
# import cv2
# import sys
# import os
# import glob
# import fnmatch
# import re
# import numpy as np
# from PIL import Image
#
# image1, image2, image3, image4 = [], [], [], []
# path = '/home/adminp/Documents/NLP/patches/'
#
#
# def split_image(img):
#     nRows = 4
#     mCols = 4
#
#     # Dimensions of the image
#     sizeX = img.shape[1]
#     sizeY = img.shape[0]
#
#     # print(img.shape)
#
#
#     for i in range(0, nRows):
#         for j in range(0, mCols):
            # print((int(i*sizeY/nRows), int(i*sizeY/nRows) + int(sizeY/nRows), int(j*sizeX/mCols), int(j*sizeX/mCols) + int(sizeX/mCols)))
# # (0, 44, 0, 71)
# # (0, 44, 71, 142)
# # (0, 44, 142, 213)
# # (0, 44, 213, 284)
# # (44, 88, 0, 71)
# # (44, 88, 71, 142)
# # (44, 88, 142, 213)
# # (44, 88, 213, 284)
# # (88, 132, 0, 71)
# # (88, 132, 71, 142)
# # (88, 132, 142, 213)
# # (88, 132, 213, 284)
# # (132, 176, 0, 71)
# # (132, 176, 71, 142)
# # (132, 176, 142, 213)
# # (132, 176, 213, 284)
#             roi = img[int(i*sizeY/nRows):int(i*sizeY/nRows) + int(sizeY/nRows), int(j*sizeX/mCols):int(j*sizeX/mCols) + int(sizeX/mCols)]
#             # cv2.imshow('rois'+str(i)+str(j), roi)
#             cv2.imwrite('patches/patch_'+str(i)+str(j)+".jpg", roi)
#
#     cv2.waitKey()
#
#
# def combine():
#     image_list = []
#     for filename in glob.glob('/home/adminp/Documents/NLP/patches/*.jpg'): #assuming gif
#         image_list.append(filename)
#
#     # print('list : ', image_list)
#     for i in image_list:
#         name = os.path.basename(i)
#         if fnmatch.fnmatch(name, 'patch_0*.jpg'):
#             image1.append(os.path.join(path, i))
#             (image1.sort(key=lambda f: int(re.sub('\D', '', f))))
#         elif fnmatch.fnmatch(name, 'patch_1*.jpg'):
#             image2.append(os.path.join(path, i))
#             (image2.sort(key=lambda f: int(re.sub('\D', '', f))))
#         elif fnmatch.fnmatch(name, 'patch_2*.jpg'):
#             image3.append(i)
#             (image3.sort(key=lambda f: int(re.sub('\D', '', f))))
#         else:
#             image4.append(i)
#             (image4.sort(key=lambda f: int(re.sub('\D', '', f))))
#
#     Image1 = [Image.open(i) for i in image1]  # ['/home/adminp/Documents/NLP/patches/patch_00.jpg', '/home/adminp/Documents/NLP/patches/patch_01.jpg',
#               # '/home/adminp/Documents/NLP/patches/patch_02.jpg', '/home/adminp/Documents/NLP/patches/patch_03.jpg'])]
#     Image2 = [Image.open(i) for i in image2]  # (['/home/adminp/Documents/NLP/patches/patch_10.jpg', '/home/adminp/Documents/NLP/patches/patch_11.jpg',
#               # '/home/adminp/Documents/NLP/patches/patch_12.jpg', '/home/adminp/Documents/NLP/patches/patch_13.jpg'])]
#     Image3 = [Image.open(i) for i in image3]  # (['/home/adminp/Documents/NLP/patches/patch_20.jpg', '/home/adminp/Documents/NLP/patches/patch_21.jpg',
#               # '/home/adminp/Documents/NLP/patches/patch_22.jpg', '/home/adminp/Documents/NLP/patches/patch_23.jpg'])]
#     Image4 = [Image.open(i) for i in image4]  # (['/home/adminp/Documents/NLP/patches/patch_30.jpg', '/home/adminp/Documents/NLP/patches/patch_31.jpg',
#               # '/home/adminp/Documents/NLP/patches/patch_32.jpg', '/home/adminp/Documents/NLP/patches/patch_33.jpg'])]
#     #
#     # print('Image list : ', Image1)
#
#     min_shape = sorted([(np.sum(i.size), i.size) for i in Image1])[0][1]
#     img1_comb = np.hstack((np.asarray(i.resize(min_shape))for i in Image1))
#     img2_comb = np.hstack((np.asarray(i.resize(min_shape))for i in Image2))
#     img3_comb = np.hstack((np.asarray(i.resize(min_shape))for i in Image3))
#     img4_comb = np.hstack((np.asarray(i.resize(min_shape))for i in Image4))
#     #
#     # # images = [image1, image2, image3]
#     #
#     imgs_comb = np.vstack((img1_comb, img2_comb, img3_comb, img4_comb))
#     imgs_comb = Image.fromarray(imgs_comb)
#     imgs_comb.save('test.jpg')
#     imgs_comb.show()
#
# # new_im = Image.new('RGB', (285, 177))
# #
# # x_offset = 0
# # for im in images:
# #     new_im.paste(im, (x_offset, 0))
# #     x_offset += im.size[0]
# #
# # new_im.save('test.jpg')
#
#
# if __name__ == '__main__':
#     img = cv2.imread('/home/adminp/Documents/NLP/sample.jpeg')
#     split_image(img)
#     combine()
# """
# Read image then cut break it in pieces and then joint it
# """
# import cv2
# import numpy as np
# import os
#
# ### User Input
# num_cols = 4
# num_rows = 4
#
# if not os.path.exists('patches'):
#     os.makedir("patches")
#
# # Read image
# img_path = '/home/adminp/Documents/NLP/sample.jpeg'
# img = cv2.imread(img_path)
#
# # Creat dummy image
# black_img = np.zeros_like(img, dtype="uint8")  ## for add pice of original img
#
# img_hight = img.shape[0]
# img_width = img.shape[1]
#
# # Create rows and columns indexing
# num_rows_space = np.linspace(0, img_hight, num_rows + 1, dtype="int")
# num_cols_space = np.linspace(0, img_width, num_cols + 1, dtype="int")
# # print("num_rows_space = ", num_rows_space)
# # print("num_cols_space = ", num_cols_space)
#
# # Cut image roa and column wise and then joint it
# for row in range(0, num_rows):
#     for col in range(0, num_cols):
#         # get piece of original img
#         img_roi = img[num_rows_space[row]:num_rows_space[row + 1], num_cols_space[col]:num_cols_space[col + 1]]
#
#         ## Add piece of image in black img
#         black_img[num_rows_space[row]:num_rows_space[row + 1], num_cols_space[col]:num_cols_space[col + 1]] = img_roi
#
#         # save piece of image as image in .jpe format
#         cv2.imwrite("patches\cut_row_{}col{}.jpg".format(row, col), img_roi)
#
#         cv2.imshow("Original Image and cut_joint image", np.hstack((img, black_img)))
#         cv2.waitKey(1000)
#
# cv2.destroyAllWindows()
