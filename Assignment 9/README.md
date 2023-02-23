## Assignment 9 with basic attention model, CIFAR dataset  

### Objectives  
Build the following network:

That takes a CIFAR10 image (32x32x3)  
Add 3 Convolutions to arrive at AxAx48 dimensions (e.g. 32x32x3 | 3x3x3x16 >> 3x3x16x32 >> 3x3x32x48)  
Apply GAP and get 1x1x48, call this X  
Create a block called ULTIMUS that:  
Creates 3 FC layers called K, Q and V such that:  
X*K = 48*48x8 > 8  
X*Q = 48*48x8 > 8   
X*V = 48*48x8 > 8   
then create AM = SoftMax(QTK)/(8^0.5) = 8*8 = 8  
then Z = V*AM = 8*8 > 8  
then another FC layer called Out that:  
Z*Out = 8*8x48 > 48  
Repeat this Ultimus block 4 times  
Then add final FC layer that converts 48 to 10 and sends it to the loss function.  
Model would look like this C>C>C>U>U>U>U>FFC>Loss  
Train the model for 24 epochs using the OCP that I wrote in class. Use ADAM as an optimizer. 

### Outcomes  

1. Basic Attention model  is loaded from models  
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
            Conv2d-1           [-1, 16, 16, 16]             448
       BatchNorm2d-2           [-1, 16, 16, 16]              32
           Dropout-3           [-1, 16, 16, 16]               0
            Conv2d-4             [-1, 32, 8, 8]           4,640
       BatchNorm2d-5             [-1, 32, 8, 8]              64
           Dropout-6             [-1, 32, 8, 8]               0
            Conv2d-7             [-1, 48, 4, 4]          13,872
       BatchNorm2d-8             [-1, 48, 4, 4]              96
           Dropout-9             [-1, 48, 4, 4]               0
        AvgPool2d-10             [-1, 48, 1, 1]               0
          ConvNet-11                   [-1, 48]               0
           Linear-12                    [-1, 8]             392
           Linear-13                    [-1, 8]             392
           Linear-14                    [-1, 8]             392
           Linear-15                   [-1, 48]             432
          Ultimus-16                   [-1, 48]               0
           Linear-17                    [-1, 8]             392
           Linear-18                    [-1, 8]             392
           Linear-19                    [-1, 8]             392
           Linear-20                   [-1, 48]             432
          Ultimus-21                   [-1, 48]               0
           Linear-22                    [-1, 8]             392
           Linear-23                    [-1, 8]             392
           Linear-24                    [-1, 8]             392
           Linear-25                   [-1, 48]             432
          Ultimus-26                   [-1, 48]               0
           Linear-27                    [-1, 8]             392
           Linear-28                    [-1, 8]             392
           Linear-29                    [-1, 8]             392
           Linear-30                   [-1, 48]             432
          Ultimus-31                   [-1, 48]               0
           Linear-32                   [-1, 10]             490
Total params: 26,074  
Trainable params: 26,074  
Non-trainable params: 0
Input size (MB): 0.01  
Forward/backward pass size (MB): 0.16  

2. CIFAR train and test data loaders are loaded from utils  
3. Sample images are viewed using imshow function from utils. RandomCrop, CoarseDropout(8*8) transformations from Albumentations are applied only for train datasets  
<img width="527" alt="image" src="https://user-images.githubusercontent.com/13360207/220422080-2f92d447-378d-43b5-be4f-fec3ec5b6b67.png">

4. One cycle policy --> Min Learning Rate - 0.001, Max Learning Rate = 0.01, Model is trained for 24 Epochs. Training and test losses/ accuracies as below  
 <img width="699" alt="image" src="https://user-images.githubusercontent.com/13360207/220813815-83292393-038a-4067-b857-ca821bcfbbf4.png">


 
5. Plot misclassified images  
<img width="527" alt="image" src="https://user-images.githubusercontent.com/13360207/220813841-d9abda76-bbf5-498e-8f18-f6c9efac3f05.png">






