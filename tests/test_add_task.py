from app.models import Task, Project
from datetime import datetime

def test_add_task():
    p = Project("Test")
    t = Task("T", "Desc", datetime.now())
    p.add_task(t)
    assert len(p.tasks) == 1
