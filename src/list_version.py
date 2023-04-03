# -*- coding: utf-8 -*-
import os

from src.constants import message, command_path
from src.open_file import open_file


def list_version(path_flutter: str, version_label: str, label: str, is_print=True):
    if not path_flutter:
        print(message)
        print(command_path)
        return
    versions = os.listdir(path_flutter)

    for v in versions:
        if v[0] != '.':
            flutter = os.listdir(os.path.join(path_flutter, v))
            if version_label in flutter:
                path = os.path.join(path_flutter, v, version_label)
                open_file(path, message=f'{label} : ', is_print=is_print,
                          check=' ✔' if label == v else '')
    return versions
