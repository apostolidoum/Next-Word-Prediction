# Next-Word-Prediction

Implementation of a Markov Chain to represent sequences of possible words. Using text corpora from the Gutenberg project (or any other text file) creates a markov chain model that is used to predict the next word the user is going to type. 

## Description
The general idea is that by counting the number or times *word_A* is being followed by *word_B* in a text you can generate a markov model where the states of the chain are the *words* 

Using Python, the chain is represented by a **dictionary**. The keys of this dictionary are the **states** of the chain, i.e. the words, and the values are also dictionaries that represent the **next state**. The dictionary of the next state has as key the next state - word and as value the number of times this transition has occured. To better illustrate this the previous example would be represented as

```
{
 'word_A' : {'word_B': number of times the sequence *word_A word_B* has been encountered in text corpora}
}
```
After the chain has been created, transitions between states are made in a random but biased way, taking into account the probability for each transition, which in extracted by the number of times this transition has occured in text corpora.

The code was tested for markov chains of 1st, 2nd and 3rd order trained on text corpora from the Gutenberg project as found on the NLTK data. The 1st order chain is the usual memoryless chain. Higher order chains take into account group of words. For example a 2nd order chain would look like this

```
{
 'word_A word_B' : {
                    'word_C': number of times *word_A word_B word_C* was encountered,
                    'word_D': number of times *word_A word_B word_D* was encountered
                   }
}
```

## Prerequisites
Python 3

NLTK Data (optional)

## Usage

To use the Next-Word-Prediction you first need to create a markov chain and train it with text corpora. 

Provided you have the NLTK Data, you can run **train1storder.py**, **train2ndorder.py**, **train3rdorder.py** to create markov chains accordingly and train them from the Gutenberg project text corpora.

To install NLTK Data see [here]( https://www.nltk.org/data.html)

Any other text file can be used for training (read the comments of the above mentioned files for a detailed explanation on how to do that). The trained chain will be saved as a json file for later use.

To use Next-Word-Prediction to predict a word from user's typing, run **user.py**. This file will load a markov chain from a json file and read the text input the user is typing. To see a prediction for a next word, based on the last word/words you typed press Enter. Word prediction None means that no sequence containing the words you last typed was found in the corpora during training. To exit press q. 

## Examples

![example using 1st order chain](https://github.com/apostolidoum/Next-Word-Prediction/blob/master/pics/example1.png  "1st order")

![example using 2nd order chain](https://github.com/apostolidoum/Next-Word-Prediction/blob/master/pics/example2.png  "2nd order")

![example using 3rd order chain](https://github.com/apostolidoum/Next-Word-Prediction/blob/master/pics/example3.png  "3rd order")

## Test
File **retest.py** loads an already created markov chain from a json file and tests transitions between states.

## More information
