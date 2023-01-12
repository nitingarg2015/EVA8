# Assignment 3b

Objectives of the assignment is to rewrite code such that:
1. 99.4% validation accuracy
2. Less than 20k Parameters
3. You can use anything from above you want. 
4. Less than 20 Epochs
5. Have used BN, Dropout, a Fully connected layer, have used GAP. 
6. To learn how to add different things we covered in this session

## About the Network
1. 8 Convolutional layers and One Fully Connected Layer
2. Batch Normalization and Dropout layer after every convolutional layer
3. ReLU activation function used
5. Three MaxPool2D layers
4. GAP layer before Fully connected layer
5. Expand & Squeeze used in first four convolutional layers, # channels increased & decreased in range of 8 to 32
6. Details of each layer with output shape & paramters as below. 15,938 parameters used in all
7. Log Softmax used as last layer activation function with NLL Loss
8. Network reached 99.4% test accuracy in the 9th epoch, and reported accuracy greater than 99.4% in last four epochs

<img width="290" alt="image" src="https://user-images.githubusercontent.com/13360207/212101979-e29b3122-5665-47f4-9b89-58f9acede661.png">  

Training Logs

<img width="402" alt="image" src="https://user-images.githubusercontent.com/13360207/212106327-429f253b-a406-47eb-a34f-aa6658734c6e.png">

<img width="404" alt="image" src="https://user-images.githubusercontent.com/13360207/212106499-fb15156c-13e2-4a76-a5db-9f37b4122297.png">


