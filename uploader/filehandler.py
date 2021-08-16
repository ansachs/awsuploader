import os
from collections import namedtuple

File = namedtuple('File', ['path', 'filename'])


def list_files(directory_path: str) -> list[File]:
    all_files = list()
    top_files = os.listdir(directory_path)

    for file in top_files:
        path = os.path.join(directory_path, file)
        if os.path.isdir(path):
            all_files.extend(list_files(path))
        else:
            all_files.append(File(path=path, filename=file))

    return all_files
