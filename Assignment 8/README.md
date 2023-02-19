## Assignment 8 with custom resnet, CIFAR dataset, Cyclical training with One Cycle Policy and GradCAM plotting  

### Objectives  
Write a custom ResNet architecture for CIFAR10 that has the below architecture
PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
Layer1 - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k] --> R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
Add(X, R1)
Layer 2 - Conv 3x3 [256k] --> MaxPooling2D --> BN --> ReLU
Layer 3 - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k] --> R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
Add(X, R2)
MaxPooling with Kernel Size 4
FC Layer 
SoftMax
Uses One Cycle Policy such that:
Total Epochs = 24, Max at Epoch = 5, LRMIN = FIND, LRMAX = FIND, NO Annihilation
Uses this transform -RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
Batch size = 512
Target Accuracy: 90% (93.8% quadruple scores). 
NO score if your code is not modular. Your collab must be importing your GitHub package, and then just running the model. I should be able to find the custom_resnet.py model in your GitHub repo that you'd be training. 

### Outcomes  

1. Custom ResNet is loaded from models  
2. CIFAR train and test data loaders are loaded from utils  
3. Sample images are viewed using imshow function from utils. RandomCrop, CoarseDropout(8*8) transformations from Albumentations are applied only for train datasets  

<img width="515" alt="image" src="https://user-images.githubusercontent.com/13360207/219948845-adee96c9-1a2f-493b-9f03-9d9fec193355.png">

4. Find learning rate using one cycle policy --> Min Learning Rate - 0.001, Max Learning Rate = 0.01

<img width="299" alt="image" src="https://user-images.githubusercontent.com/13360207/219948908-8686807d-770b-46d0-b7ea-f264b702e89e.png">

5. Model is trained for 24 Epochs. Training and test losses/ accuracies as below  
 <img width="728" alt="image" src="https://user-images.githubusercontent.com/13360207/219948946-ddf4c8d7-a23d-43ff-8cb0-182e1e27a618.png">
 
5. Plot misclassified images  
<img width="526" alt="image" src="https://user-images.githubusercontent.com/13360207/219948966-528e2cb9-b4b2-435f-b3ee-6040567674fd.png">


6. GradCAM plot for images  
<img width="541" alt="image" src="https://user-images.githubusercontent.com/13360207/219948978-5c5e5eda-81e6-4fa0-8a68-dfccc77e3b40.png">



