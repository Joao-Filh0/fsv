import requests
import re


def get_flutter_stable_versions():
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


numeric_versions = get_flutter_stable_versions()

if numeric_versions:
    print("Stable versions available")
    for version in numeric_versions:
        print(version)


#git describe --tags > version
#git --git-dir=/caminho/para/a/pasta/de/destino/flutter/.git --work-tree=/caminho/para/a/pasta/de/destino/flutter describe  --tags > /caminho/para/a/pasta/de/destino/flutter/version
#git clone --branch 2.5.3 https://github.com/flutter/flutter.git
#git clone https://github.com/flutter/flutter.git /caminho/para/a/pasta/de/destino
