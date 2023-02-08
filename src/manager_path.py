class ManagePath:
    def save(self, path):
        with open('flutter_path', "w") as flutter_path:
            flutter_path.write(path)

    def get_path(self):
        try:
            with open('flutter_path', "r") as flutter_path:
                path = flutter_path.read()
                if path:
                    return path
                return None
        except FileNotFoundError:
            return None
