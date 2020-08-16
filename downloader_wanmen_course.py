import json
import os
import urllib.request
from utils.auth_utils import header_wanmen


def get_course_detail(idx, course_id, filename):
    # https://api.wanmen.org/4.0/content/lectures/59ed633e8a98b872ce637dcc?routeId=main
    url = "https://api.wanmen.org/4.0/content/lectures/{0}?routeId=main".format(course_id)

    opener = urllib.request.build_opener()
    opener.addheaders = header_wanmen()

    urllib.request.install_opener(opener)
    print(url)

    urllib.request.urlretrieve(url, filename)


maximum_batch_size = 5

if __name__ == '__main__':
    index = 0
    batch_idx = 1
    with open("site_data/wanmen/course/586d23485f07127674135d32.json", 'r', encoding='utf-8') as f:
        json_obj = json.loads(f.read())
        g_idx = 0
        for group in json_obj:
            g_idx += 1
            c_idx = 0
            # group_id = group['_id']
            group_name = group['name']
            root_id = group['courseId']
            for course in group['children']:
                c_idx += 1
                course_id = course['_id']
                course_name = course['name']
                folder_name = 'download\\wanmen\\{0}\\batch{1}\\'.format(root_id, batch_idx)
                os.makedirs(folder_name, exist_ok=True)
                filename = folder_name + 'G{0}_{1}_C{2}_{3}_{4}.json' \
                    .format(g_idx, group_name, c_idx, course_name, course_id)

                get_course_detail(course_id, course_id, filename)

                index += 1
                if index >= maximum_batch_size:
                    index = 0
                    batch_idx += 1
