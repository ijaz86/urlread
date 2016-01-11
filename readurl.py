#Download images from a file with URL adresses

import urllib.request

input_file = open("urls", 'r')
for line in input_file:
    URL = line
    IMAGE = URL.rsplit('/',1)[-1]
    urllib.request.urlretrieve(URL, IMAGE)



