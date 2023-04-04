# -*- coding: utf-8 -*-
import shutil
import os
from src.helpers.validate_platform import is_win
from  colorama import  Fore


def remove_folder(dir_path, required_permission=False, show_message=False):
    if show_message:
        print(f"{Fore.RED}Deleting ...\n")
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)

        if os.path.isfile(item_path):
            os.unlink(item_path)
        else:
            win = is_win()
            if win and required_permission:
                os.chmod(item_path, 0o700)
                os.system(f'rmdir /s /q "{item_path}"')
            else:
                shutil.rmtree(item_path)

    os.rmdir(dir_path)
