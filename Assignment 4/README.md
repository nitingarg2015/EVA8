# Assignment 4:
1.	New target is:
2.  99.4% (this must be consistently shown in your last few epochs, and not a one-time achievement)
3.	Less than or equal to 15 Epochs
4.	Less than 10000 Parameters (additional points for doing this in less than 8000 pts)
5.	Do this in at least 3 steps

## Initial Iteration - Assignment 4_init:
This is the base version we arrived at as part of assignment 3

### Result:
1. Parameters: 15,938, Learning Rate: 0.1, Epochs: 20
2. Best Training Accuracy: 99.08%, Best Test Accuracy: 99.48% 

### Analysis:
1. Number of parameters more than new target of 10000
2. Number of epochs to reach target of 99.4% greater than 20
3. Test accuracy is slightly unstable with variations in the range of 99.22% to 99.48% in last 4 epochs

### Plan for next iteration:
1.	Revisit the model by reducing parameters to around 10000
2.	Keep the structure similar to first iteration (Expand and Squeeze), reduce parameters by reducing number of channels in each convolutional layer
3.	Last layer – Change to convolutional layer instead of Fully Connected layer (as per model viewed in the EVA session

## Iteration 1: Assignment 4 – Iteration 1

### Target: 10000 – 12000 parameters, Epochs < 16

### Result:
1. Parameters: 11,450, Learning Rate: 0.1, Epochs: 15, Receptive Field: 54*54
2. Best Training Accuracy: 99.08%, Best Test Accuracy: 99.33% 

### Analysis:
1. Number of parameters still more than new target of 10000
2. 12 epochs to reach target of 99.3%
3. Test accuracy variations in the range of 99.29% to 99.33% in last 4 epochs
4. Reduction of parameters did not create major impact on loss of test accuracy

### Plan for next iteration:
1.	Revisit the model by reducing parameters to around 10000
2.	3rd Convolutional layer is contributing towards 4640 parameters. Reduce number of channels in this layer to bring # parameters to < 10000

## Iteration 2: Assignment 4 – Iteration 2

### Target: < 10000, Epochs < 16

### Result:
1.	Parameters: 9590, Learning Rate: 0.1, Epochs: 15, Receptive Field: 54*54
2.	Best Training Accuracy: 99.10%, Best Test Accuracy: 99.29%  

### Analysis:
1.	Number of parameters below expected target of 10000
2.	15 epochs to reach target of 99.29%
3.	Test accuracy variations in the range of 99.08% to 99.29% in last 4 epochs
4.	99.21% test accuracy was achieved in 8th Epoch. No significant learning post that
5.	Test accuracy improved from 97.76% in first epoch to 99.03% in 6th epoch. Post that learning had slowed down and was observed to be varying

### Plan for next iteration:
1.	Add learning rate schedules to reduce learning rate in steps:
2. StepLR with step size = 6 and gamma = 0.2

## Iteration 3: Assignment 4 – Iteration 3

### Target: < 10000, Epochs < 16, Test Accuracy ~99.4%

### Result:
1.	Parameters: 9590, Learning Rate: 0.1 with StepLR scheduler step size of 6 and gamma = 0.2, Epochs: 15, Receptive Field: 54*54
2.	Best Training Accuracy: 99.27%, Best Test Accuracy: 99.42% 

### Analysis:
1.	Number of parameters below expected target of 10000
2.	13 epochs to reach target of 99.41%
3.	99.31% test accuracy was achieved in 9th Epoch. 
4.	Test accuracy variations in the range of 99.23% to 99.42% in last 4 epochs

### Plan for next iteration:
1.	Stabilize learning by adjusting learning rate schedules

## Iteration 4: Assignment 4 – Iteration 4

### Target: < 10000, Epochs < 16, Test Accuracy ~99.4%
	StepLR with step size = 4 and gamma = 0.2

### Result:
1.	Parameters: 9590, Learning Rate: 0.1 with StepLR scheduler step size of 4 and gamma = 0.2, Epochs: 15, Receptive Field: 54*54
2.	Best Training Accuracy: 99.12%, Best Test Accuracy: 99.34% 

### Analysis:
1.	Test accuracy consistent from 99.32% to 99.34%
2.	Reached test accuracy of 99.32% in the 10th epoch
3.	Post that learning has not happened with test accuracy fluctuating between 99.32% and 99.34$

### Plan for next iteration:
1.	Increase learning rate increment to 0.4

## Iteration 5: Assignment 4 – Iteration 5

### Target: < 10000, Epochs < 16, Test Accuracy ~99.4%
	StepLR with step size = 4 and gamma = 0.4

### Result:
1.	Parameters: 9590, Learning Rate: 0.1 with StepLR scheduler step size of 4 and gamma = 0.4, Epochs: 15, Receptive Field: 54*54
2.	Best Training Accuracy: 99.22%, Best Test Accuracy: 99.32% 

### Analysis:
1.	Test accuracy varying from 99.20% to 99.31%
2.	Reached test accuracy of 99.32% in the 10th epoch
3.	Test accuracy fluctuating beyond 10th epoch

### Plan for next iteration:
Introduce RandomRotation((-5,5)) transformation

## Iteration 6: Assignment 4 – Iteration 6

### Target: < 10000, Epochs < 16, Test Accuracy ~99.4%
StepLR with step size = 4 and gamma = 0.4, with RandomRotation((-5,5)) transformation

### Result:
1.	Parameters: 9590, Learning Rate: 0.1 with StepLR scheduler step size of 4 and gamma = 0.4, Epochs: 15, Receptive Field: 54*54  
 
2. **Best Training Accuracy: 99.11%, Best Test Accuracy: 99.43%** 

### Analysis:
1.	Reached test accuracy of 99.38% in the 9th epoch
2.	**Achieved accuracy > 99.4 in last 2 epochs, and accuracy > 99.33 in last 5 epochs**


### Training Logs

EPOCH: 1 Learning Rate:  0.1
Loss=0.03220589831471443 Batch_id=468 Accuracy=92.74: 100%|██████████| 469/469 [00:22<00:00, 20.94it/s]

Test set: Average loss: 0.0581, Accuracy: 9813/10000 (98.13%)

EPOCH: 2 Learning Rate:  0.1
Loss=0.04848999157547951 Batch_id=468 Accuracy=97.41: 100%|██████████| 469/469 [00:20<00:00, 22.56it/s]

Test set: Average loss: 0.0491, Accuracy: 9842/10000 (98.42%)

EPOCH: 3 Learning Rate:  0.1
Loss=0.029843779280781746 Batch_id=468 Accuracy=98.03: 100%|██████████| 469/469 [00:20<00:00, 22.71it/s]

Test set: Average loss: 0.0420, Accuracy: 9868/10000 (98.68%)

EPOCH: 4 Learning Rate:  0.1
Loss=0.08162355422973633 Batch_id=468 Accuracy=98.26: 100%|██████████| 469/469 [00:20<00:00, 22.74it/s]

Test set: Average loss: 0.0292, Accuracy: 9911/10000 (99.11%)

EPOCH: 5 Learning Rate:  0.04000000000000001
Loss=0.02789262682199478 Batch_id=468 Accuracy=98.69: 100%|██████████| 469/469 [00:20<00:00, 22.70it/s]

Test set: Average loss: 0.0254, Accuracy: 9914/10000 (99.14%)

EPOCH: 6 Learning Rate:  0.04000000000000001
Loss=0.015598594211041927 Batch_id=468 Accuracy=98.74: 100%|██████████| 469/469 [00:20<00:00, 22.88it/s]

Test set: Average loss: 0.0283, Accuracy: 9903/10000 (99.03%)

EPOCH: 7 Learning Rate:  0.04000000000000001
Loss=0.024348855018615723 Batch_id=468 Accuracy=98.79: 100%|██████████| 469/469 [00:20<00:00, 23.03it/s]

Test set: Average loss: 0.0220, Accuracy: 9924/10000 (99.24%)

EPOCH: 8 Learning Rate:  0.04000000000000001
Loss=0.028741663321852684 Batch_id=468 Accuracy=98.88: 100%|██████████| 469/469 [00:20<00:00, 22.76it/s]

Test set: Average loss: 0.0232, Accuracy: 9919/10000 (99.19%)

EPOCH: 9 Learning Rate:  0.016000000000000004
Loss=0.07494921237230301 Batch_id=468 Accuracy=98.97: 100%|██████████| 469/469 [00:21<00:00, 21.70it/s]

Test set: Average loss: 0.0203, Accuracy: 9938/10000 (99.38%)

EPOCH: 10 Learning Rate:  0.016000000000000004
Loss=0.024480052292346954 Batch_id=468 Accuracy=99.00: 100%|██████████| 469/469 [00:20<00:00, 22.95it/s]

Test set: Average loss: 0.0210, Accuracy: 9931/10000 (99.31%)

EPOCH: 11 Learning Rate:  0.016000000000000004
Loss=0.010427321307361126 Batch_id=468 Accuracy=99.03: 100%|██████████| 469/469 [00:20<00:00, 22.53it/s]

Test set: Average loss: 0.0199, Accuracy: 9936/10000 (99.36%)

EPOCH: 12 Learning Rate:  0.016000000000000004
Loss=0.013095739297568798 Batch_id=468 Accuracy=99.02: 100%|██████████| 469/469 [00:20<00:00, 22.71it/s]

Test set: Average loss: 0.0207, Accuracy: 9933/10000 (99.33%)

EPOCH: 13 Learning Rate:  0.006400000000000002
Loss=0.01104509737342596 Batch_id=468 Accuracy=99.09: 100%|██████████| 469/469 [00:22<00:00, 21.16it/s]

Test set: Average loss: 0.0196, Accuracy: 9933/10000 (99.33%)

EPOCH: 14 Learning Rate:  0.006400000000000002
Loss=0.011890456080436707 Batch_id=468 Accuracy=99.07: 100%|██████████| 469/469 [00:20<00:00, 23.00it/s]

Test set: Average loss: 0.0190, Accuracy: 9943/10000 (99.43%)

EPOCH: 15 Learning Rate:  0.006400000000000002
Loss=0.014988377690315247 Batch_id=468 Accuracy=99.11: 100%|██████████| 469/469 [00:20<00:00, 22.95it/s]

Test set: Average loss: 0.0194, Accuracy: 9940/10000 (99.40%)
