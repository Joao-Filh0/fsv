from setuptools import setup, find_packages

setup(
    name="fsv",
    version="0.0.4",
    description="Utilitários para desenvolvedor Flutter",
    author="João Alves",
    author_email="militaof522@gmail.com",
    packages=find_packages(),
    install_requires=[
        "argparse>=1.4.0",
    ],
    entry_points={
        "console_scripts": [
            "fsv=main:main"
        ]
    },
    python_requires=">=3.10.6",
)
