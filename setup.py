from setuptools import setup, find_packages

setup(
    name="fsv",
    version="0.0.17",
    description="Utilitários para desenvolvedor Flutter",
    author="João Alves",
    author_email="militaof522@gmail.com",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "requests",
        "colorama",
        "argparse>=1.4.0",

    ],
    entry_points={
        "console_scripts": [
            "fsv=main:main"
        ]
    },
    python_requires=">=3.10.6",
)
