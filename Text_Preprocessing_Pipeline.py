# The potential of machine learning lies in the transition from data to insights, waiting to be 
# revealed in moments of analysis.-cbrwx

import re
import builtins
import os
import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
print("NLTK data downloaded successfully.")

# Define function for handling contractions
def expand_contractions(text, contractions_dict):
    pattern = re.compile('({})'.format('|'.join(contractions_dict.keys())), flags=re.IGNORECASE | re.DOTALL)
    def replace_text(t):
        txt = t.group(0)
        if txt.lower() in contractions_dict.keys():
            return contractions_dict[txt.lower()]
    expanded_text = pattern.sub(replace_text, text)
    return expanded_text

# Define function for handling numbers
def replace_numbers(text, replacement_token):
    return re.sub(r'\d+', replacement_token, text)

# Open the input file and read its contents
input_file = "e:\__results\enron_mails.txt"
with builtins.open(input_file, "r", encoding="utf-8") as f:
    text = f.read()
print("Input file read successfully.")

# Remove emails
text = re.sub(r"\S+@\S+", "", text)
print("Email addresses removed.")

# Remove unwanted characters
text = re.sub(r"[^a-zA-Z0-9\s\.\?,!'\"]", "", text)
print("Unwanted characters removed.")

# Expand contractions
contractions_dict = {"don't": "do not", "can't": "cannot", "won't": "will not", "shouldn't": "should not", "isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not", "hasn't": "has not", "haven't": "have not"}
text = expand_contractions(text, contractions_dict)
print("Contractions expanded.")

# Convert all text to lowercase
text = text.lower()
print("Text converted to lowercase.")

# Replace numbers
text = replace_numbers(text, "NUM")
print("Numbers replaced with 'NUM'.")

# Replace multiple spaces with a single space
text = re.sub(r"\s+", " ", text)
print("Multiple spaces replaced with a single space.")

# Remove leading and trailing spaces from each line
lines = text.split("\n")
lines = [line.strip() for line in lines]
print("Leading and trailing spaces removed from each line.")

# Remove empty lines
lines = [line for line in lines if line]
print("Empty lines removed.")

# Join the lines into a single string
text = "\n".join(lines)
print("Lines joined into a single string.")

# Tokenize the text
tokens = word_tokenize(text)
print("Text tokenized.")

# Lemmatize the tokens
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in tokens]
print("Tokens lemmatized.")

# Save the lemmatized text to a new file
output_file = "output_enron.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(" ".join(lemmas))
print("Lemmatized text saved to output file:", output_file)
