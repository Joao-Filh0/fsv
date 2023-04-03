# -*- coding: utf-8 -*-
from src.list_version import list_version
from src.open_file import open_file
import os


def rename_version(arg: str, path_flutter: str, label: str, version_label: str):
    os.chdir(path_flutter)
    try:
        flutter_current_version_name = open_file(os.path.join(path_flutter, label, version_label), is_print=False)
        os.rename(label, flutter_current_version_name)
    except Exception as e:
        pass
    versions = list_version(path_flutter=path_flutter, version_label=version_label, label=label, is_print=False)
    if arg not in versions:
        print('Flutter version not found')
        return

    try:
        os.rename(arg, label)
        print(f'The current version is {arg}')
    except:
        print('Error not renamed')
