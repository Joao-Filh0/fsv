# -*- coding: utf-8 -*-
from colorama import Fore, Style


def open_file(path: str, message='', is_print=True, check=''):
    with open(path, "r") as version:
        read_version = version.read()

        if is_print:
            version = message + read_version
            if check:
                color = Fore.GREEN
            else:
                color = Fore.YELLOW
            try:
                print(color + version + check + Style.RESET_ALL)
            except Exception:
                print(color + version + " v" if check else "" + Style.RESET_ALL)
        else:
            version = read_version
        return version
