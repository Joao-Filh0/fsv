from src.open_file import open_file
import os, subprocess


class CloneFlutter:
    def __init__(self):
        pass

    def __rename_dir(self, path_flutter: str, label: str, version_label: str):
        flutter_current_version_name = open_file(path_flutter + f'{label}/{version_label}', is_print=False)
        os.chdir(path_flutter)
        try:
            os.rename(label, flutter_current_version_name)
        except Exception as e:
            print(f'Error {e}')

    def __set_file_version(self, path_flutter: str, label):
        result = subprocess.run(
            f"git --git-dir={path_flutter}{label}/.git --work-tree={path_flutter}{label} describe  --tags > {path_flutter}{label}/version",
            capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            print(result.stdout)
        else:
            print(result.stderr)

    def clone(self, path_flutter, version: str, label: str, version_label: str):
        self.__rename_dir(path_flutter=path_flutter,label=label,version_label=version_label)
        result = subprocess.run(f"git clone --branch {version} https://github.com/flutter/flutter.git {path_flutter}",
                                capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            self.__set_file_version(path_flutter=path_flutter,label=label)
            print(result.stdout)
        else:
            print(result.stderr)
