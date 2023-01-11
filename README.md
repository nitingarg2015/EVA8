## Manual Forward and Back Propagation

Forward and Back Propagation steps were manually conducted for a neural network with 1) input layer with 2 neurons, 2) single hidden layer with 2 neurons and 3) Output layer with 2 neurons. Schematic diagram with initial weights is as per the below figure:


![image](https://user-images.githubusercontent.com/13360207/211772604-25ac1274-b38f-493d-b27e-f456f21c22bc.png)

Input Values are i1 = 0.05, i2 = 0.1 

Output values are t1 =  0.01, t2 = 0.99  

Loss function used in the network is calculated as below

![image](https://user-images.githubusercontent.com/13360207/211781404-e8278890-89d9-4598-bb52-c2248def9d6f.png)


Equations for forward and backward propagation are provided in the sheet *Parameter Calcs*

## Back Propagation
Our goal with back propagation algorithm is to update each weight in the network so that the actual output is closer to the target output, thereby minimizing the error for each output neuron and the network as a whole

Since we are propagating backward, the first thing we need to do is to calculate the change in total errors w.r.t the outputs o1 and o2. This is calculated as:
![image](https://user-images.githubusercontent.com/13360207/211782618-5e5ee934-50d7-427e-ac26-c4044b444b97.png)


Backpropagation to evaluate the sensitity of the output with respect to weight 5 is done by applying chain rule, map for the same is as shown below

![image](https://user-images.githubusercontent.com/13360207/211784133-83f24a49-4840-4a14-9da4-677071eba076.png)

Equation of backpropagating error w.r.t w5 is as below:

![image](https://user-images.githubusercontent.com/13360207/211784332-d52e2331-d48f-4ca9-ba22-7b1bfdaaeeed.png)

*This process is followed for all the weights from w1 to w8 and equations for each of these are provided in the excel sheet*  


