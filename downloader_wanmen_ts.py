import _thread
import json
import urllib.request
import re
import os
from utils.thread_utils import CountDownLatch
from downloader_wanmen_constants import COURSE_ID


def start_download(path, c_id, latch):
    files = os.listdir(path)
    for fi in files:
        fi_d = os.path.join(path, fi)
        if os.path.isdir(fi_d):
            pass
            # print(os.path.join(path, fi_d))
            # get_files(fi_d)
        else:
            filename = fi_d
            print(filename)

            elements = filename.split('_')
            group_id = re.sub(r'[^G]*G', '', elements[0])
            group_name = '第{0}讲 {1}'.format(group_id, elements[1]).strip()
            course_id = re.sub(r'C', '', elements[2])
            course_name = '{0}.{1}{2}'.format(group_id, course_id, elements[3]).strip()

            with open(filename, 'r', encoding='utf-8') as f:
                json_obj = json.loads(f.read())
                video = json_obj['hls']['pcHigh']

                # url_sample = re.sub(r'\.m3u8.*', '0.ts', video)
                # url_tmpl = re.sub(r'[0-9]+.ts', '%d.ts', url_sample)

                url_sample = re.sub(r'\.m3u8.*', '00000.ts', video)
                url_tmpl = re.sub(r'[0-9]{5}.ts', '%05d.ts', url_sample)

                filename_tmpl = 'Wanmen-%05d.ts'

                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('Origin', 'https://www.wanmen.org'),
                    ('Referer',
                     'https://www.wanmen.org/courses/596f00f9c4e8e41da1410f38/lectures/59ed631b8a98b872ce637dc8'),
                ]
                urllib.request.install_opener(opener)

                for idx in range(0, 5000):
                    url = url_tmpl % idx
                    print(url)
                    folder_name = 'video_cache_all\\' + c_id + '\\' + group_name + '\\' + course_name + '\\'
                    os.makedirs(folder_name, exist_ok=True)
                    filename = folder_name + filename_tmpl % idx

                    try:
                        urllib.request.urlretrieve(url, filename)
                    except Exception as e:
                        print('Stop due to exception: ' + e.__str__())
                        break

    latch.count_down()


def gather_batch(c_id):
    path = "download\\wanmen\\{0}".format(c_id)
    files = os.listdir(path)
    size = len(files)
    latch = CountDownLatch(size)
    for fi in files:
        folder_name = os.path.join(path, fi)
        if os.path.isdir(folder_name):
            _thread.start_new_thread(start_download, (folder_name, c_id, latch,))

    latch.a_wait()


if __name__ == "__main__":
    gather_batch(COURSE_ID)
