# -*- coding: utf-8 -*-
import shutil
import os
from src.helpers.validate_platform import is_win


def remove_folder(dir_path):
    print("Deleting ...")
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)

        if os.path.isfile(item_path):
            os.unlink(item_path)
        else:
            win = is_win()
            if win:
                os.chmod(item_path, 0o700)
                os.system(f'rmdir /s /q "{item_path}"')
            else:
                shutil.rmtree(item_path)

    os.rmdir(dir_path)
