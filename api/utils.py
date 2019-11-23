import os
import glob

from nltk.corpus import wordnet
from werkzeug.utils import secure_filename
import pytesseract 
from PIL import Image 
 
from api.constants import *

# Allowed file name function
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Synonyms generation function
def synonyms_list(keyword):
    synonyms = [] 
    for syn in wordnet.synsets(keyword): 
        for l in syn.lemmas(): 
            if l.name() not in ['number', 'full']:
                synonyms.append(l.name()) 
                synonyms.append(l.name().upper()) 
                synonyms.append(l.name().capitalize())
    return synonyms

# Image parser function
def image_parser(filename):
    return pytesseract.image_to_string(Image.open(BASE_DIR + DATA_DIR + filename)) 

# Generating the fields function
def generate_field(text_file, synonyms):
    target_lines = []
    results = []
    # Listing the possible lines for the form filling
    with open(text_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for w in line.split():
                if w in synonyms:
                    target_lines.append(line)
    # Cleaning the possible lines 
    for line in target_lines:
        for w in line.split():
            word = w.replace('.', '', 1)
            word = word.replace(',', '', 1)
            if word.isdigit(): 
                results.append(line) 
    return results