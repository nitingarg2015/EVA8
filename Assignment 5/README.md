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
<img width="507" alt="image" src="https://user-images.githubusercontent.com/13360207/215048718-b284c36c-a854-434e-9cbc-af3d03452c8b.png">

7. Define function **ntest** that return data points for incorrect predictions
	a. It accepts trained model, device and test_loader as inputs
	b. Outputs provided for all incorrect predictions, where length of each list = number of batches, and each tensor within the list contains data_images, pred_labels,  and target_labels for the given batch  
8. Define function **plot_misclassified** to plot misclassfied images  

Mispredictions for model with Batch Normalization & L1 Regularization  

<img width="395" alt="image" src="https://user-images.githubusercontent.com/13360207/215048794-e149a7bb-f281-4bfd-97ec-b78ffda44356.png">

Mispredictions for model with Layer Normalization  

<img width="394" alt="image" src="https://user-images.githubusercontent.com/13360207/215048838-0564a770-ada8-4438-b86a-87786d138fd0.png">

Mispredictions for model with Group Normalization  

<img width="393" alt="image" src="https://user-images.githubusercontent.com/13360207/215048865-2c324d4b-fb92-4a1b-8e57-86b41d9f9991.png">

### Findings from Normalization Techniques  
1. Batch normalization provides least test loss and highest test accuracy. This may be because the base model for fine tuned earlier for batch normalization
2. Fluctuation is observed in the rate of decrease in loss/ rate of increase of accuracy for batch normalization
3. Test loss reduces more consistenlty for Layer and Group normalization
4. Outcomes: Batch Normalizaiton: Test Accuracy - 99.27%, Layer Normalization - 99.02%, Group Normalization - 99.25%
5. Layer Normalization - Number of trainable parameters increased from 9590 to 90,158  

### Method to perform three Normalization Techniques  
Consider data set with batch size = 3, Number of Layers = 2, Channels per layer = 4, and input image size = 2x2. Sample data for this data set is as below. Refer Excel file "Regularization demonstration" in this assignment  

<img width="689" alt="image" src="https://user-images.githubusercontent.com/13360207/215062029-8ecb5f40-50b3-447b-8be2-645fd0a54df6.png">

#### Batch Normalization  
In Batch Normalization, mean and standard deviation is calculated for each channel, with sample size = batch size. For the above example, 4 mean and 4 variances will be calcuated for each layer
Number of calculations for Mean and Std Deviation = 16. Calculations for sample data as below  

<img width="597" alt="image" src="https://user-images.githubusercontent.com/13360207/215062111-e45fb295-15d9-46b6-84e3-d5789a1d61cd.png">

### Layer Normalization  
In Layer Normalization, mean and standard deviation is calculated for item in the batch with sample size = number of channels. For the above example, 3 mean and 3 variances will be calcuated for each layer
Number of calculations for Mean and Std Deviation = 8. Calculations for sample data as below  

<img width="674" alt="image" src="https://user-images.githubusercontent.com/13360207/215062169-e3f6d498-ac8e-4062-a2c3-f558ce7945cc.png">

### Group Normalization  
In Group Normalization, each layer is divided into n groups. Mean and standard deviation is then calculated for each item of the batch for defined group size. This helps to work with small batch sizes and higher number of channels per layer. Calculations for sample data as below 

<img width="676" alt="image" src="https://user-images.githubusercontent.com/13360207/215062212-2e706630-8043-4bc6-ad59-a3ae7606547f.png">


