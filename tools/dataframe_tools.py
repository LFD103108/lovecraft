# in this file, we define function that are convenient for clean and manipulate dataframes

# Libraries
import pandas as pd
import re
import numpy as np
from pathlib import Path

#############################################################################################################################################

# Functions

# This function finds the project root by looking for a marker file (e.g., .git) in the current directory and its parents
def find_project_root(marker=".git"):
    path = Path.cwd()
    
    while path != path.parent:
        if (path / marker).exists():
            return path
        path = path.parent
    
    raise FileNotFoundError("Project root not found")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / "data"

# This function normalizes story titles by lowercasing, removing punctuation, and replacing spaces with underscores
def normalize_title(title): 
    if pd.isna(title):
        return None
    
    title = title.lower()
    
    # normalize unicode quotes/dashes
    title = (
        title.replace("’", "'")
             .replace("‘", "'")
             .replace("“", "")
             .replace("”", "")
             .replace("–", "-")
             .replace("—", "-")
    )
    
    # remove subtitles ("or ...")
    title = re.split(r"\s+or\s+", title)[0]
    
    # remove punctuation
    title = re.sub(r"[^\w\s]", "", title)
    
    # normalize spaces
    title = re.sub(r"\s+", "_", title.strip())
    
    return title