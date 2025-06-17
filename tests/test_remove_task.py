from app.models import Task, Project
from datetime import datetime

def test_remove_task():
    p = Project("Test")
    t = Task("T", "", datetime.now())
    p.add_task(t)
    p.remove_task("T")
    assert len(p.tasks) == 0
