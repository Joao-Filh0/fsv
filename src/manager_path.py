# -*- coding: utf-8 -*-
from src.constants import success_config_path, error_config_path

import platform
import os


class ManagePath:
    def save(self, path):
        try:
            with open('flutter_path', "w") as flutter_path:

                if platform.system() != 'Windows':
                    path = os.path.join('/', path)
                flutter_path.write(path)
                print(success_config_path, end='')
                print(': ' + path)

        except:
            print(error_config_path)

    def get_path(self):
        try:
            with open('flutter_path', "r") as flutter_path:
                path = flutter_path.read()
                if path:
                    return path
                return None
        except FileNotFoundError:
            return None
