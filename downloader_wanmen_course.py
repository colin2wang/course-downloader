import json
import urllib.request
from utils.auth_utils import header_wanmen
import re


def get_course_detail(idx, course_id, filename):
     # https://api.wanmen.org/4.0/content/lectures/59ed633e8a98b872ce637dcc?routeId=main
    url = "https://api.wanmen.org/4.0/content/lectures/{0}?routeId=main".format(course_id)

    opener = urllib.request.build_opener()
    opener.addheaders = header_wanmen()

    urllib.request.install_opener(opener)
    print(url)

    urllib.request.urlretrieve(url, filename)


with open("download/59ed631b8a98b872ce637dc8.json", 'r', encoding='utf-8') as f:
    json_obj = json.loads(f.read())
    g_idx = 0
    for group in json_obj:
        g_idx += 1
        c_idx = 0
        # group_id = group['_id']
        group_name = group['name']
        for course in group['children']:
            c_idx += 1
            course_id = course['_id']
            course_name = course['name']
            filename = 'download\\wanmen\\G{0}_{1}_C{2}_{3}_{4}.json'\
                .format(g_idx, group_name, c_idx, course_name, course_id)

            get_course_detail(course_id, course_id, filename)
