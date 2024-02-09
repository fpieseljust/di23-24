import pathlib
from setuptools import setup

# El directorio que contiene este archivo
directorio_raiz = pathlib.Path(__file__).parent

# El texto del archivo README
README = (directorio_raiz / "README.md").read_text()

# Esta llamada a setup() hace todo el trabajo
setup(
    name="holamundopyside6_XXX",
    version="0.0.1",
    description="Hola mundo con pyside6",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["holamundopyside6"],
    include_package_data=True,
    install_requires=["PySide6"],
    entry_points={
        "console_scripts": [
            "holamundopyside6=holamundopyside6.__main__:main",
        ]
    },
)