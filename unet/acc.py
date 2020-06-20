from PIL import Image
import cv2
import numpy as np
import os

def compute_acc(path_img, path_label,thre:int):
    img = Image.open(path_img)
    #img.show()
    label = Image.open(path_label)
    img = np.array(img)
    _,img = cv2.threshold(img,thre,255,cv2.THRESH_BINARY)
    # img = cv2.resize(img,(512,512))
    #print(img[250])
    label = np.array(label)
    # label = cv2.resize(label,(256,256),interpolation=cv2.INTER_AREA)
    # _,label = cv2.threshold(label,thre,255,cv2.THRESH_BINARY)
    #print(label[250])
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    h, w = img.shape
    # print(h,w)
    # print(label.shape)
    for i in range(h):
        for j in range(w):
            if(img[i][j] == label[i][j]):
                if(label[i][j] == 0):
                    TN = TN + 1
                else:
                    TP = TP + 1
            else:
                if(label[i][j] == 0):
                    FP = FP + 1
                else:
                    FN = FN + 1
    return TN, TP, FP, FN


# log=[]
# for thre in range(255):
#     acc = 0
#     all_TN = 0
#     all_TP = 0
#     all_FP = 0
#     all_FN = 0
#     for name in os.listdir("dataset/new_test_set/test_label"):
#         name = name[0]
#         img_file = os.path.join("dataset/new_test_set/predict_label/%s_predict.png" % name)
#         label_file = os.path.join("dataset/new_test_set/test_label/%s.png" % name)
#         TN, TP, FP, FN = compute_acc(img_file, label_file,thre)
#         all_TN = all_TN + TN
#         all_TP = all_TP + TP
#         all_FP = all_FP + FP
#         all_FN = all_FN + FN
#     acc = (all_TP + all_TN)/ (all_TP + all_FN + all_FP + all_TN)
#     arr=np.array([all_TP,all_FP,all_FN,all_TN,acc])
#     log.append(arr)

acc = 0
all_TN = 0
all_TP = 0
all_FP = 0
all_FN = 0
for name in os.listdir("dataset/new_test_set/test_label"):
    name = name[0]
    img_file = os.path.join("dataset/new_test_set/predict_label_1/%s_predict.png" % name)
    label_file = os.path.join("dataset/new_test_set/test_label/%s.png" % name)
    TN, TP, FP, FN = compute_acc(img_file, label_file,87)
    all_TN = all_TN + TN
    all_TP = all_TP + TP
    all_FP = all_FP + FP
    all_FN = all_FN + FN
acc = (all_TP + all_TN)/ (all_TP + all_FN + all_FP + all_TN)
print(all_TP)
print(all_FP)
print(all_FN)
print(all_TN)

print(acc)
# np.savetxt("threshold_select.txt",log)









