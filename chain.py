#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:07:48 2018

@author: Apostolidou Maria

Description: Markov Chain implementation for next word prediction.
             Trained for 1st, 2nd and 3rd order chains.
"""
from string import punctuation
from numpy.random import choice
import json

class MarkovChain(object):
    """
    Class of the Python implementation of the markov chain
    chain is a dictionary that represents the markov chain
    the keys of the chain are the states, i.e. words
    the values are also dictionaries that represent the next state
    the value of chain is a dictionary with key the next state (word)
    and value the number of times this transaction has occured
    """
    
    def __init__(self, order, chain={}):
        self.chain = chain 
        self.order = order
        
    def train(self, filename):
        """
        Given a file containing corpora, retrieves data-words from the input
        and updates the markov chain accordingly.
        Input files can be books from NLTK Gutenberg, text files, or even
        user input.
        To train the markov chain with user input, the text typed from the 
        user is saved to a file and given to this method as argument.
        Inpute: a string of the filenamefrom tkinter import *
        Return: nada
        """
        words = self.get_input_fron_file(filename)
        self.update_Markov_chain(words)
        
    def get_input_fron_file(self,filename):
        """
        Given a filename, opens the corresponding file to read it and return a
        list of the words in it, in the appropriate form (no punctiuation,
        capitals, etc). This list of words will be used to train the markov 
        chain
        Input: a string of the filename
        Return: a list of words
        """
        words = [] 
        with open(filename) as f:        
            for word in f.read().split():
                pure_word = self.strip_punctuation(word)
                words.append(pure_word.lower())
        return words
    
    def strip_punctuation(self,s):
        """
        Given a string s, strips away all punctuation marks
        Input: a string s
        Return: a string 
        """
        return ''.join(c for c in s if c not in punctuation)
        
    def update_Markov_chain(self, words):
        """
        Given a corpora of text, in the form of a list of words, greates states 
        in the chain for newly encountered words and updates the statistics.
        Whenever a 'word' followed by 'next_word' occurs in the corporam the 
        counter for next_state being the 'next_word' is incremented.
        For a higher order chain the state is a tuple of no. of order words
        Input : a list of words for trainign corpora, order of chain
        Return : nada
        """
       
        index = 0
        for word in words[:len(words)-self.order-1]:
            state = ' '.join(words[index:index + self.order+1])
            next_state = words[index + self.order + 1] 
            index += 1 
        
            if state not in self.chain:
                self.chain[state] = {}
        
            if next_state not in self.chain[state]:
                self.chain[state][next_state] = 0
            
            self.chain[state][next_state] += 1
    
        
            
    def find_next_state(self,state):
        """
        Given a state find the next state at random
        """
        
        state = self.strip_punctuation(state)
        if state not in self.chain.keys():
            # word has never been encountered in training
            return None
        else:            
            choices = list(self.chain[state].keys())
            weights = list(self.chain[state].values())
            # find propabilities from weights
            sum = self.calc_sum(weights)
            # -Debug- print(sum)
            prob = []
            for w in weights:
                prob.append(float(w)/sum)
            # -Debug- print(prob)
            return choice(choices,p=prob)
        
    def calc_sum(self,listarray):
        """
        Calculates the sum of the elements of a list
        Input: a list of numbers
        Return type: a float number
        """
        
        sum = 0.0
        for x in listarray:
            sum += x
        return sum
 
    # JSON methods
    
    def to_json(self, filename):
        """
        Converts the trained markov chain to a json object and stores it to a
        file for future use
        """
        
        with open(filename,'w') as f:
            json.dump(self.to_json_serializible(),f)
        
    def to_json_serializible(self):
        """
        Converts a MarkovChain object to a dictionary to be used from json
        """
        
        return {
                "order":self.order,
                "markov_chain":json.dumps(self.chain, sort_keys=True)
                }
     
    @classmethod
    def from_json(cls, filename):
        """
        Converts a json file containing the markov chain back to a MarkovChain 
        object to use 
        """
        
        with open(filename) as f:
            data = json.load(f)
        order = data['order']
        chain = json.loads(data['markov_chain'])
        obtained_chain = cls(order,chain)        
        return obtained_chain
    
