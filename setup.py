from setuptools import setup, find_packages

setup(
    name="ollama-diff",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "questionary",
    ],
    entry_points={
        "console_scripts": [
            "ollama-diff=ollama_diff.cli:run_model",
        ],
    },
)
