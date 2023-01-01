
### PyTorch 101 Assignment

This is a neural network which 

1. takes 2 inputs:

	1. an image from the MNIST dataset **(say 5)**, and
	2. a random number between 0 and 9, **(say 7)**

2. and gives two outputs:
	1. the "number" that was represented by the MNIST image **(predict 5)&& and
	2. the "sum" of this number with the random number and the input image to the network **(predict 5+7 = 12)


ComboDataset dataset class is first created. This class combines the input image data (image and its label) with a randomly generated integer from 0 to 9. It returns four items as part of its output: 
1. Image as a tensor
2. Randomly generated integer as a 10 class one hot vector
3. Training label for the Image as an integer
4. Sum of Randomly generated integer and the training label as an iteger

Dataloader class is then used to generate train and test batches of given size  

Neural Network is then built using convolutional and linear neural networks as follows  

1. Six Convolutional layers are used that incrementally increase the receptive field from 3*3 to 32*32 for input image size of 28*28 in conv6 convolutional layer  
2. Output of conv6 convolutional layer is of size 10*3*3. This is fed into a linear layer that outputs 10 neurons, one each of the numbers from 0 to 1
3. Above output (batch_size*10) is transformed using softmax function and is concatenated with one hot vector random number input (batch_size*10) to form a tensor of size batch_size*20
4. This tensor is then passed through two linear neural network layers to generate an output on 19 neurons (representing sum from 0 to 18)
5. Relu activation function is used for each of the convolutional
6. No activation functio is used linear layers for summation as the transformation is linear represting sum of two numbers
7. Feed forward network returns two arrays post log_softmax transformation, one each for output for image prediction and sum prediction

Stochastic gradient descent with learning rate of 0.01 and momentum of 0.9 is used to train the network. Network is trained for 10 epochs  

Training and test functions are defined with the following attributes:  
1. The negative log likelihood loss. It is useful to train a classification problem with C classes  
2. Loss is calculated seperately for image classification and sum prediction
3. Both the losses are added to compute cumulative loss
4. Considering that loss for image classification is much lower compated to summation, a factor of 1.2 is used to adjust the losses prior to addition
5. Cumulative loss is used for back propagation through the batches  

Results are evaluated using accuracy metrics  
1. Accuracy is defined as ratio of number of correct predictions and total number of predictions  
2. Accuracy is evaluated seperately for image prediction and sum prediction  

Following outcomes are achieved post training for 10 epochs with learning rate of 0.01 at momentum of 0.9  on the test data
1. Image prediction loss 0.00182  
2. Image prediction accuracy 99%  
3. Sum prediction loss 0.7002  
4. Sum prediction accuracy 96%
