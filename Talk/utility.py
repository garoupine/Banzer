#!/usr/bin/env python3

"""
Module Name: utils.py

Description: This module contains utility functions and classes for various tasks, including debugging, testing, and data visualization.

Classes:
None

Functions:


Author: Messaoudi Dhia Elhak
Date: 2023-04-24
"""

import numpy as np 
import matplotlib.pyplot as plt 
from IPython import display
import seaborn as sns
import tensorflow as tf

def audioplayback(label,waveform):
    print('Label:', label)
    print('Waveform shape:', waveform.shape)
    print('Audio playback')
    display.display(display.Audio(waveform, rate=16000))


def plot_spectrogram(spectrogram,ax):
    if len(spectrogram.shape) > 2:
        assert len(spectrogram.shape) == 3
        spectrogram = np.squeeze(spectrogram, axis=-1)
    log_spec = np.log(spectrogram.T + np.finfo(float).eps)
    height = log_spec.shape[0]
    width = log_spec.shape[1]
    X = np.linspace(0, np.size(spectrogram), num=width, dtype=int)
    Y = range(height)
    ax.pcolormesh(X, Y, log_spec)

def module_perforamance(history):
    metrics = history.history
    plt.figure(figsize=(16,6))
    plt.subplot(1,2,1)
    plt.plot(history.epoch, metrics['loss'], metrics['val_loss'])
    plt.legend(['loss', 'val_loss'])
    plt.ylim([0, max(plt.ylim())])
    plt.xlabel('Epoch')
    plt.ylabel('Loss [CrossEntropy]')

    plt.subplot(1,2,2)
    plt.plot(history.epoch, 100*np.array(metrics['accuracy']), 100*np.array(metrics['val_accuracy']))
    plt.legend(['accuracy', 'val_accuracy'])
    plt.ylim([0, 100])
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy [%]')

    plt.show()

def module_confusionmatrix(tst_spec_ds,y_pred,label_names):
    y_true = tf.concat(list(tst_spec_ds.map(lambda s,lab: lab)), axis=0)
    confusion_mtx = tf.math.confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(confusion_mtx,xticklabels=label_names,yticklabels=label_names,annot=True, fmt='g')
    plt.xlabel('Prediction')
    plt.ylabel('Label')
    plt.show()

def display_predictions(labels,predictions):
    plt.bar(labels, tf.nn.softmax(predictions[0]))
    plt.title("Probability distribution over the possible classes for the input")
    plt.show()

def get_command(path,commands):
    words = path.split('/')
    return  [word for word in words if word in commands].pop(0)
    #return command