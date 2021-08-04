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

