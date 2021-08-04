This research project proposes a method to automatically classify images of individuals to determine whether or not they are wearing a face mask.

The proposed method uses a ResNet50 model pre-trained on the ImageNet database. The model was first trained with feature extraction on the face masks data set, then further trained with fine-tuning. The data set underwent four data augmentation techniques; a random crop, flip, rotation and contrast factor. The proposed method achieved an accuracy of 99.34% on a publicly available face mask data set.


This code was made primarily following the Tensorfow tutorial: https://www.tensorflow.org/tutorials/images/transfer_learning

How to run:
1. Open main.py in an IDE such as Wing or Pycharm.
2. Run main.py

Code Structure:

Imports
Configure training, validaion and test dataset
Configure dataset for performance
Data Augmentation
Rescaling pixel values
Create the base model from the pre-trained convnets
Feature extraction
    - Freeze the convolutional base
    - Batch Normalisation
    - Add classification head
    - Compile model
    - Train model
    - Display learning curves using matplotlib
Fine tuning
    - Un-freeze te top layers of the model
    - Compile the model
    - Continue training the model
    - Evaluation and prediction

