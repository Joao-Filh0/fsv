import os

from src.open_file import open_file


def list_version(path_flutter: str, version_label: str, label: str, is_print=True):
    versions = os.listdir(path_flutter)
    for v in versions:
        if v[0] != '.':
            flutter = os.listdir(path_flutter + f'{v}')
            if version_label in flutter:
                open_file(path_flutter + v + f'/{version_label}', message=f'{label} : ', is_print=is_print,
                          check='  ✓' if label == v else '')
    return versions
