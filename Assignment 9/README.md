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
2. CIFAR train and test data loaders are loaded from utils  
3. Sample images are viewed using imshow function from utils. RandomCrop, CoarseDropout(8*8) transformations from Albumentations are applied only for train datasets  

<img width="515" alt="image" src="https://user-images.githubusercontent.com/13360207/219948845-adee96c9-1a2f-493b-9f03-9d9fec193355.png">

4. One cycle policy --> Min Learning Rate - 0.001, Max Learning Rate = 0.01

<img width="299" alt="image" src="https://user-images.githubusercontent.com/13360207/219948908-8686807d-770b-46d0-b7ea-f264b702e89e.png">

5. Model is trained for 24 Epochs. Training and test losses/ accuracies as below  
 <img width="728" alt="image" src="https://user-images.githubusercontent.com/13360207/219948946-ddf4c8d7-a23d-43ff-8cb0-182e1e27a618.png">
 
5. Plot misclassified images  
<img width="526" alt="image" src="https://user-images.githubusercontent.com/13360207/219948966-528e2cb9-b4b2-435f-b3ee-6040567674fd.png">




