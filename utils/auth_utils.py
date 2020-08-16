from utils.log_utils import get_logger

LOG = get_logger(__name__)


def parse_header(path, required=[]):
    header_list = []
    with open(path, 'r', encoding='utf-8') as f:
        _file_content = f.read()
        LOG.debug("File content: {0}".format(_file_content))
        _headers = _file_content.split("' -H '")

        for _header in _headers:
            elements = _header.split(":")
            if required.__contains__(elements[0]):
                t = (elements[0], elements[1])
                header_list.append(t)

    return header_list


def header_wanmen():
    header_list = parse_header('../auth_curl/wanmen_lecture.txt', ['authorization', 'x-app', 'x-token', 'x-time', 'authority'])
    header_list.append(('user-agent',
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 Maxthon/5.3.8.2000'))
    return header_list


if __name__ == '__main__':
    header = parse_header('../auth_curl/wanmen_lecture.txt', ['authorization', 'x-app', 'x-token', 'x-time', 'authority'])
    print(header)
