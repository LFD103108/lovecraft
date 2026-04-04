# In this file, we define functions that are convenient to clean and manipulate the text data

# Setup

# Libraries
import numpy as np   # imports the Numpy library for numerical tools
import os            # imports the OS library for interacting with the operating system  
#os.chdir('..')       # changes to the parent directory

###########################################################################################################

# Functions

# this functions checks if a given name is in the file
def search_name(file_path, name):
    with open(file_path) as file: 
        text = file.read() # reads the file
        if name in text: 
            print('YES')   # prints 'YES' if the name is found in the text
        else:
            print('NO')    # prints 'NO' if the name is not found in the text

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