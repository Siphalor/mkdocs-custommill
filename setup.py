import yaml
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()

with open("mkdocs.yml", "r") as yml:
    conf = yaml.safe_load(yml.read())
    version = conf['extra']['version'][1:]

setup(
    name="mkdocs-custommill",
    version=version,
    url='https://github.com/Siphalor/mkdocs-custommill',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    install_requires=[
        'mkdocs',
    ],
    license='MIT',
    description='Improved and extended version of the Windmill theme',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Siphalor',
    author_email='dev@siphalor.de',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'custommill = mkdocs_custommill',
        ]
    },
    zip_safe=False
)
