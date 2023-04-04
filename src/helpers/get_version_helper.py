import os


def get_version_helper(path: str):
    folders = os.listdir(path)
    list_version = []
    for folder in folders:
        if 'flutter' == folder or folder[0].isnumeric():
            new_path = os.path.join(path, folder, 'version')
            try:
                with open(new_path, "r") as version:
                    version = version.read().replace(" ", "")
                    list_version.append(version)
            except Exception as e:
                print(e)
    return list_version
