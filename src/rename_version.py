from src.helpers.get_slash import get_slash
from src.list_version import list_version
from src.open_file import open_file
import os


def rename_version(arg: str, path_flutter: str, label: str, version_label: str):
    slash = get_slash()
    flutter_current_version_name = open_file(path_flutter + f'{label}{slash}{version_label}', is_print=False)
    versions = list_version(path_flutter=path_flutter, version_label=version_label, label=label, is_print=False)
    if arg not in versions:
        print('Flutter version not found')
        return
    os.chdir(path_flutter)
    try:
        os.rename(label, flutter_current_version_name)
        os.rename(arg, label)
        print(f'The current version is {arg}')
    except:
        print('Error not renamed')
