import subprocess

from downloader_wanmen_constants import COURSE_ID
from utils.file_utils import get_dirs
from utils.log_utils import get_logger

logger = get_logger(__name__)


def merge_course_videos(c_id):
    dir_list = get_dirs('video_cache_all\\{0}'.format(c_id))

    for dir_name in dir_list:
        elements = dir_name.split('\\')

        cmd = "cmd.exe /c merge_python.cmd {0} \"{1}\" \"{2}\"".format(elements[1], elements[2], elements[3])
        logger.info("command: {0}".format(cmd))

        ex = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = ex.communicate()
        status = ex.wait()


if __name__ == "__main__":
    merge_course_videos(COURSE_ID)
