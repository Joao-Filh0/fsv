from src.constants import success_config_path, error_config_path

import platform


class ManagePath:
    def save(self, path):
        try:
            with open('flutter_path', "w") as flutter_path:

                if platform.system() != 'Windows':
                    end_path = path[-1]
                    start_path = path[0]
                    p1 = '/'
                    if end_path != p1:
                        path = path + p1
                    if start_path != p1:
                        path = p1 + path
                flutter_path.write(path)
                print(success_config_path, end='')
                print(': ' + path)

        except:
            print(error_config_path)

    def get_path(self):
        try:
            with open('flutter_path', "r") as flutter_path:
                path = flutter_path.read()
                if path:
                    return path
                return None
        except FileNotFoundError:
            return None
