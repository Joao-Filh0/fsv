import argparse

from src.constants import (description, version_label,
                           label, not_found_path,
                           message_current_path,
                           message, command_path)
from src.flutter_origin.clone_flutter import CloneFlutter
#from src.flutter_origin.get_version_origin import GetFlutterStableVersions
from src.get_folder_sizes.get_folder_size import GetFolderSize
from src.list_version import list_version
from src.manager_path import ManagePath
from src.pub_get.pub_get import PubGet
from src.rename_version import rename_version


def main():
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--change', '-c', required=False)
    parser.add_argument('--list', '-l', required=False, const='l', nargs='?')
    parser.add_argument('--path', '-p', required=False)
    parser.add_argument('--pull', '-pl', required=False)
    parser.add_argument('--pub-get', '-pg', required=False, const='desc', nargs='?')
    parser.add_argument('--view-path', '-vp', required=False, const='vp', nargs='?')
    parser.add_argument('--list-stable', '-ls', required=False, const='ls', nargs='?')
    parser.add_argument('--memory', '-m', required=False, const='m', nargs='?')

    args = parser.parse_args()

    manage_path = ManagePath()
    get_path = manage_path.get_path()
    config_path = get_path

    if vars(args).get('change'):
        rename_version(arg=args.change, path_flutter=config_path, label=label, version_label=version_label)
    elif vars(args).get('list'):
        list_version(path_flutter=config_path, version_label=version_label, label=label)
    elif vars(args).get('path'):
        manage_path.save(args.path)
    elif vars(args).get('view_path'):
        if config_path:
            print(f'{message_current_path} : {config_path}')
        else:
            print(not_found_path)
            print(message)
            print(command_path)

    elif vars(args).get('pub_get'):
        pub_get = PubGet(args.pub_get)
        pub_get.run()

    # elif vars(args).get('list_stable'):
    #     list_flutter_origin_stable = GetFlutterStableVersions()
    #     list_flutter_origin_stable.run()

    elif vars(args).get('pull'):
        pull = CloneFlutter()
        pull.clone(path_flutter=config_path, version=args.pull, label=label, version_label=version_label)

    elif vars(args).get('memory'):
        pull = GetFolderSize()
        pull.run(path=config_path)


if __name__ == "__main__":
    main()
