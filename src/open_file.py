# -*- coding: utf-8 -*-
def open_file(path: str, message='', is_print=True, check=''):
    with open(path, "r") as version:
        version = message + version.read()
        if is_print:
            print(version+check)
        return version
