from app.models import Task, Project
from datetime import datetime

def test_assign_task():
    p = Project("P")
    t = Task("T", "", datetime.now())
    p.add_task(t)
    assert t in p.tasks
