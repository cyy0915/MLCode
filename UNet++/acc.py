# mind that this file has to be run in the same directory.

from PIL import Image
import numpy as np
import os

# this function was slightly modified from the example from TA.
# the only modification was that it now supports soft output.
def compute_acc(path_img, path_label):
    img = Image.open(path_img)
    # img.show()
    label = Image.open(path_label)
    img = np.array(img)
    # print(img[250])
    label = np.array(label)
    # print(label[250])
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            # this line forces 0-255 value into 0 or 255 binary value
            tag = int(img[i][j]/128)*255
            if(tag == label[i][j]):
                if(tag == 0):
                    TN = TN + 1
                else:
                    TP = TP + 1
            else:
                if(tag == 0):
                    FP = FP + 1
                else:
                    FN = FN + 1
    return TN, TP, FP, FN


if __name__ == "__main__":
    acc = 0
    all_TN = 0
    all_TP = 0
    all_FP = 0
    all_FN = 0

    # different choice here denotes different data to test.
    # the first is trained without deep supervision,
    # the second is all the layers of the network with deep supervision

    path_img = "pytorch-nested-unet-master/outputs/isbi_NestedUNet_woDS/0"
    path_img_sep = "pytorch-nested-unet-master/outputs/useDeepSupervision_separated/0"

    path_label = "pytorch-nested-unet-master/inputs/isbi_test/masks/0"
    lsimg = os.listdir(path_img)
    print(lsimg)

    # test without deep supervision
    for name in lsimg:
        img_file = path_img + '/' + name
        print(img_file)
        label_file = path_label + '/' + name
        TN, TP, FP, FN = compute_acc(img_file, label_file)
        all_TN = all_TN + TN
        all_TP = all_TP + TP
        all_FP = all_FP + FP
        all_FN = all_FN + FN
    acc = (all_TP + all_TN) / (all_TP + all_FN + all_FP + all_TN)
    print(all_TP)
    print(all_FP)
    print(all_FN)
    print(all_TN)

    print(acc)

    # test deep supervision
    print("testing separated")
    lsimg = os.listdir(path_img_sep)
    print(lsimg)

    for i in range(4):
        print("calculating layer No %d" % i)
        for j in range(5):
            img_file = path_img_sep + '/' + str(j) + '_' + str(i) + '.png'
            print(img_file)
            label_file = path_label + '/' + str(j) + '.png'
            TN, TP, FP, FN = compute_acc(img_file, label_file)
            all_TN = all_TN + TN
            all_TP = all_TP + TP
            all_FP = all_FP + FP
            all_FN = all_FN + FN
        acc = (all_TP + all_TN) / (all_TP + all_FN + all_FP + all_TN)

        print(all_TP)
        print(all_FP)
        print(all_FN)
        print(all_TN)

        print(acc)
