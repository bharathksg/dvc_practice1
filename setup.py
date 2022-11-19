from setuptools import setup,find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_decription=f.read()

setup(
    name="src",
    version="0.0.1",
    author="bharathksg",
    description="A small package for ml",
    long_description=long_decription,
    long_decription_content_type="text/markdown",
    author_email="bharath100ksg@gmail.com",
    url="https://github.com/bharathksg/dvc_practice1",
    package_dir={"":"src"},
    packages=find_packages(where="src"),license="GNU",
    python_requires="3.9",
    install_requires=[
        'scikit_learn',
        'pandas',
        'numpy',
        'dvc'
        ]

)