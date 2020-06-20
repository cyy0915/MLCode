# Test Code with UNet++

### Introduction

This part of the repository is about the code we used to test UNet++. All codes other than [pytorch-nested-unet-master](https://github.com/cyy0915/MLCode/tree/master/UNet%2B%2B/pytorch-nested-unet-master) are written by us, while the former one is copied from [this repository](https://github.com/4uiiurz1/pytorch-nested-unet). Due to the fact that this is an aggregated project, you must note the position from which any file should be executed. For this sub-repo, all three .py files must be executed here; while other codes inside [pytorch-nested-unet-master](https://github.com/cyy0915/MLCode/tree/master/UNet%2B%2B/pytorch-nested-unet-master) should be executed inside that directory.

### How to use the code

#### Data enhancement

Run train_data_enforce.py to enforce the data resided inside [pytorch-nested-unet-master](https://github.com/cyy0915/MLCode/tree/master/UNet%2B%2B/pytorch-nested-unet-master). Specify the directory inside the file to change the directory of the data. Note that the data must follow the format specified by [pytorch-nested-unet-master](https://github.com/cyy0915/MLCode/tree/master/UNet%2B%2B/pytorch-nested-unet-master). Run this line once before training to enforce the data:

> python train_data_enfoece.py

#### Training

Training the models with different settings require different commands. All commands here must be executed in the [pytorch-nested-unet-master](https://github.com/cyy0915/MLCode/tree/master/UNet%2B%2B/pytorch-nested-unet-master) directory. If you want to train the model without deep supervision, run in the directory the following:

> python train.py --dataset isbi --arch NestedUNet --input_w 512 --input_h 512 --batch_size 1

Note that the batch_size specification are just limited by our GPU capacity, so you could change that parameter according to your hardware capacity.

Or, if you want to train the model with deep supervision enabled, run the following line:

> python train.py --dataset isbi --arch NestedUNet --input_w 512 --input_h 512 --batch_size 1 --deep_supervision True --name useDeepSupervision

#### Official test the accuracy on test-set

By the way the official implementation gave, run in the [pytorch-nested-unet-master](https://github.com/cyy0915/MLCode/tree/master/UNet%2B%2B/pytorch-nested-unet-master) directory:

> python val.py --name isbi_NestedUNet_woDS

And:

> python val.py --name useDeepSupervision

They will output the accuracy of the data using the official standard.

#### Course-specific test of accuracy on test-set

By the way given by our TA, run in the current directory:

> python acc.py

Note that you must run both training processes in order to see the full output of this file (because it contains test for both).
