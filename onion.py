import base64
from Crypto.PublicKey import RSA
import hashlib

onion = "yvuqbyepwaowxm2p"
search = [line.rstrip("\n") for line in open("words.txt")]
count = 0


def searchIn(onion):
    results = ""
    rating = 0
    for value in search:
        if len(value) >= 4 and onion.startswith(value.encode()):
            results = results + "-" + value
            rating += pow(len(value), 2) * 2
        elif len(value) >= 5 and onion.find(value.encode()) != -1:
            results = results + "-" + value
            rating += pow(len(value), 2)
    if any(str.isdigit(c) for c in onion.decode('ascii')) is False:
        rating += 10
    if results == "":
        return 0, 0
    else:
        return results[1:], rating


while 1:
    searchResult = 0
    while searchResult == 0:
        key = RSA.generate(1024)

        priv = key.exportKey("PEM")
        pub = key.publickey().exportKey("PEM")
        onion = base64.b32encode(hashlib.sha1(pub).digest()[:10]).lower()
        searchResult, searchRating = searchIn(onion)
        count = count + 1
    print("Rating:", searchRating, searchResult, onion.decode('ascii'),
          "#", count)

    f = open("keys/%s-%s-%s.pem" % (searchRating, searchResult,
                                    onion.decode('ascii')), "w")
    f.write(priv.decode('ascii'))
    f.close()

    f = open("keys/%s-%s-%s.pub" % (searchRating, searchResult,
                                    onion.decode('ascii')), "w")
    f.write(pub.decode('ascii'))
    f.close()

    onion = "1111111111111111"
    searchRating = 0
