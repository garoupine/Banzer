##!/usr/bin/env python3


"""
Module Name: module.py

Description: This module contains a class that manages audio datasets for machine learning tasks. It provides 
functions to download data from a given URL, prepare the data for training, get the labels, split the validation set,
and transform the data into mel-spectrograms.

Classes:
- Datasetmanager: A class that manages audio datasets for machine learning tasks.

Functions:


Author: Messaoudi Dhia Elhak
Date: 2023-04-24
"""


# Modules
import tensorflow as tf 
import numpy as np 
from keras import layers 
from keras import models
# Module code here

class Model():
    def __init__(self,input_shape,labels,data):
        self.shape = input_shape
        self.labels = labels
        self.lables_num = len(labels)
        self.norm_layer = layers.Normalization()
        self.norm_layer.adapt(data=data.map(map_func=lambda spec, label: spec))
        self.model = models.Sequential([
                    layers.Input(shape=self.shape),
                    layers.Resizing(32, 32),
                    self.norm_layer,
                    layers.Conv2D(32, 3, activation='relu'),
                    layers.Conv2D(64, 3, activation='relu'),
                    layers.MaxPooling2D(),
                    layers.Dropout(0.25),
                    layers.Flatten(),
                    layers.Dense(128, activation='relu'),
                    layers.Dropout(0.5),
                    layers.Dense(self.lables_num),
                    ])

    def verbose(self):
        self.model.summary() 

    def compile(self):
        self.model.compile(optimizer=tf.keras.optimizers.Adam(),
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=['accuracy'],)
        
    def train(self,train_ds,val_ds,epoches):
        self.history = self.model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epoches,
    callbacks=tf.keras.callbacks.EarlyStopping(verbose=1, patience=2),
    )
    
    def gethistory(self):
        return self.history
    
    def predict(self,spectogram):
        return self.model.predict(spectogram)
    
    def get_prediction(self,spectogram):
        tmp = self.predict(spectogram)
        tmp = self.labels[tf.argmax(tf.nn.softmax(tmp[0]))]
        print('predicted command',tmp)
        return tmp
