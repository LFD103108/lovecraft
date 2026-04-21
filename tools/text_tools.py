# In this file, we define functions that are convenient to clean and manipulate the text data

# Setup

# Libraries
import numpy as np   # imports the Numpy library for numerical tools
import pandas as pd                     # imports the Pandas library for data manipulation and analysis
from scipy import stats # imports statiscal tools
import os            # imports the OS library for interacting with the operating system  
from pathlib import Path               # imports the Path class from the pathlib library for working with file paths
import re  # for regex splitting
#os.chdir('..')       # changes to the parent directory

###########################################################################################################

# Functions

# this functions checks if a given name is in the file
def search_name(file_path, name):
    with open(file_path) as file: 
        text = file.read() # reads the file
        if name in text: 
            value = 1   # sets the value to 1
        else:
            value = 0   # sets the value to 0
    return value

def string_to_numerical(string):
    numerical_form = [ ord(symbol) for symbol in string] # converts each symbol to a numerical value
    return np.array(numerical_form)                      # returns the numerical form as a Numpy array


# this function reads a filename.txt file and creates a dictionary with the file name and the rest of the text splitted into sentences

def text_sentences(filename): 


    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read() 

    abbreviations = ["Mr", "Mrs", "Ms", "Dr", "Prof", "Sr", "Jr", "St", "Mme", "Mlle"]
    abbreviations_lookbehind = "".join(f"(?<!\\b{abbr})" for abbr in abbreviations) # makes a lookbehind that detects patterns before the split reference. 

    split_pattern = re.compile(
    rf'{abbreviations_lookbehind}\.(?:[“”"\'\)\]]*)(?=\s+[A-Z]|$)')  # join the lookbehind with a positive lookahead that detects patters after the split reference. 

    sentences = [phrase.strip() for phrase in re.split(split_pattern, text) if phrase.strip()]

    return sentences

# this function calculates statistical quantities such as mean, mode, median, standard deviation, skewness and kurtosis

def dist_statistics(distribution): 
    distribution_statistics = {}

    distribution_mean = np.mean(distribution)
    distribution_std = np.std(distribution)
    distribution_median = np.median(distribution)
    distribution_mode = float(stats.mode(distribution).mode)
    distribution_skew = stats.skew(distribution)
    distribution_kurt = stats.kurtosis(distribution)

    distribution_statistics = {'mean': float(round(distribution_mean, 4)), 
                               'standard_deviation': float(round(distribution_std, 4)), 
                               'distribution_mode': float(round(distribution_mode, 4)), 
                               'distribution_median': float(round(distribution_median, 4)),
                               'distribution_skew': float(round(distribution_skew, 4)),
                               'distribution_kurt': float(round(distribution_kurt, 4))
                               }

    return distribution_statistics


###########################################################################################################

# Class for working with the bibliography of texts

class bibliography():
    def __init__(self):

        # file names
        self.files =  os.listdir("data/silver/texts")  # saved as "name.txt", e.g. "cthulhu.txt"

        # texts
        self.texts = {name[0:-4]: open( "data/silver/texts/" + name ).read()  for name in self.files}
        # entries are the story names, with the stories being stored in strings
        # e.g. self.texts['cthulhu'] = "The Call of Cthulhu" story, as a string

        # sentences
        self.sentences = {name[:-4]: text_sentences(os.path.join("data/silver/texts", name)) for name in self.files}
        # entries are the story nomes, followed by a list containing its sentences

        # text metadata DataFrame 
        self.df_texts = pd.read_csv("data/gold/texts.csv")  # loads the texts dataframe

        # numerical representation
        self.numerical_dict = np.load('data/gold/numerical_dict.npy', allow_pickle=True).item()  # loads the numerical dictionary from a file in NumPy format
        # entries are the story names, with the stories being stored as lists of numerical values
        
        # Fourier transform
        self.fourier_dict = np.load('data/gold/fourier_dict.npy', allow_pickle=True).item()  # loads the Fourier dictionary from a file in NumPy format
        # entries are the story names, with the stories being stored as lists of complex numbers (the Fourier transform of the numerical representation)
        