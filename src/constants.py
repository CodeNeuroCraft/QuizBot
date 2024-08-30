import os


ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE_PATH: str = os.path.join(ROOT_DIR, 'config.yaml')
VERSION: str = '1.0'


__all__ = [
    'CONFIG_FILE_PATH',
    'ROOT_DIR',
    'VERSION',
]