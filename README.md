# Onion-Generator
Generate .onion domains with a simple Python script

## Process

The process of generating these domains is relatively simple, but the chances of generating a specific domain are slim. It make take tens-of-thousands, if not more, iterations before a domain is found that is satisfactory.

Do not expect to find an exact match for a Tor domain, as there are 32^16 (or 1.2e24) different possible domains. 

1. Generate a 1024 bit RSA keypair
2. Using the public key from said keypair, compute the SHA1 digest
3. Grab the first 10 digits of said digest
4. Convert the digest to the Base32 encoding
5. (Add `.onion` to the end of the digest)

```python
key = RSA.generate(1024)
priv = key.exportKey('PEM')
pub = key.publickey().exportKey('PEM')
onion = base64.b32encode(hashlib.sha1(pub).digest()[:10]).lower()
```
        
## Chances of Success

A domain can contain any character from A-Z and any digit from 2-7. That leaves 32 options per byte. The table below outlines the number of computations that would statistically be required to get a domain with a specific word somewhere in it.

| Length | Statistic | Computations |
| ------ | --------- | ------------ |
| 1 | 32^1 | 32 |
| 2 | 32^2 | 1,024 |
| 3 | 32^3 | 32,768 |
| 4 | 32^4 | 1,048,576 |
| 5 | 32^5 | 33,554,432 |
| 6 | 32^6 | 1,073,741,824 |
| 7 | 32^7 | 34,359,738,368 |
| 8 | 32^8 | 1,099,511,627,776 |
| & | So | On |

The reason that this script works long before reaching a trillion iterations is that we are not looking for a specific word at the beginning of the domain, but we are searching for a large number of words anywhere in the domain. We can then refer to those with the highest ratings and pick out any of value.

## Examples

- 2heydare7dvkj7t4 [.onion] "Hey there"
- errorvttrooz3mr2 [.onion] "Error"
- vk66etreadyage65 [.onion] "(Get) Ready (for) Age = 65"
- bikef2rmplcsk3hb [.onion] "Bike to..."
- busyqkswix6kt42i [.onion] "Busy"
- cashkhq3lzfn2z3j [.onion] "Cash"
- newsgvmaumyg5wcc [.onion] "News"

### Longest word matches found

After a few hours of searching with a 3,000 word list, these were the highest rated matches found

Rating: 36
*Longest word match found: **Camera** in **bfcamerafz4h32hz***

Rating: 50
*Longest word match found at beginning of domain: **Floor** in **floordslujm7ndrc***


## Installation

### Install Python's PyCrypto library

`pip install pycrypto`

### Run the program in a UNIX shell

`python onion.py`

A `/keys/` directory is required to run the script

`mkdir keys` if it is not already there

## Notes

- *Multiple instances of this script can run at the same time*

- *PyCrypto does not seem to be the fastest way to create public and private keys, but regardless, it works! I was able to create anywhere between 30-100 per minute, depending on the hardware that I ran it on.*

### Ratings

A simple script is written to give each "domain" a rating.
 - For each word found: (length of word) ^ 2
 - - If word found is at the beginning of the domain, it's rating is doubled
 - +10 rating for domains with no numbers

### Accountability

- *I do not condone any direct uses for these private/public key pairs and have not tested them directly. I provided this script because of its useful practice with Python's cryptographic functions, and I claim no responsibility for what they are used for.*

- *The attached `words.txt` file is a list of many popular words in the English language, but I did not come up with the list myself.*
