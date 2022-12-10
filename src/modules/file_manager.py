import os
from dataclasses import dataclass

import zipfile
import shutil

@dataclass
class File:
    path: str
    directory: str
    file: str
    file_name: str
    file_extension: str


@dataclass
class Files:
    list : list[File]

    def add(self, file: File):
        self.list.append(file)


def process_path(path: str) -> File:
    path_1 = os.path.split(path)
    directory = path_1[0]
    file = path_1[1]
    path_2 = os.path.splitext(file)
    file_name = path_2[0]
    file_extension = path_2[1]
    return File(
        path=path,
        directory=directory,
        file=file,
        file_name=file_name,
        file_extension=file_extension)


def process_list_of_path(path_list: list[str]) -> Files:
    file_list = Files([])
    for path in path_list:
        splited_path = process_path(path=path)
        file_list.add(splited_path)
    return file_list 


def unzip_file(file_path: str, extract_path: str) -> None:
    shutil.unpack_archive(file_path, extract_path)


if __name__ == "__main__":
    path_1 = 'H:/Users/seba/Desktop/Temp_job (2).zip'
    path_2 = 'H:/Users/seba/Desktop/Temp_job.zip'
    file_1 = process_path(path_1)
    file_2 = process_path(path_2)
    lst = Files([])

    lst.add(file_1)
    print(lst)
    lst.add(file_2)
    print(lst)
