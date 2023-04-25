#!/usr/bin/env python3


"""
Module Name: Datasetmanager.py

Description: This module contains a class that manages audio datasets for machine learning tasks. It provides 
functions to download data from a given URL, prepare the data for training, get the labels, split the validation set,
and transform the data into mel-spectrograms.

Classes:
- Datasetmanager: A class that manages audio datasets for machine learning tasks.

Functions:
getsample1(): return normal sample (audio label) from the train_ds dataset
getsample2(): return a sectogram from the train_spectrogram_ds

Author: Messaoudi Dhia Elhak
Date: 2023-04
"""


# Modules
import os 
import pathlib
import tensorflow as tf 
import numpy as np 
#from tensorflow import keras

# Module code here

class Datasetmanager():
    def __init__(self,path):
        #self.data_dir_path = path
        self.data_dir = pathlib.Path(path)
        #train_ds ,evaluate_ds = pass
    
    def getdata(self,link):
        data_dir = self.data_dir
        if not data_dir.exists():
            tf.keras.utils.get_file(
            'mini_speech_commands.zip',
            origin=link,
            extract=True,
            cache_dir='.', cache_subdir='data')
        else:
            print("Data already downloaded")

    def prepdata(self):
        self.train_ds, self.val_ds = tf.keras.utils.audio_dataset_from_directory(
            directory=self.data_dir,
            batch_size=64,
            validation_split=0.2,
            seed=0,
            output_sequence_length=16000,#Period in kHZ
            subset='both')
        
        
        
        #return self.train_ds,self.val_ds

    def getlabels(self):
        self.label_names = np.array(self.train_ds.class_names)
        return self.label_names
        #print('Commands:', commands) 

    #This dataset only contains single channel audio, so use the tf.squeeze function to drop the extra axis:
    def squeeze(self):
        self.train_ds = self.train_ds.map(lambda audio, labels: (tf.squeeze(audio, axis=-1), labels), tf.data.AUTOTUNE)
        self.val_ds = self.val_ds.map(lambda audio, labels: (tf.squeeze(audio, axis=-1), labels), tf.data.AUTOTUNE)
        
    #This function is called to split the validation set into two subsets one for validation and one for testing
    def split(self):    
        self.val_ds = self.val_ds.shard(num_shards=2, index=1)
        self.test_ds = self.val_ds.shard(num_shards=2, index=0)
    
    def verbose(self):
        if hasattr(self, 'trai_ds'): 
            print(self.train_ds.element_spec)
        if hasattr(self, 'val_ds'):     
            print(self.val_ds.element_spec)
        if hasattr(self, 'test_ds'):  
            print(self.test_ds.element_spec)
    
    #utility fucntion to tranfrom the data to mel-spectograms
    def get_spectrogram(self,waveform):
            spectrogram = tf.signal.stft(waveform, frame_length=255, frame_step=128)
            spectrogram = tf.abs(spectrogram)
            spectrogram = spectrogram[..., tf.newaxis]
            return spectrogram   
    
    def make_spec_ds(self):
        self.train_spectrogram_ds = self.train_ds.map(map_func=lambda audio,label: (self.get_spectrogram(audio), label),num_parallel_calls=tf.data.AUTOTUNE)
        self.val_spectrogram_ds = self.val_ds.map(map_func=lambda audio,label: (self.get_spectrogram(audio), label),num_parallel_calls=tf.data.AUTOTUNE)
        if hasattr(self, 'test_ds'):
            self.test_spectrogram_ds = self.test_ds.map(map_func=lambda audio,label: (self.get_spectrogram(audio), label),num_parallel_calls=tf.data.AUTOTUNE)
            return self.train_spectrogram_ds, self.val_spectrogram_ds, self.test_spectrogram_ds
        else:
            return self.train_spectrogram_ds, self.val_spectrogram_ds

    def preprocess(self):
        self.train_spectrogram_ds = self.train_spectrogram_ds.cache().shuffle(10000).prefetch(tf.data.AUTOTUNE)
        self.val_spectrogram_ds = self.val_spectrogram_ds.cache().prefetch(tf.data.AUTOTUNE)
        if hasattr(self, 'test_ds'): 
            self.test_spectrogram_ds = self.test_spectrogram_ds.cache().prefetch(tf.data.AUTOTUNE)

    def getsample(self,size):
        for i in range(size):
            for audio_sample, audio_sample_label in self.train_ds.take(1):
                break;  
        return audio_sample,audio_sample_label
    
    def get_sectogram_sample(self,size):
        for i in range(size):
            for spectogram, sectogram_label in self.train_spectrogram_ds.take(1):
                break;  
        return spectogram, sectogram_label
    
    #Return the encoded wavefile and the spectogram
    def encode_audio(self,path):
        #tmp = self.data_dir/path
        #tmp = tf.io.read_file(str(tmp))
        tmp = tf.io.read_file(path)
        tmp, sample_rate = tf.audio.decode_wav(tmp, desired_channels=1, desired_samples=16000,)
        tmp = tf.squeeze(tmp, axis=-1)
        waveform = tmp
        tmp = self.get_spectrogram(tmp)
        tmp = tmp[tf.newaxis,...]
        return waveform,tmp



def setseed(seed):
    tf.random.set_seed(seed)
    np.random.seed(seed)



if __name__ == '__main__':

    # Set the seed value for experiment reproducibility.
    seed = 42
    setseed(seed)



    with open('config.txt', 'r') as f:
        config = dict(line.strip().split('=') for line in f)

    url = config['url']
    path = config['path']


#print(url)
#print(path)
#url="http://storage.googleapis.com/download.tensorflow.org/data/mini_speech_commands.zip"
#DATASET_PATH = 'data/mini_speech_commands'
#data_dir = pathlib.Path(DATASET_PATH)

    foo = Datasetmanager(path)
    foo.getdata(url)
    foo.prepdata()
    foo.getlabels()
    #foo.verbose()
    foo.squeeze()
    #foo.split()
    #foo.verbose()
    foo.make_spec_ds()
