import os

from src.helpers.remove_folder import remove_folder


class DeleteFlutterVersion:
    def __candidate_version(self, path: str, version_label: str, set_version: str):

        folders = os.listdir(path)
        for folder in folders:
            if 'flutter' in folder or folder[0].isnumeric():
                new_path = os.path.join(path, folder, version_label)
                with open(new_path, "r") as version:
                    version = version.read().replace(" ", "")

                    if set_version == version.replace(" ", ""):
                        return os.path.join(path, folder)

        return None

    def run(self, path: str, version_label: str, set_version: str):

        folder = self.__candidate_version(path, version_label, set_version)
        if folder:
            remove_folder(folder)
            print(f'Version {set_version} removed')
        else:
            print(f'Version {set_version} not found')
