# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import re

from colorama import Fore, Style


class GetFolderSize:
    def _convert_size(self, size_bytes: int) -> str:
        try:
            if size_bytes < 0:
                raise ValueError("Error")
            elif size_bytes >= 2 ** 30:
                size_in_gb = size_bytes / 2 ** 30
                return f"{round(size_in_gb, 2)} GB"
            elif size_bytes >= 2 ** 20:
                size_in_mb = size_bytes / 2 ** 20
                return f"{round(size_in_mb, 2)} MB"
            elif size_bytes >= 2 ** 10 or size_bytes == 1:
                size_in_kb = size_bytes / 2 ** 10
                return f"{round(size_in_kb, 2)} KB"
            else:
                return f"{size_bytes} bytes"
        except ValueError as e:
            print(e)

    def _get_folder_size(self, path: str) -> str:
        try:
            if not os.path.isdir(path):
                raise ValueError("Error")
            size_bytes = sum(
                os.path.getsize(os.path.join(dirpath, filename)) for dirpath, _, filenames in os.walk(path) for filename
                in filenames)
            return self._convert_size(size_bytes)
        except ValueError as e:
            print(e)

    def run(self, path: str):
        print(f'{Fore.LIGHTGREEN_EX}Calculating the bytes ...')
        path = os.path.normpath(path)
        total_size_bytes = 0

        for subdir in os.listdir(path):
            subdir_path = os.path.join(path, subdir)
            if os.path.isdir(subdir_path):
                if re.match(r"^\d+(\.\d+)*$", subdir) or "flutter" in subdir.lower():
                    total_size_bytes += sum(
                        os.path.getsize(os.path.join(dirpath, filename)) for dirpath, _, filenames in os.walk(subdir_path) for filename
                        in filenames)

        total_size = self._convert_size(total_size_bytes)
        print(f'{Fore.LIGHTBLUE_EX}Used --> {total_size}{Style.RESET_ALL}')



