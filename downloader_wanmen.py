# -*- coding: utf-8 -*-
import urllib.request
import re


# https://media.wanmen.org/59e7daa8-54b6-44ca-b299-aed76da50961_pc_high00001.ts
# https://media.wanmen.org/0c5ad07b-bae8-442a-a7f5-7bcf824c47ae_pc_high0.ts
# %05d

# url_sample = 'https://media.wanmen.org/a99b71a4-4cdc-458c-b0ae-3559be61c170_pc_high00000.ts'
# url_tmpl = re.sub(r'[0-9]{5}.ts', '%05d.ts', url_sample)

url_sample = 'https://media.wanmen.org/ab5b66b2-9563-49b4-894f-63dc987c5cd1_pc_high3.ts'
url_tmpl = re.sub(r'[0-9]+.ts', '%d.ts', url_sample)

filename_tmpl = 'Wanmen-%05d.ts'

opener = urllib.request.build_opener()
opener.addheaders = [
    ('Origin', 'https://www.wanmen.org'),
    ('Referer', 'https://www.wanmen.org/courses/596f00f9c4e8e41da1410f38/lectures/59ed631b8a98b872ce637dc8'),
]
urllib.request.install_opener(opener)

for idx in range(0, 5000):
    url = url_tmpl % idx
    print(url)
    filename = 'video_cache\\' + filename_tmpl % idx
    try:
        urllib.request.urlretrieve(url, filename)
    except Exception as e:
        print('Stop due to exception: ' + e.__str__())
        break





