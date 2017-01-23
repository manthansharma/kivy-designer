from os import path, environ

from designer.app import DesignerApp
from designer.utils.utils import get_fs_encoding
from kivy.resources import resource_add_path


def main():
    data = path.join(path.dirname(path.abspath(__file__)), 'data')
    environ['designer_source_dir'] = path.dirname(path.abspath(__file__))
    if isinstance(data, bytes):
        data = data.decode(get_fs_encoding())
    resource_add_path(data)
    DesignerApp().run()


if __name__ == '__main__':
    main()
