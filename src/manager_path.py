from src.constants import success_config_path, error_config_path


class ManagePath:
    def save(self, path):
        with open('flutter_path', "w") as flutter_path:
            flutter_path.write(path)

    def get_path(self):
        try:
            with open('flutter_path', "r") as flutter_path:
                path = flutter_path.read()
                if path:
                    print(success_config_path)
                    return path
                return None
        except FileNotFoundError:
            print(error_config_path)
            return None
