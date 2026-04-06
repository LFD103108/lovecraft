# In this file, we define functions that are convenient to clean and manipulate the text data

# Setup

# Libraries
import numpy as np   # imports the Numpy library for numerical tools
import pandas as pd                     # imports the Pandas library for data manipulation and analysis
import os            # imports the OS library for interacting with the operating system  
from pathlib import Path               # imports the Path class from the pathlib library for working with file paths
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

        # text metadata DataFrame 
        self.df_texts = pd.read_csv("data/gold/texts.csv")  # loads the texts dataframe

        # numerical representation
        self.numerical_dict = np.load('data/gold/numerical_dict.npy', allow_pickle=True).item()  # loads the numerical dictionary from a file in NumPy format
        # entries are the story names, with the stories being stored as lists of numerical values
        
        # Fourier transform
        self.fourier_dict = np.load('data/gold/fourier_dict.npy', allow_pickle=True).item()  # loads the Fourier dictionary from a file in NumPy format
        # entries are the story names, with the stories being stored as lists of complex numbers (the Fourier transform of the numerical representation)
        