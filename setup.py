from setuptools import setup,find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



setup(
    name='Mono_Python',
    version='0.0.1',
    author='Ibrahim Hamzat',
    author_email='hamat.ibrahim3@gmail.com',
    description="A mono client package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hamzzy/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)