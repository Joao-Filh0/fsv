# -*- coding: utf-8 -*-
import platform


def get_slash():
    if platform.system() == 'Windows':
        return '\\'
    return '/'
