import os


class GetFolderSize:

    def __get_size(self, path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                filepath = os.path.join(dirpath, file)
                total_size += os.path.getsize(filepath)
        return total_size

    def __convert_size(self, size_bytes):
        if size_bytes >= 2 ** 30:
            size_gb = size_bytes / 2 ** 30
            return f'{round(size_gb, 2)} GB'
        elif size_bytes >= 2 ** 20:
            size_mb = size_bytes / 2 ** 20
            return f'{round(size_mb, 2)} MB'
        elif size_bytes >= 2 ** 10:
            size_kb = size_bytes / 2 ** 10
            return f'{round(size_kb, 2)} KB'
        else:
            return f'{size_bytes} bytes'

    def run(self, path: str):
        print('Calculating the bytes ...')
        folder_size = self.__get_size(path)
        self.__convert_size(folder_size)
        print(f'{path}: {folder_size} bytes')
