# -*- coding: utf-8 -*-

import argparse

from src.constants import (description, version_label,
                           label, not_found_path,
                           message_current_path,
                           message, command_path, change_message, list_message, path_message, pull_message,
                           remove_message, pub_get_message, list_stable_message, memory_message)
from src.delete_flutter_version.delete_flutter_version import DeleteFlutterVersion
from src.flutter_origin.clone_flutter import CloneFlutter
from src.flutter_origin.get_version_origin import GetFlutterStableVersions
from src.get_folder_sizes.get_folder_size import GetFolderSize
from src.list_version import list_version
from src.manage_path.manager_path import ManagePath
from src.new_feature.new_feature import create_new_feature
from src.flutter_launcher.flutter_launcher import FlutterLauncher
from src.rename_version import rename_version


def main():
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--change', '-c', required=False, help=change_message)
    parser.add_argument('--list', '-l', required=False, const='l', nargs='?', help=list_message)
    parser.add_argument('--path', '-p', required=False, help=path_message)
    parser.add_argument('--pull', '-pl', required=False, help=pull_message)
    parser.add_argument('--remove', '-rm', required=False, help=remove_message)
    parser.add_argument('--pub-get', '-pg', required=False, const='desc', nargs='?', help=pub_get_message)
    parser.add_argument('--pub-upgrade', '-pu', required=False, const='desc', nargs='?', help="flutter pub upgrade")
    parser.add_argument('--clean', '-cls', required=False, const='desc', nargs='?', help="flutter clean")
    parser.add_argument('--view-path', '-vp', required=False, const='vp', nargs='?')
    parser.add_argument('--list-stable', '-ls', required=False, const='ls', nargs='?', help=list_stable_message)
    parser.add_argument('--memory', '-m', required=False, const='m', nargs='?', help=memory_message)
    parser.add_argument('--new-feature', '-nf', required=True)

    args = parser.parse_args()

    manage_path = ManagePath()
    config_path = manage_path.get_flutter_path()
    if config_path is None:
        print('Add a path where you would like\n flutter to be installed')
        print(command_path)
        return

    elif vars(args).get('change'):
        rename_version(arg=args.change, path_flutter=config_path, label=label, version_label=version_label)
        return

    elif vars(args).get('list'):
        list_version(path_flutter=config_path, version_label=version_label, label=label)
        return

    elif vars(args).get('path'):
        manage_path.save(args.path)
        return

    elif vars(args).get('view_path'):
        if config_path:
            print(f'{message_current_path} : {config_path}')
        else:
            print(not_found_path)
            print(message)
            print(command_path)
        return

    elif vars(args).get('pub_get'):
        pub_get = FlutterLauncher(args.pub_get)
        pub_get.run('pub get')
        return

    elif vars(args).get('clean'):
        pub_get = FlutterLauncher(args.pub_get)
        pub_get.run('clean')
        return

    elif vars(args).get('pub_upgrade'):
        pub_get = FlutterLauncher(args.pub_get)
        pub_get.run('pub upgrade')
        return

    elif vars(args).get('list_stable'):
        list_flutter_origin_stable = GetFlutterStableVersions()
        list_flutter_origin_stable.run(path=config_path)
        return

    elif vars(args).get('pull'):
        pull = CloneFlutter()
        pull.clone(path_flutter=config_path, version=args.pull, label=label, version_label=version_label)
        return

    elif vars(args).get('memory'):
        memory = GetFolderSize()
        memory.run(path=config_path)
        return

    elif vars(args).get('remove'):
        remove = DeleteFlutterVersion()
        remove.run(path=config_path, version_label=version_label, set_version=args.remove)
        return
    elif vars(args).get('new_feature'):
        create_new_feature(args.new_feature)
        return
    return


if __name__ == "__main__":
    main()
