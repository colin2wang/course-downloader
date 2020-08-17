from downloader_wanmen_constants import COURSE_ID
from utils.file_utils import get_files
from utils.log_utils import get_logger

logger = get_logger(__name__)


def verify_download_files(c_id):
    file_list = get_files('video_cache_all\\586d23485f07127674135d4d')

    file_name_dict = dict()
    file_count_dict = dict()

    for filename in file_list:
        elements = filename.split('\\')
        key = "{0}-{1}".format(elements[2], elements[3])

        # file count
        if key not in file_count_dict:
            file_count_dict[key] = 0
        count = file_count_dict[key]
        file_count_dict[key] = count + 1

        # file name
        file_name_dict[key] = elements[4]

    for key, name in file_name_dict.items():
        count = file_count_dict[key]
        if name != "Wanmen-{0}.ts".format("%05d" % (count - 1)):
            print("{}: filename: {}, count: {}\n".format(key, name, count))


if __name__ == "__main__":
    verify_download_files(COURSE_ID)
