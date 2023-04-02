# -*- coding: utf-8 -*-
from src.helpers.get_slash import get_slash
from src.helpers.remove_folder import remove_folder
from src.open_file import open_file
import os
import subprocess


class CloneFlutter:
    def __init__(self):
        self.slash = get_slash()

    def __rename_dir(self, path_flutter: str, label: str, version_label: str):
        flutter_current_version_name = open_file(path_flutter + f'{label}/{version_label}', is_print=False)
        os.chdir(path_flutter)
        try:
            os.rename(label, flutter_current_version_name)
        except Exception as e:
            print(f'Error {e}')

    def __set_file_version(self, path_flutter: str, label, version: str):
        with open(f'{path_flutter}{label}/version', 'w') as f:
            f.write(version)

    def clone(self, path_flutter, version: str, label: str, version_label: str):
        try:
            self.__rename_dir(path_flutter=path_flutter, label=label, version_label=version_label)
        except FileNotFoundError:
            pass
        print('Please await, fot the requested version ...')
        result = subprocess.run(
            f"git clone --branch {version} https://github.com/flutter/flutter.git {path_flutter}/{label}",
            capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            self.__set_file_version(path_flutter=path_flutter, label=label, version=version)
            remove_folder(f'{path_flutter}{label}{self.slash}examples')
        else:
            print(result.stderr)
