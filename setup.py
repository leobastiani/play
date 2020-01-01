import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="play",
    version="1.0.0",
    author="Leonardo Guarnieri de Bastiani",
    author_email="leogbastiani@gmail.com",
    description="Plays your music folder with VLC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leobastiani/play",
    install_requires=[
        'pathlib',
    ],
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['play=play:main'],
    },
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ]
)
