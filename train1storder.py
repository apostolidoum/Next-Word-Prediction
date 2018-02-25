#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 19:37:43 2018

@author: Apostolidou Maria

Description: Training module of 1st order Markov Chain
             using nltk corpora from project gutenberg
             
Important: To use you need to download nltk and change the path accordingly, 
           to find the nltk_date/corpora/gutenberg folder on your computer.
           To train the markov chain, any text file can be used.
           To create and train a markov chain with a text file example.txt
           run:
               mc = MarkovChain(0)
               mc.train('example.txt')
"""
from chain import MarkovChain
from nltk.corpus import gutenberg


# creating the chain 
# 1st order -> 0
mc = MarkovChain(0)

# train
# download nltk and change path accordingly
# any text file can be used to train the chain
corpora_path = '/usr/local/share/nltk_data/corpora/gutenberg/'

for filename in gutenberg.fileids():
    print(corpora_path+str(filename))
    try:
        mc.train(corpora_path+str(filename))
    except (UnicodeDecodeError):
        pass
    

# testing
# print(mc.chain)
# print(mc.find_next_state('it')) #first order
# print(mc.find_next_state('gain'))

    
# convert to json and save to file
mc.to_json('markov_chain_1st_order.json')



