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

## Function Files
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
  
### Function Files - loadcifar.py
Loads CIFAR training and test datasets, and returns test_loader and train_loader  

### Function Files - testfns.py  
Accepts trained model, device and data_loader as inputs and returns test accuracy  

### Function Files - misclassified.py  
Two functions defined: 1) get_miss_classified, 2) getFractionsMissed  

1) get_miss_classified - takes model, device, images, labels as inputs and returns lists of misclassified images, their targets and labels. This information is used to view misclassified images  

2) getFractionsMissed - takes model, device, test_loader as inputs and returns a dictionary of fractions missed predictions by class  

## assignment-6-v1.ipynb - Main File  

### View training Data:  
<img width="393" alt="image" src="https://user-images.githubusercontent.com/13360207/216126501-35ac538f-1afe-471d-a255-d3eaa2f354c3.png">

### Training parameters  
Learning Rate: 0.1
Number of Epochs: 45  
Momentum = 0.9  
Cross Entropy Loss, SGD Optimizer  
**Training Accuracy: 79.08%**  
**Test Accuracy: 87.27%**  

## Mis Classified Images  
<img width="392" alt="image" src="https://user-images.githubusercontent.com/13360207/216127242-6bb6b73f-e695-41e8-b31f-ff043ac50bd1.png">

## Fractions Mis Classified by Class  
<img width="478" alt="image" src="https://user-images.githubusercontent.com/13360207/216127362-4cd0a458-5032-46c7-bab3-475e466f6710.png">

<img width="228" alt="image" src="https://user-images.githubusercontent.com/13360207/216127412-dc2769ed-f7a3-4ff2-8208-16a7df7f711b.png">



