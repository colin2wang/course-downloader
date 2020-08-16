# -*- coding: utf-8 -*-
import urllib.request
import re


# 'https://media001.geekbang.org/e8fd515b954144fabbde0510683e5c7a/2a5a540b9349499fb6d32f924b18e3fc-a0eec740caa5343d32395f5b476ea608-ld-00001.ts'
# %05d

url_sample = 'https://media001.geekbang.org/ec1f43a9273c449eb101efaeec820ded/c6c8bd7fb6064043bcd16ed740f1dd87-ee91b047c67951619aec1059aa2192f9-hd-00013.ts'

url_tmpl = re.sub(r'[0-9]{5}.ts', '%05d.ts', url_sample)

filename_tmpl = 'GeekBang-%05d.ts'

for idx in range(1, 5000):
    url = url_tmpl % idx
    print(url)
    filename = 'video_cache\\' + filename_tmpl % idx
    try:
        urllib.request.urlretrieve(url, filename)
    except Exception as e:
        print('Stop due to exception: ' + e.__str__())
        break


