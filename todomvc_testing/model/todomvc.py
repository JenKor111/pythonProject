from selene import have, command
from selene.support.shared import browser

completed = have.css_class('completed')


class TodoMVC:

    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open(self):
        browser.open('https://todomvc.com/examples/emberjs/')
        return self

