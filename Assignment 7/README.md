## Assignment 7 with ResNet18, CIFAR dataset and GradCAM plotting  

### Objectives  
Your assignment is to build the above training structure. Train ResNet18 on Cifar10 for 20 Epochs. The assignment must:
pull your Github code to google colab (don't copy-paste code)
prove that you are following the above structure
that the code in your google collab notebook is NOTHING.. barely anything. There should not be any function or class that you can define in your Google Colab Notebook. Everything must be imported from all of your other files
your colab file must:
train resnet18 for 20 epochs on the CIFAR10 dataset
show loss curves for test and train datasets
show a gallery of 10 misclassified images
show gradcam Links to an external site.
output on 10 misclassified images.
ResNet18 model is loaded from models

### Outcomes  

1. ResNet18 is loaded from models  
2. CIFAR train and test data loaders are loaded from utils  
3. Sample images are viewed using imshow function from utils. RandomCrop, ShiftScaleRotate, CoarseDropout(16*16) transformations from Albumentations are applied only for train datasets  

<img width="398" alt="image" src="https://user-images.githubusercontent.com/13360207/218249129-4499fc6e-f3c5-44e6-90bc-ad6029c1933c.png">

4. Model is trained for 20 Epochs. Training and test losses/ accuracies as below  
  <img width="518" alt="image" src="https://user-images.githubusercontent.com/13360207/218249716-53afb15d-678d-4628-b05c-1b20bf5d447b.png">

5. Plot misclassified images  
<img width="404" alt="image" src="https://user-images.githubusercontent.com/13360207/218249729-808a2b6c-ff3e-4a7f-b93c-a50bedf66aa4.png">

6. GradCAM plot for images  
<img width="406" alt="image" src="https://user-images.githubusercontent.com/13360207/218249744-58ade7ba-cb01-4acd-b751-e14b9baf9086.png">


