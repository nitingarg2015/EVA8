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
6. Details of each layer with output shape & paramters as below. **15,938 parameters used in all**
7. Log Softmax used as last layer activation function with NLL Loss
8. Network reached 99.4% test accuracy in the 9th epoch, and reported accuracy greater than 99.4% in last four epochs

<img width="290" alt="image" src="https://user-images.githubusercontent.com/13360207/212101979-e29b3122-5665-47f4-9b89-58f9acede661.png">  

## Results:
1. Network trained using SGD optimizer, with learning rate of 0.01, batch size = 128, for 20 Epochs
2. Test set: Average loss: 0.0171
3. Accuracy: 9941/10000 (99.4%)

## Training Logs 

loss=0.19803179800510406 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.08it/s]
Test set: Average loss: 0.0641, Accuracy: 9808/10000 (98.1%)

loss=0.07573869079351425 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.09it/s]
Test set: Average loss: 0.0397, Accuracy: 9878/10000 (98.8%)

loss=0.1322895884513855 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.55it/s]
Test set: Average loss: 0.0313, Accuracy: 9891/10000 (98.9%)

loss=0.06421316415071487 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.54it/s]
Test set: Average loss: 0.0286, Accuracy: 9906/10000 (99.1%)

loss=0.044296275824308395 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.44it/s]
Test set: Average loss: 0.0262, Accuracy: 9919/10000 (99.2%)

loss=0.05155544355511665 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.11it/s]
Test set: Average loss: 0.0261, Accuracy: 9911/10000 (99.1%)

loss=0.03312501683831215 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.32it/s]
Test set: Average loss: 0.0222, Accuracy: 9926/10000 (99.3%)

loss=0.00557462265715003 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 27.95it/s]
Test set: Average loss: 0.0268, Accuracy: 9916/10000 (99.2%)

loss=0.0999639630317688 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.22it/s]
Test set: Average loss: 0.0219, Accuracy: 9939/10000 (99.4%)

loss=0.04821547865867615 batch_id=468: 100%|██████████| 469/469 [00:17<00:00, 26.65it/s]
Test set: Average loss: 0.0310, Accuracy: 9912/10000 (99.1%)

loss=0.007714048493653536 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 27.99it/s]
Test set: Average loss: 0.0228, Accuracy: 9925/10000 (99.2%)

loss=0.01548339519649744 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.15it/s]
Test set: Average loss: 0.0184, Accuracy: 9946/10000 (99.5%)

loss=0.017923129722476006 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.30it/s]
Test set: Average loss: 0.0205, Accuracy: 9937/10000 (99.4%)

loss=0.014997020363807678 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.30it/s]
Test set: Average loss: 0.0196, Accuracy: 9941/10000 (99.4%)

loss=0.022441944107413292 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.20it/s]
Test set: Average loss: 0.0226, Accuracy: 9929/10000 (99.3%)

loss=0.001764744403772056 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 27.82it/s]
Test set: Average loss: 0.0166, Accuracy: 9950/10000 (99.5%)

loss=0.01769092120230198 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 27.86it/s]
Test set: Average loss: 0.0184, Accuracy: 9949/10000 (99.5%)

loss=0.045729491859674454 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 27.95it/s]
Test set: Average loss: 0.0209, Accuracy: 9943/10000 (99.4%)

loss=0.018251623958349228 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.25it/s]
Test set: Average loss: 0.0171, Accuracy: 9941/10000 (99.4%)


