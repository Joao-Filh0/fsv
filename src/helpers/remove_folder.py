# -*- coding: utf-8 -*-
import shutil
import os


def remove_folder(dir_path):
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            os.unlink(item_path)
        else:
            shutil.rmtree(item_path)

    os.rmdir(dir_path)
