# -*- coding: utf-8 -*-
import subprocess
import os


class FlutterLauncher:
    def __init__(self, args):
        self.file = "pubspec.yaml"
        self.reverse = args

    def __launcher(self, project_path, command):
        subprocess.run(["cd", project_path], shell=True)

        result = subprocess.run(f"flutter  {command} {project_path}", capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error running 'flutter pub get' on {project_path}:")
            print(result.stderr)

    def __find_pubspec_files(self, start_directory):
        pubspec_files = []

        for root, dirs, files in os.walk(start_directory):
            for file in files:
                if file == self.file:
                    pubspec_files.append(os.path.join(root, file))

        return pubspec_files

    def run(self, command):

        if self.reverse != 'desc' and self.reverse != 'asc':
            print(f'Command ({self.reverse}) not found !')
            return

        start_directory = os.getcwd()

        pubspec_files = self.__find_pubspec_files(start_directory)

        if self.reverse == 'desc':
            pubspec_files.reverse()

        if pubspec_files:
            for filepath in pubspec_files:
                dir_name = start_directory.split('/')[-1]
                pubspec_path = filepath.split(dir_name)[-1]
                path = pubspec_path[1:].replace(self.file, '')
                self.__launcher(path, command)
        else:
            print("Project FLUTTER not found.")
