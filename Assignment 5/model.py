"""model.ipynb
Define Net Class for training CNN model
During initialization, define normalization type as "batch", "layer" or "group" for respective normalization types
If group normalization is selected, we have optional parameter - num_groups to be defined, default value is set as 4

It accepts input image of type 1*28*28
"""

# CNN model definition
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, normalization_type, num_groups = 4):
        super(Net, self).__init__()

        self.normalization_type = normalization_type
        self.num_groups = num_groups

        if self.normalization_type == 'batch':
            self.conv1 = nn.Sequential(
                nn.Conv2d(1, 8, 3, padding=1),                      #input: 1*28*28, output: 8*28*28, RF: 3*3
                nn.BatchNorm2d(8),
                nn.Dropout(0.05)
            )
            
            self.conv2 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding=1),                     #input: 8*28*28, output: 16*28*28, RF: 5*5 
                nn.BatchNorm2d(16),
                nn.Dropout(0.05)
            )

            self.conv3 = nn.Sequential(
                nn.Conv2d(16, 20, 3, padding=1),                     #input: 16*28*28, output: 20*28*28, RF: 7*7 
                nn.BatchNorm2d(20),
                nn.Dropout(0.05)
            )

            self.conv4 = nn.Sequential(
                nn.Conv2d(20, 8, 1),                                #input: 20*28*28, output: 8*28*28, RF: 7*7
                nn.MaxPool2d(2, 2),                                  #input: 8*28*28, output: 8*14*14, RF: 8*8
                nn.Dropout(0.05)
            )

            self.conv5 = nn.Sequential(
                nn.Conv2d(8, 8, 3, padding=1),                     #input: 8*14*14, output: 8*14*14, RF: 12*12 
                nn.BatchNorm2d(8),
                nn.Dropout(0.05)
            )

            self.conv6 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding=1),                     #input: 8*14*14, output: 16*14*14, RF: 16*16 
                nn.BatchNorm2d(16),
                nn.Dropout(0.05)
            )

            self.conv7 = nn.Sequential(
                nn.Conv2d(16, 8, 1),                                 #input: 16*14*14, output: 8*14*14, RF: 16*16 
                nn.MaxPool2d(2, 2),                                  #input: 8*14*14, output: 8*7*7, RF: 18*18
                #nn.Dropout(0.05)
            )

            self.conv8 = nn.Sequential(
                nn.Conv2d(8, 8, 3, padding = 1),                     #input: 8*7*7, output: 8*7*7, RF: 26*26 
                nn.BatchNorm2d(8),
                nn.Dropout(0.05)
            )

            self.conv9 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding = 1),                    #input: 8*7*7, output: 16*7*7, RF: 34*34 
                nn.BatchNorm2d(16),
                nn.Dropout(0.05)
            )

        elif self.normalization_type == 'layer':
            self.conv1 = nn.Sequential(
                nn.Conv2d(1, 8, 3, padding=1),                      #input: 1*28*28, output: 8*28*28, RF: 3*3
                nn.LayerNorm([8, 28,28], elementwise_affine = False),
                nn.Dropout(0.05)
            )
            
            self.conv2 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding=1),                     #input: 8*28*28, output: 16*28*28, RF: 5*5 
                nn.LayerNorm([16, 28,28], elementwise_affine = False),
                nn.Dropout(0.05)
            )

            self.conv3 = nn.Sequential(
                nn.Conv2d(16, 20, 3, padding=1),                     #input: 16*28*28, output: 20*28*28, RF: 7*7 
                nn.LayerNorm([20, 28, 28], elementwise_affine = False),
                nn.Dropout(0.05)
            )

            self.conv4 = nn.Sequential(
                nn.Conv2d(20, 8, 1),                                #input: 20*28*28, output: 8*28*28, RF: 7*7
                nn.MaxPool2d(2, 2),                                  #input: 8*28*28, output: 8*14*14, RF: 8*8
                nn.Dropout(0.05)
            )

            self.conv5 = nn.Sequential(
                nn.Conv2d(8, 8, 3, padding=1),                     #input: 8*14*14, output: 8*14*14, RF: 12*12 
                nn.LayerNorm([8, 14, 14], elementwise_affine = False),
                nn.Dropout(0.05)
            )

            self.conv6 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding=1),                     #input: 8*14*14, output: 16*14*14, RF: 16*16 
                nn.LayerNorm([16, 14, 14], elementwise_affine = False),
                nn.Dropout(0.05)
            )

            self.conv7 = nn.Sequential(
                nn.Conv2d(16, 8, 1),                                 #input: 16*14*14, output: 8*14*14, RF: 16*16 
                nn.MaxPool2d(2, 2),                                  #input: 8*14*14, output: 8*7*7, RF: 18*18
                #nn.Dropout(0.05)
            )

            self.conv8 = nn.Sequential(
                nn.Conv2d(8, 8, 3, padding = 1),                     #input: 8*7*7, output: 8*7*7, RF: 26*26 
                nn.LayerNorm([8, 7, 7], elementwise_affine = False),
                nn.Dropout(0.05)
            )

            self.conv9 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding = 1),                    #input: 8*7*7, output: 16*7*7, RF: 34*34 
                nn.LayerNorm([16, 7, 7], elementwise_affine = False),
                nn.Dropout(0.05)
            )

        elif self.normalization_type == 'group':
            self.conv1 = nn.Sequential(
                nn.Conv2d(1, 8, 3, padding=1),                      #input: 1*28*28, output: 8*28*28, RF: 3*3
                nn.GroupNorm(self.num_groups,8),
                nn.Dropout(0.05)
            )
            
            self.conv2 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding=1),                     #input: 8*28*28, output: 16*28*28, RF: 5*5 
                nn.GroupNorm(self.num_groups,16),
                nn.Dropout(0.05)
            )

            self.conv3 = nn.Sequential(
                nn.Conv2d(16, 20, 3, padding=1),                     #input: 16*28*28, output: 20*28*28, RF: 7*7 
                nn.GroupNorm(self.num_groups,20),
                nn.Dropout(0.05)
            )

            self.conv4 = nn.Sequential(
                nn.Conv2d(20, 8, 1),                                #input: 20*28*28, output: 8*28*28, RF: 7*7
                nn.MaxPool2d(2, 2),                                  #input: 8*28*28, output: 8*14*14, RF: 8*8
                nn.Dropout(0.05)
            )

            self.conv5 = nn.Sequential(
                nn.Conv2d(8, 8, 3, padding=1),                     #input: 8*14*14, output: 8*14*14, RF: 12*12 
                nn.GroupNorm(self.num_groups,8),
                nn.Dropout(0.05)
            )

            self.conv6 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding=1),                     #input: 8*14*14, output: 16*14*14, RF: 16*16 
                nn.GroupNorm(self.num_groups,16),
                nn.Dropout(0.05)
            )

            self.conv7 = nn.Sequential(
                nn.Conv2d(16, 8, 1),                                 #input: 16*14*14, output: 8*14*14, RF: 16*16 
                nn.MaxPool2d(2, 2),                                  #input: 8*14*14, output: 8*7*7, RF: 18*18
                #nn.Dropout(0.05)
            )

            self.conv8 = nn.Sequential(
                nn.Conv2d(8, 8, 3, padding = 1),                     #input: 8*7*7, output: 8*7*7, RF: 26*26 
                nn.GroupNorm(self.num_groups,8),
                nn.Dropout(0.05)
            )

            self.conv9 = nn.Sequential(
                nn.Conv2d(8, 16, 3, padding = 1),                    #input: 8*7*7, output: 16*7*7, RF: 34*34 
                nn.GroupNorm(self.num_groups, 16),
                nn.Dropout(0.05)
            )

        else:
            raise ValueError("Invalid normalization type")

        self.conv10 = nn.Sequential(
            nn.AvgPool2d(2, 2),                                  #input: 16*7*7, output: 16*3*3, RF: 38*38
            nn.Conv2d(16, 10, 3)                                #input: 16*3*3, output: 10*1*1, RF: 54*54
            #nn.BatchNorm2d(16),
            #nn.Dropout(0.10)
        )
        self.fc = nn.Linear(16*3*3, 10)
        
    def forward(self, x):
        x = F.relu(self.conv3(F.relu(self.conv2(F.relu(self.conv1(x))))))
        x = F.relu(self.conv6(F.relu(self.conv5(F.relu(self.conv4(x))))))
        x = F.relu(self.conv9(F.relu(self.conv8(F.relu(self.conv7(x))))))

        x = self.conv10(x)
        x = x.view(x.size(0), -1)

 #       x = self.fc(x)
        
        x = F.log_softmax(x, dim=1)
        return x