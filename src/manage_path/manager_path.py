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

    def get_flutter_path(self):
        path = self.get_path()
        if path is None:
            flutter_path = None
            paths = os.environ['PATH'].split(os.pathsep)
            path_base = os.path.join("flutter", "bin")
            for path in paths:
                if path_base in path:
                    flutter_path = path[:path.find(path_base)]
                    break
            return flutter_path
        return path
