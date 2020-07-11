from os import system
from sys import argv
from subprocess import call
from shutil import rmtree

def main():
    task = argv[1]
    if task == 'docs':
        system('mkdocs build')
    elif task == 'gh-pages':
        system('mkdocs gh-deploy')
    elif task == 'publish':
        rmtree('dist', ignore_errors=True)
        system('python setup.py sdist bdist_wheel')
        system('twine upload --repository testpypi dist/*')

if __name__ == '__main__': main()
