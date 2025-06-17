from app.models import Task, Project
from datetime import datetime

def test_filter():
    p = Project("P")
    t = Task("A", "", datetime.now())
    p.add_task(t)
    assert p.get_tasks_by_status(False)
