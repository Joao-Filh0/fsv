# -*- coding: utf-8 -*-
import re
import requests


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

    def run(self):
        print('Search Flutter Stables Versions ...')

        numeric_versions = self.__get_versions()

        if numeric_versions:
            print("Stable versions available")
            for version in numeric_versions:
                print(f'Stable = {version}')

