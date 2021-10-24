from app.Controllers import Controller
from app.Models import Tasks


class TasksController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._tasks = Tasks()

    def index(self):
        tasks = self._tasks.all()
        return self._render_template("tasks.html", tasks = tasks)

    def create(self):
        return self._render_template("create-task.html")

    def store(self):
        attributes = {
            'name': self._request.form['name'],
            'description': self._request.form['description'],
            'user_id': str(68)
        }
        if not self._tasks.create(attributes)['id']:
            self._flash('Failed to register!')
            self._redirect('/tasks/create')

        return self._redirect('/tasks')