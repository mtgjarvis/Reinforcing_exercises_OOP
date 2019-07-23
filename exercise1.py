class Task:
    def __init__(self, due_date, description):
        self.due_date = due_date
        self.description = description
        

class TodoList:
    def __init__(self):
        self.tasks_list = []

    def add_task(self, due_date, description):
        self.tasks_list.append(Task(due_date, description))


TodoList.add_task('','Tomorrow', 'Saturday 5PM')
TodoList.add_task('','Friday 6PM', 'these exercises')
second_task = Task('Friday 7:30', 'drink beer')
third_task = Task('Friday 8:30', 'Have dinner')

