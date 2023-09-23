import time

from todomvc_testing.model import todos


def test_open():
    todos.open()
    time.sleep(2)