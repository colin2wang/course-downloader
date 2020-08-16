import os


def get_files(path):
    _file_list = []
    read_files0(path, _file_list)
    return _file_list


def read_files0(path, _file_list):
    files = os.listdir(path)

    for fi in files:
        file_name = os.path.join(path, fi)
        if os.path.isdir(file_name):
            read_files0(file_name, _file_list)
        else:
            _file_list.append(file_name)


def get_dirs(path):
    _dir_list = []
    read_dirs0(path, _dir_list)
    return _dir_list


def read_dirs0(path, _dir_list):
    files = os.listdir(path)

    for fi in files:
        file_name = os.path.join(path, fi)
        if os.path.isdir(file_name):
            read_dirs0(file_name, _dir_list)
        else:
            if not _dir_list.__contains__(path):
                _dir_list.append(path)


if __name__ == '__main__':
    dirs = get_dirs('../../video_cache_all')
    print(dirs)
