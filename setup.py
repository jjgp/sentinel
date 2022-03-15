from setuptools import find_packages, setup

install_requires = [
    "click >= 8.0",
    "numpy >= 1.22",
    "tensorflow >= 2.8",
]

extras_require = {
    "dev": [
        "black",
        "flake8 >= 4.0",
        "isort >= 5.9",
        "pre-commit >= 2.16",
        "pytest >= 7.1",
    ],
}

setup(
    name="sentinel",
    version="0.0.1",
    url="https://github.com/jjgp/sentinel",
    author="Jason Prasad",
    author_email="jasongprasad@gmail.com",
    description="Land use classification using satelite imaging ",
    install_requires=install_requires,
    extras_require=extras_require,
    packages=find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": ["sentinel = src.sentinel.cli.cli:main"],
    },
)
