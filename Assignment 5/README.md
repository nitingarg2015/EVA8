## Assignment 5

### Objective

Three versions of 4th assignment's best model to be made with:
1. Network with Group Normalization
2. Network with Layer Normalization
3. Network with L1 + BN  

Write a single model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include
Write a single notebook file to run all the 3 models above for 20 epochs each
Create graphs for Test Loss and Test Accuracy
Find 10 misclassified images for each of the 3 models, and show them as a 5x2 image matrix in 3 separately annotated images
Explain how to perform the 3 normalizations techniques

### Model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include

Model.py file has been created that does the following
1. Defines Net Class for training CNN model
2. During initialization, define normalization type as "batch", "layer" or "group" for respective normalization types
3. If group normalization is selected, we have optional parameter - num_groups to be defined, default value is set as 4
4. It accepts input image of type 1*28*28  

### Assignment_5_v1.ipynb - Notebook runs remaining parts of the assignment  

1. Load **model.py** and import **Net class**, generaty summary using torchsummary - summary is generated for all three normalizations
![Training Parameters](https://user-images.githubusercontent.com/13360207/215048506-53ae5476-31ae-482f-8d32-374438150bfe.jpg)


2. Use dataloader to create training and test datasets, define batch size. batch size = 128 is used  
3. Define functions for training the model for a given epoch and generating test outputs
	a. **train** function taken inputs as pre defined model, device, train_loader (dataloader), pre defined optimizer, and optional lambda_l1 for L1 regularization. It returns the following: training loss, training accuracy for that epoch
	b. **test** function taken inputs as pre defined model, device, test_loader (dataloader). It returns the following: test loss, test accuracy for that epoch  
4. **train_model** function is defined to initate training for required number of epochs
	a. train_model inputs - model_type - batch, layer, or group normalization, lambda_l1 if required for L1 Regularization, and num_groups parameter for group normalization
	b. Generated output: 1. model - for generating test outputs, 2. train_losses, train_acc_all, test_losses, test_acc_all - For further analysis and generating plots
5. Train three models using **train_model_function** for 20 epochs  
6. Plot graphs for test loss and test accuracy


7. Define function **ntest** that return data points for incorrect predictions
	a. It accepts trained model, device and test_loader as inputs
	b. Outputs provided for all incorrect predictions, where length of each list = number of batches, and each tensor within the list contains data_images, pred_labels,  and target_labels for the given batch  
8. Define function **plot_misclassified** to plot misclassfied images  

Mispredictions for model with Batch Normalization & L1 Regularization


Mispredictions for model with Layer Normalization


Mispredictions for model with Group Normalization

