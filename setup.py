from setuptools import setup, find_packages

setup(
    name="CodeScout",
    version="0.1.0", 
    packages=find_packages(),
    install_requires=[
        "requests",
        "argparse",
        "openai"
    ],
    entry_points={
        "console_scripts": [
            "CodeScout=CodeScout.cli:main"
        ]
    },
    author="OriSavir",
    author_email="osavir1 at jhu dot edu",
    description="A CLI tool for reviewing code using LLMs, currently supports OpenAI models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OriSavir/CodeScout",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: Early-Stage Open Source"
    ],
    python_requires=">=3.8",
)
