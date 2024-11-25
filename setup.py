from setuptools import setup, find_packages

setup(
    name="ollama-diff-py",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rich>=13.0.0",
        "questionary>=1.10.0",
        "ollama==0.4.1",
    ],
    entry_points={
        "console_scripts": [
            "ollama-diff = ollama_diff.cli:run_model",
        ],
    },
    author="loadertsx",
    author_email="nahueldevelop@example.com",
    description="A tool to view git diff between branches and ask ollama questions",
    url="https://github.com/Nahuelluca20/ollama-diff-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
