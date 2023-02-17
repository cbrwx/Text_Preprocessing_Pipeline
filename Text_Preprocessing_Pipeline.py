# The potential of machine learning lies in the transition from data to insights, waiting to be 
# revealed in moments of analysis.-cbrwx

import re
import builtins
import os
import nltk
import codecs

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

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

# Identify the encoding of the file and open it
with codecs.open(input_file, "rb") as f:
    text = f.read()
    # Attempt to detect the encoding using a list of possible encodings
    possible_encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
    for encoding in possible_encodings:
        try:
            text = text.decode(encoding)
            print(f"Input file read successfully using {encoding} encoding.")
            break
        except:
            continue

# Remove emails
text = re.sub(r"\S+@\S+", "", text)
print("Email addresses removed.")

# Remove unwanted characters
text = re.sub(r"[^a-zA-Z0-9\s\.\?,!'\"]", "", text)
print("Unwanted characters removed.")

# Expand contractions
# contractions_dict = {"don't": "do not", "can't": "cannot", "won't": "will not", "shouldn't": "should not", "isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not", "hasn't": "has not", "haven't": "have not"}

contractions_dict = {
    "ain't": "are not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he's": "he is",
    "how'd": "how did",
    "how'll": "how will",
    "how's": "how is",
    "i'd": "I would",
    "i'll": "I will",
    "i'm": "I am",
    "i've": "I have",
    "isn't": "is not",
    "it'd": "it would",
    "it'll": "it will",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "must've": "must have",
    "mustn't": "must not",
    "needn't": "need not",
    "oughtn't": "ought not",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "she'd": "she would",
    "she'll": "she will",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "that's": "that is",
    "there'd": "there would",
    "there'll": "there will",
    "there're": "there are",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'll": "we will",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "where'd": "where did",
    "where's": "where is",
    "who'll": "who will",
    "who's": "who is",
    "won't": "will not",
    "would've": "would have",
    "wouldn't": "would not",
    "y'all": "you all",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have"
}

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

# Remove words that appear more than 3 times after itself on a single line
new_lines = []
for line_num, line in enumerate(lines):
    line_tokens = line.split()
    new_line_tokens = []
    for i in range(len(line_tokens)):
        # Check if the current word appears more than 3 times after itself on the same line
        if i < len(line_tokens) - 3 and line_tokens[i] == line_tokens[i+1] == line_tokens[i+2] == line_tokens[i+3]:
            # print(f"Line {line_num}: Word '{line_tokens[i]}' appears more than 3 times after itself on the same line. Removing the redundant occurrences.")
            continue
        new_line_tokens.append(line_tokens[i])
    # Join the tokens back into a string and append it to the new_lines list
    new_line = " ".join(new_line_tokens)
    new_lines.append(new_line)
    # Print a message indicating the number of tokens removed from the line (if any)
    tokens_removed = len(line_tokens) - len(new_line_tokens)
    if tokens_removed > 0:
        print(f"Line {line_num}: Removed {tokens_removed} redundant occurrences of a word.")
print("Redundant occurrences of words removed from the text.") 


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
output_file = "wikipedia_articles_universe_tokenized.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(" ".join(lemmas))
print("Lemmatized text saved to output file:", output_file)
