import time

from todomvc_testing.model import todos


def test_open():
    todos.open()
    time.sleep(2)
    time.sleep(2)
    todos.add('An', 'Ad', 'As')
    time.sleep(2)
    todos.should_be('An', 'Ad', 'As')
    time.sleep(2)
    todos.edit('An', 'An +++')
    time.sleep(2)
    todos.should_be('An +++', 'Ad', 'As')
    todos.edit_by_focus_change('Ad', 'Ad +++')
    todos.should_be('An +++', 'Ad +++', 'As')
    time.sleep(2)
    todos.toggle('As')
    time.sleep(2)
    todos.toggle_all()
    time.sleep(2)
    todos.clear_completed()
    time.sleep(2)
    todos.should_be_empty()
    time.sleep(2)
    todos.add('Here')
    time.sleep(2)
    todos.delete('Here')
    time.sleep(2)

