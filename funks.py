import argparse


def create_parser():
    """Делаем парсер для аргументов командной строки"""
    parser = argparse.ArgumentParser()
    parser.add_argument("way_2_folder")
    parser.add_argument("--loop", type=int, default=2)
    parser.add_argument("--ip", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9090)
    return parser


def get_args():
    """Получаем аргументы"""
    parser = create_parser()
    namespace = parser.parse_args()
    return namespace.loop, namespace.ip, namespace.port


def get_path():
    """Получаем путь до папки"""
    parser = create_parser()
    namespace = parser.parse_args()
    return namespace.way_2_folder