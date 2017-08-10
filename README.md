# Onion-Generator
Generate .onion domains with a simple Python script



## Install Python's PyCrypto library

`pip install pycrypto`

## Run the program in a UNIX shell

`python onion.py`

### A `/keys/` directory is required to run the script

`mkdir keys` if it is not already there

*Note: Multiple instances of this script can run at the same time*

*Note: PyCrypto does not seem to be the fastest way to create public and private keys, but regardless, it works! I was able to create anywhere between 30-100 per minute, depending on the hardware that I ran it on.*

### Ratings

A simple script is written to give each "domain" a rating.
 - For each word found: (length of word) ^ 2
 - - If word found is at the beginning of the domain, it's rating is doubled
 - +10 rating for domains with no numbers

## Accountability

*I do not condone any direct uses for these private/public key pairs and have not tested them directly. I provided this script because of its useful practice with Python's cryptographic functions, and I claim no responsibility for what they are used for.*

*The attached `words.txt` file is a list of many popular words in the English language, but I did not come up with the list myself.*
