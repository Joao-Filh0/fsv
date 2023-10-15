import os


def create_new_feature(feature_name):
    if not feature_name:
        print("Por favor, forneça um nome de feature.")
        return

    base_dir = feature_name
    folders = [
        "core/data/datasources",
        "core/data/repositories",
        "core/data/models",
        "core/domain/usecases",
        "core/domain/repositories",
        "core/domain/entities",
        "ui/blocs",
        "ui/components",
        "ui/pages",
    ]

    try:
        os.makedirs(base_dir)
        for folder in folders:
            folder_path = os.path.join(base_dir, folder)
            os.makedirs(folder_path)

            file_name = os.path.basename(folder) + ".dart"
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'w') as f:
                pass

        feature_module_path = os.path.join(base_dir, f"{feature_name}_module.dart")
        with open(feature_module_path, 'w') as f:
            pass

        print(f"Estrutura de pastas e arquivos .dart criados para a feature '{feature_name}'.")

    except OSError as e:
        print(f"Erro ao criar a estrutura de pastas e arquivos: {e}")
