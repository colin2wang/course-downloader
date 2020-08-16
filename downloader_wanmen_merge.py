
from utils.file_utils import get_files, get_dirs
from utils.log_utils import get_logger
import subprocess

logger = get_logger(__name__)
dir_list = get_dirs('video_cache_all')

for dir_name in dir_list:
    elements = dir_name.split('\\')

    cmd = "cmd.exe /c merge_python.cmd \"{0}\" \"{1}\"".format(elements[1], elements[2])
    logger.info("command: {0}".format(cmd))

    ex = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = ex.communicate()
    status = ex.wait()
