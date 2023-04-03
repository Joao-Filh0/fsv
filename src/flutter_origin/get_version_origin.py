# -*- coding: utf-8 -*-
import re
import requests
from colorama import Fore, Style

from src.helpers.get_version_helper import get_version_helper


class GetFlutterStableVersions:
    def __get_versions(self):
        url = "https://api.github.com/repos/flutter/flutter/tags"
        page = 1
        per_page = 100
        numeric_versions = []

        while True:
            response = requests.get(url, params={'page': page, 'per_page': per_page})

            if response.status_code == 200:
                tags = response.json()

                if not tags:
                    break

                for tag in tags:
                    if re.match(r'^\d+(\.\d+)*$', tag['name']):
                        numeric_versions.append(tag['name'])

                if len(tags) < per_page:
                    break

                page += 1
            else:
                print(f"Error: {response.status_code}")
                return None

        return numeric_versions

    def run(self, path: str):
        print('Search Flutter Stables Versions ...')

        numeric_versions = self.__get_versions()
        numeric_versions.reverse()
        list_versions = get_version_helper(path=path)

        if numeric_versions:
            print("Stable versions available")
            for version in numeric_versions:
                if version in list_versions:
                    print(f'{Fore.GREEN} Stable = {version} <------- {Style.RESET_ALL}')
                else:
                    print(f'{Fore.YELLOW} Stable = {version} {Style.RESET_ALL}')
