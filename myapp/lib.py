import pathlib
import importlib.resources

from myapp import resources


def lib_fun(file_path: str):
    print('ext lib received path:', file_path)
    path = pathlib.Path(file_path)
    content = file_path.read_text()
    print('ext lib loaded:', content)


def run():
    with importlib.resources.path(resources, 'res.txt') as path:
        print('res', type(path), path)
        lib_fun(path)

