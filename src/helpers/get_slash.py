import platform


def get_slash():
    if platform.system() == 'Windows':
        return '\\'
    return '/'
