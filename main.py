import argparse

from src.constants import description, path_flutter, version_label, label
from src.list_version import list_version
from src.manager_path import ManagePath
from src.pub_get.pub_get import PubGet
from src.rename_version import rename_version

parser = argparse.ArgumentParser(description=description)

parser.add_argument('--change', '-c', required=False)
parser.add_argument('--list', '-l', required=False, const='l', nargs='?')
parser.add_argument('--path', '-p', required=False)
parser.add_argument('--pub-get', '-pg', required=False, const='desc', nargs='?')

args = parser.parse_args()

manage_path = ManagePath()
get_path = manage_path.get_path()
config_path = get_path if get_path else path_flutter

if vars(args).get('change'):
    rename_version(arg=args.change, path_flutter=config_path, label=label, version_label=version_label)
elif vars(args).get('list'):
    list_version(path_flutter=config_path, version_label=version_label, label=label)
elif vars(args).get('path'):
    manage_path.save(args.path)
elif vars(args).get('pub_get'):
    pub_get = PubGet(args.pub_get)
    pub_get.run()
