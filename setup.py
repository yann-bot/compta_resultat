from setuptools import setup, find_packages

setup(
    name="mon_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Liste des dépendances comme "numpy", "requests", etc.
    ],
    author="Yann Dubois Ouafete",
    author_email="yannouafete@gmail.com",
    description="Une brève description de ton package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yann-bot/compat_resultat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
