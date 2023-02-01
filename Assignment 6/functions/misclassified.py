### Functions to plot misclassified images

'''
function to return data points for plotting misses
It accepts the following inputs:
1. trained model - trained on GPU, 2. device - cuda device, 3. images as a tensor (channel*shape*shape),
4) labels as 1D torch tensor

Outputs provided for all incorrect predictions, where length of each list = number of batches:
1. data_images - List of torch tensors of images, if no mispredictions in a given batch then empty tensor
2. pred_labels - List of Predicted labels, if no mispredictions in a given batch then empty tensor
3. target_labels - Ground truth or target labels, if no mispredictions in a given batch then empty tensor
'''
import torch
import collections

def get_miss_classified(model, device, images, labels):
    #images to labels to GPU
    if not (images.is_cuda):
        images = images.to(device)
    if not (labels.is_cuda):
        labels = labels.to(device)

    model.eval()

    with torch.no_grad():
        output = model(images)
        #predict labels
        pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
        #identify positions that are misclassified
        misses = torch.where(torch.not_equal(pred.squeeze(), labels))[0].cpu()

        # get missed information convert tensors back to cpu() for plotting images
        if images.is_cuda:
            data_images = images[misses].cpu()
        if labels.is_cuda:
            target_labels = labels[misses].cpu()
        if pred.is_cuda:
            pred_labels = pred[misses].cpu()

    return data_images, target_labels, pred_labels

'''
Function getFractionsMissed --> 
Input: model, device, test_loader
Output: fractions missed by each class
'''
def getFractionsMissed(model, device, test_loader):
    model.eval()
    missed_targets = []  # contains list of target labels by batch
    targets = []

    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)

            output = model(data)

            pred = output.argmax(dim=1, keepdim=True)  # get the index

            misses = torch.where(torch.not_equal(pred.squeeze(), target))
            missed_targets.append(target[misses].cpu())
            targets.append(target.cpu())

    targets = [x.item() for item in targets for x in item]
    missed_targets = [x.item() for item in missed_targets for x in item]

    # using Counter to find frequency of elements
    target_freq = collections.Counter(targets)
    miss_freq = collections.Counter(missed_targets)

    # calculate fraction misses for each class
    fractions_dict = {key: miss_freq[key] / target_freq.get(key, 0)
                      for key in target_freq.keys()}
    # sort fractions_dict by keys
    keys = list(fractions_dict.keys())
    keys.sort()
    fractions_dict = {i: fractions_dict[i] for i in keys}

    return fractions_dict