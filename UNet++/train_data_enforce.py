# mind that this file has to be run in the same directory.

from PIL import Image
import os
from glob import glob


# this function was specially used for enforcing the data of UNet++, with rotating and flipping.
# the input route is arbitrary, but image names have to be formatted like '1.png'.
def enforceFromRoute(route, num, show=False):
    # find all picture name
    img_ids = list(range(num))
    img_ids = [str(i) for i in img_ids]

    if show:
        print(img_ids)

    for i in range(num):
        im = Image.open(route + img_ids[i] + '.png')
        if show:
            im.show()
        ############################ rotate ##############################
        # rotate 90
        im_rotate = im.rotate(90)
        if show:
            im_rotate.show()
        im_rotate.save(route + str(num + i) + '.png')
        # rotate 180
        im_rotate = im.rotate(180)
        if show:
            im_rotate.show()
        im_rotate.save(route + str(2*num + i) + '.png')
        # rotate 270
        im_rotate = im.rotate(270)
        if show:
            im_rotate.show()
        im_rotate.save(route + str(3*num + i) + '.png')
        ############################ transpose ##############################
        # l-r flip
        im_transpose = im.transpose(Image.FLIP_LEFT_RIGHT)
        if show:
            im_transpose.show()
        im_transpose.save(route + str(4*num + i) + '.png')

        # u-d flip
        im_transpose = im.transpose(Image.FLIP_TOP_BOTTOM)
        if show:
            im_transpose.show()
        im_transpose.save(route + str(5*num + i) + '.png')


if __name__ == "__main__":
    # this file was executed before training to enforce the data, in order to increase the network capacity.
    # enforce both the data and the label
    enforceFromRoute('pytorch-nested-unet-master/inputs/isbi/images/', num=25, show=False)
    enforceFromRoute('pytorch-nested-unet-master/inputs/isbi/masks/0/', num=25, show=False)