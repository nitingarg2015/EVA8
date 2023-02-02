## Objective  
1. Fix the network  
2. Change the code such that it uses GPU  
3. Change the architecture to C1C2C3C40 (No MaxPooling, but 3 3x3 layers with stride of 2 instead) (If you can figure out how to use Dilated kernels here instead of MP or strided convolution, then 200pts extra!)  
4. Total RF must be more than 44  
5. One of the layers must use Depthwise Separable Convolution  
6. One of the layers must use Dilated Convolution  
7. Use GAP (compulsory):- add FC after GAP to target #of classes (optional)  
8. Use albumentation library and apply: horizontal flip, shiftScaleRotate, coarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of your dataset), mask_fill_value = None)  
9. Achieve 85% accuracy, as many epochs as you want. Total Params to be less than 200k.  

### Function Files - model.py  
Model.py file has been created that does the following  
1. Defines Net Class for training CNN model  
2. During initialization, define optional droput value  
3. 12 Convolutional layers
4. **One convolutional layer with Dilation (Conv2d-19)**
5. **One Depthwise convolutional layer (Conv2d-28 and Conv2d-29)**  
6. Batch Normalization and Dropout layer after each convolutional layer but for depthwise seperable layer
7. GAP layer - AvgPool2d-30
8. FC Layer - Linear-31
9. **Trainable parameters: 188,842**  
10. **Receptive Field: 63**  

<img width="286" alt="image" src="https://user-images.githubusercontent.com/13360207/216124978-38b96ff5-44c6-4ef8-b88b-d731eba69922.png">
  
## assignment-6-v1.ipynb - Main File  

### View training Data:  
<img width="398" alt="image" src="https://user-images.githubusercontent.com/13360207/216230688-fade815f-a1c0-45b2-aced-1269a3199b29.png">

### Training parameters  
Learning Rate: 0.1, Scheduled Step 0.01 after 35th Epoch  

Number of Epochs: 45  
Epoch where >85% test accuracy achieved: 30  
Momentum = 0.9  
Cross Entropy Loss, SGD Optimizer  
**Training Accuracy: 79.08%**  
**Test Accuracy: 88.86%**  

## Mis Classified Images  
<img width="395" alt="image" src="https://user-images.githubusercontent.com/13360207/216230957-8bc2a085-7417-47fb-8ded-d06a79610e10.png">

## Fractions Mis Classified by Class  
<img width="487" alt="image" src="https://user-images.githubusercontent.com/13360207/216230982-7180af81-2a46-4038-a016-047a23974d7a.png">

<img width="230" alt="image" src="https://user-images.githubusercontent.com/13360207/216231007-fc567e4c-749c-4ac1-a837-96f1577cf410.png">

## Function Files
### Function Files - loadcifar.py
Loads CIFAR training and test datasets, and returns test_loader and train_loader  

### Function Files - testfns.py  
Accepts trained model, device and data_loader as inputs and returns test accuracy  

### Function Files - misclassified.py  
Two functions defined: 1) get_miss_classified, 2) getFractionsMissed  

1) get_miss_classified - takes model, device, images, labels as inputs and returns lists of misclassified images, their targets and labels. This information is used to view misclassified images  

2) getFractionsMissed - takes model, device, test_loader as inputs and returns a dictionary of fractions missed predictions by class  

